# db_config.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # 🔁 Replace with your actual MySQL password
        database="bankdb"
    )