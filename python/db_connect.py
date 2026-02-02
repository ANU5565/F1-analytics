import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anuroop@999",
        database="f1_analytics"
    )
