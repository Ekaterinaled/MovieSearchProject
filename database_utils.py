import mysql.connector
from mysql.connector import Error
from config import SAKILA_DB_CONFIG, LOG_DB_CONFIG

def connect_db(config):
    """Establishes a database connection."""
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except Error as e:
        print(f"❌ Connection error: {e}")
        return None
