import os

import mysql.connector
from mysql.connector import Error


def create_connection():
    password = os.environ.get("MYSQL_PASSWORD")
    if password is None:
        print("MySQL Connection Error: MYSQL_PASSWORD environment variable is not set.")
        return None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="smart_crop_db"
        )

        if connection.is_connected():
            print("MySQL Database Connected Successfully!")
            return connection

    except Error as e:
        print("MySQL Connection Error:", e)

    return None


if __name__ == "__main__":
    connection = create_connection()

    if connection:
        connection.close()
        print("Database connection closed.")
