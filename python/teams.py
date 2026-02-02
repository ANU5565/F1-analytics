from db_connect import get_connection

def get_team_standings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.team_name, SUM(r.points) AS total_points
        FROM race_results r
        JOIN drivers d ON r.driver_id = d.driver_id
        JOIN teams t ON d.team_id = t.team_id
        GROUP BY t.team_id
        ORDER BY total_points DESC
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results
    