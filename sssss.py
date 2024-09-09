import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="red_bus_details"
)

# Creating a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("UPDATE bus_details SET Seats_Available = CAST(TRIM(SUBSTRING_INDEX(Seats_Available, ' ', 1)) AS UNSIGNED);")

# Fetching data
results = cursor.fetchall()


# Closing the connection
cursor.close()
conn.close()



# UPDATE bus_details
# SET SeatsNumber = CAST(TRIM(SUBSTRING_INDEX(Seats, ' ', 1)) AS UNSIGNED);