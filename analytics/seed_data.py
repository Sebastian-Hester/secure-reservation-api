import sqlite3
from datetime import datetime, timedelta
import random

DB_PATH = "app.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Find an existing user (we'll attach reservations to them)
    cur.execute("SELECT id FROM users LIMIT 1")
    row = cur.fetchone()

    if not row:
        raise RuntimeError("No users found. Register a user first.")

    user_id = row[0]

    base_date = datetime.now()

    sample_reservations = []

    for i in range(15):
        created_at = base_date - timedelta(days=random.randint(0, 14))
        reservation_date = created_at.date() + timedelta(days=random.randint(1, 10))

        sample_reservations.append(
            (
                user_id,
                reservation_date.isoformat(),
                random.choice([2, 3, 4, 5, 6]),
                random.choice(
                    [
                        "Window seat",
                        "Birthday",
                        "High chair needed",
                        "Anniversary",
                        "Quiet area",
                        None,
                    ]
                ),
                created_at.isoformat(),
            )
        )

    cur.executemany(
        """
        INSERT INTO reservations (user_id, date, party_size, notes, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        sample_reservations,
    )

    conn.commit()
    conn.close()

    print(f"Inserted {len(sample_reservations)} sample reservations")

if __name__ == "__main__":
    main()
