from mysql_connector import get_mysql_connection
import csv

# Get MariaDB connection
conn = get_mysql_connection()

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# SQL query to select all data from the 'orders' table
orders_query = 'SELECT * FROM orders'

# Execute the 'orders' query
cursor.execute(orders_query)

# Fetch all rows from the result set
orders_data = cursor.fetchall()

# Define the filename for the 'orders' CSV file
orders_filename = 'orders.csv'

# Write the 'orders' data to a CSV file
with open(orders_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])  # Write column headers
    writer.writerows(orders_data)

# SQL query to select all data from the 'orders_quantity' table
orders_quantity_query = 'SELECT * FROM orders_quantity'

# Execute the 'orders_quantity' query
cursor.execute(orders_quantity_query)

# Fetch all rows from the result set
orders_quantity_data = cursor.fetchall()

# Define the filename for the 'orders_quantity' CSV file
orders_quantity_filename = 'orders_quantity.csv'

# Write the 'orders_quantity' data to a CSV file
with open(orders_quantity_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])  # Write column headers
    writer.writerows(orders_quantity_data)

# Close the cursor and connection
cursor.close()
conn.close()
