from db_connect import get_connection

def get_all_drivers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT driver_name, wins FROM drivers")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data
