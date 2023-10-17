import psycopg2

# Function to read warehouse details


def get_warehouse_detail(warehouse_id):
    # Connect to the database
    conn = psycopg2.connect(dbname='dci_db',
                            user='postgres',
                            password='postgres',
                            host='localhost',
                            port=5432)
    # Create a cursor object
    cur = conn.cursor()
    # Execute the SQL query to read warehouse details
    cur.execute("SELECT * FROM Warehouse WHERE Warehouse_Id = %s",
                (warehouse_id,))
    # Get the results
    warehouse = cur.fetchone()
    # Close the cursor and connection objects
    cur.close()
    conn.close()
    return warehouse

# Function to read employee details


def get_employee_detail(employee_id):
    # Connect to the database
    conn = psycopg2.connect(dbname='dci_db',
                            user='postgres',
                            password='postgres',
                            host='localhost',
                            port=5432)
    # Create a cursor object
    cur = conn.cursor()
    # Execute the SQL query to read employee details
    cur.execute("SELECT * FROM Employee WHERE Employee_Id = %s", (employee_id,))
    # Get the results
    employee = cur.fetchone()
    # Close the cursor and connection objects
    cur.close()
    conn.close()
    return employee


# Print warehouse details
warehouse = get_warehouse_detail(2)
print("Printing Warehouse record")
print(f"Warehouse Id: {warehouse[0]}")
print(f"Warehouse Name: {warehouse[1]}")
print(f"Employee Count: {warehouse[2]}")

# Print employee details
employee = get_employee_detail(105)
print("Printing Employee record")
print(f"Employee Id: {employee[0]}")
print(f"Employee Name: {employee[1]}")
print(f"Warehouse Id: {employee[2]}")
print(f"Joining Date: {employee[3]}")
print(f"Specialty: {employee[4]}")
print(f"Salary: {employee[5]}")
print(f"Experience: {employee[6]}")
