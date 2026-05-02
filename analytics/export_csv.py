import sqlite3
import csv
from pathlib import Path

# Path to your SQLite database
DB_PATH = Path("app.db")

# Folder where CSVs will be written
OUT_DIR = Path("analytics") / "exports"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def export_query_to_csv(conn, sql: str, params: tuple, out_path: Path):
    """
    Runs a SQL query and writes the results to a CSV file.
    """
    cur = conn.cursor()
    cur.execute(sql, params)

    # Column names from the query
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(rows)

    print(f"Wrote {out_path} ({len(rows)} rows)")


def main():
    # Safety check
    if not DB_PATH.exists():
        raise FileNotFoundError("app.db not found. Make sure it exists in repo root.")

    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")

    # 1) Raw reservations dataset
    export_query_to_csv(
        conn,
        """
        SELECT
            r.id,
            r.user_id,
            u.email AS user_email,
            r.date,
            r.party_size,
            r.notes,
            r.created_at
        FROM reservations r
        JOIN users u ON u.id = r.user_id
        ORDER BY r.created_at DESC
        """,
        (),
        OUT_DIR / "reservations_raw.csv"
    )

    # 2) Daily metrics
    export_query_to_csv(
        conn,
        """
        SELECT
            substr(r.created_at, 1, 10) AS created_date,
            COUNT(*) AS reservations_created,
            AVG(r.party_size) AS avg_party_size
        FROM reservations r
        GROUP BY substr(r.created_at, 1, 10)
        ORDER BY created_date ASC
        """,
        (),
        OUT_DIR / "daily_metrics.csv"
    )

    # 3) Party size distribution
    export_query_to_csv(
        conn,
        """
        SELECT
            r.party_size,
            COUNT(*) AS count_reservations
        FROM reservations r
        GROUP BY r.party_size
        ORDER BY r.party_size ASC
        """,
        (),
        OUT_DIR / "party_size_distribution.csv"
    )

    conn.close()


if __name__ == "__main__":
    main()
