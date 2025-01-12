# Connect to the Database in Your Project: Use the configuration 
# details to connect to the MySQL database in your project. Here 
# is an example using mysql-connector-python:

import mysql.sitepackages.connector
from db_config import db_config

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Example usage
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")
        cursor.close()
        conn.close()

import psycopg2
from db_config import db_config

## To connect to a PostgreSQL database instead of MySQL
def connect_to_db():
    try:
        connection = psycopg2.connect(**db_config)
        print("Connected to PostgreSQL database")
        return connection
    except psycopg2.Error as err:
        print(f"Error: {err}")
        return None

# Example usage
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT current_database();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")
        cursor.close()
        conn.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)



