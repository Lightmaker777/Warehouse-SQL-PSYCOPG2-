import psycopg2
import datetime


def update_employee_experience(employee_id):
    """Updates the experience of a given employee in years.
    Args:
        employee_id: The ID of the employee whose experience is to be updated.
    """
    conn = psycopg2.connect(
        dbname="dci_db", user="postgres", password="postgres", host="localhost", port=5432)
    cur = conn.cursor()
    # Check if the employee's record exists in the database
    cur.execute(
        "SELECT COUNT(*) FROM employee WHERE employee_id=%s", (employee_id,))
    record_count = cur.fetchone()[0]
    if record_count == 0:
        raise Exception("Employee's record does not exist in the database.")
    # Execute the SQL query to update the employee's experience
    sql = "UPDATE employee SET experience = EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM joining_date) WHERE employee_id=%s"
    cur.execute(sql, (employee_id,))
    # Commit the changes
    conn.commit()
    # Close the cursor and connection objects
    cur.close()
    conn.close()


def get_employee_detail(employee_id):
    """Returns the employee record for a given employee ID.
    Args:
        employee_id: The ID of the employee whose record is to be returned.
    Returns:
        The employee record, or `None` if the employee's record does not exist in the database.
    """
    conn = psycopg2.connect(
        dbname="dci_db", user="postgres", password="postgres", host="localhost", port=5432)
    cur = conn.cursor()
    # Execute the SQL query to get the employee record
    sql = "SELECT * FROM employee WHERE employee_id=%s"
    cur.execute(sql, (employee_id,))
    employee = cur.fetchone()
    # Close the cursor and connection objects
    cur.close()
    conn.close()
    return employee


# Test the code
try:
    update_employee_experience(101)
except Exception as e:
    print(e)
else:
    # Print the employee's record
    employee = get_employee_detail(101)
    if employee is not None:
        print('Printing Employee record')
        print()
        print('Employee ID: ', employee[0])
        print('Employee Name: ', employee[1])
        print('Warehouse ID: ', employee[2])
        print('Joining Date: ', employee[3])
        print('Specility: ', employee[4])
        print('Salary: ', employee[5])
        print('Experience: ', employee[6])
    else:
        print("Employee's record does not exist in the database.")
