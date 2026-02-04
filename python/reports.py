import pandas as pd
from db_connect import get_connection

conn = get_connection()

df = pd.read_sql("""
    SELECT d.driver_name, SUM(r.points) AS total_points
    FROM race_results r
    JOIN drivers d ON r.driver_id = d.driver_id
    GROUP BY d.driver_id
""", conn)

conn.close()

df.to_csv("driver_standings.csv", index=False)
df.to_excel("driver_standings.xlsx", index=False)

print ("Reports generated successfully")

