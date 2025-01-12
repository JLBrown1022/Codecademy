# To connect your project to a MySQL database managed by Homebrew
# you need to install the mysql-connector-python package.
####################################################################
# Ensure MySQL is Running: Start the MySQL service if it is not.
# Create a Database Configuration File: Create a configuration file 
# (e.g., db_config.py) to store your database connection details.
# Update the Configuration File: Modify your db_config.py to include
# MySQL connection details.
# Connect to the Database: Use the mysql-connector-python package to
# connect to your MySQL database.
####################################################################

# MySQL database configuration details:
db_config_mysql = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'subscriptions',
    'charset': 'utf8'
},

# To connect your project to a MySQL database managed by Homebrew
# 
# Create a Database Configuration File: Create a configuration file 
# (e.g., db_config.py) to store your database connection details.
# Update the Configuration File: Modify your db_config.py to include 
# PostgreSQL connection details.
# PostgreSQL database configuration details:

db_config_postgres = {
    'dbname': 'subscriptions',
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1',
    'port': '5432',
}

