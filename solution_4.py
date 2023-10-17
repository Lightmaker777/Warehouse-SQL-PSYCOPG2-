import psycopg2


def get_specialist_employee_list(speciality, salary):
    # Fetch employee's details as per speciality and Salary
    conn = psycopg2.connect(
        dbname="dci_db", user="postgres", password="postgres", host="localhost", port=5432)
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee WHERE speciality=%s AND salary>=%s",
                (speciality, salary))
    employees = cur.fetchall()
    cur.close()
    conn.close()
    print()
    print('Printing employees whose specialty is Driver and salary greater than or equal to 30000')
    for employee in employees:
        print()
        print('Employee ID: ', employee[0])
        print('Employee Name: ', employee[1])
        print('Warehouse ID: ', employee[2])
        print('Joining Date: ', employee[3])
        print('Specialty: ', employee[4])
        print('Salary: ', employee[5])
        print('Experience: ', employee[6])


get_specialist_employee_list("Driver", 30000)


def create_employee(empolyeeSqlQuery):
    # Create new employee in database as per the SQL query passed to the function.
    conn = psycopg2.connect(
        dbname="dci_db", user="postgres", password="postgres", host="localhost", port=5432)
    cur = conn.cursor()
    cur.execute(empolyeeSqlQuery)
    conn.commit()
    cur.close()
    conn.close()
    print()
    print('New Employee Created')


create_employee("INSERT INTO employee(Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience) \
    VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
                )
