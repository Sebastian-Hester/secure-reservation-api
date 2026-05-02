import sqlite3
import csv

conn = sqlite3.connect("app.db")
cur = conn.cursor()

exports = [
    (
        "reservations_raw.csv",
        "SELECT * FROM reservations"
    ),
    (
    "daily_metrics.csv",
    """
    SELECT 
        date AS "Created Date",
        COUNT(*) AS "Reservations Created",
        AVG(party_size) AS "Avg Party Size",
        CASE strftime('%w', date)
            WHEN '0' THEN 'Sun'
            WHEN '1' THEN 'Mon'
            WHEN '2' THEN 'Tue'
            WHEN '3' THEN 'Wed'
            WHEN '4' THEN 'Thu'
            WHEN '5' THEN 'Fri'
            WHEN '6' THEN 'Sat'
        END AS "Day of Week",
        CAST(strftime('%w', date) AS INTEGER) + 1 AS "Weekday Number"
    FROM reservations
    GROUP BY date
    ORDER BY date
    """
    ),
    (
        "party_size_distribution.csv",
        """
        SELECT 
            party_size AS "Party Size",
            COUNT(*) AS "Reservations"
        FROM reservations
        GROUP BY party_size
        ORDER BY party_size
        """
    ),
]

for filename, query in exports:
    cur.execute(query)
    rows = cur.fetchall()
    headers = [d[0] for d in cur.description]

    with open(f"analytics/exports/{filename}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Updated analytics/exports/{filename} with {len(rows)} rows")

conn.close()