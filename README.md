# Warehouse Information System (Mini Project)

This exercise will focus on using Psycopg2 to create some CRUD operations for a Postgres database in a Python application.

## Context

The application will be called "Warehouse Information System", and the database is supposed to have two tables `Warehouse` and `Employees`.

There are 3 exercise questions, which simulate real-time queries, and each question contains a specific skill you need to learn. When you complete the exercise, you get more familiar with database operations in Python.

## SQL Queries for Data Prep

You can find the SQL queries (for Postgres) to prepare the required data for our exercise below.

1. Create Database

```SQL
CREATE database dci_db;
```

2. Create Warehouse Table

```SQL
CREATE TABLE Warehouse (
	Warehouse_Id serial NOT NULL PRIMARY KEY,
	Warehouse_Name VARCHAR (100) NOT NULL,
	Employee_Count serial
);

INSERT INTO Warehouse (Warehouse_Id, Warehouse_Name, Employee_Count)
VALUES
('1', 'Amazon Warehouse', 1000),
('2', 'Rewe Warehouse', 400),
('3', 'Tedi Warehouse', 200),
('4', 'Bahn Warehouse', 1500);
```

3. Create Employee Table

```SQL
CREATE TABLE Employee (
	Employee_Id serial NOT NULL PRIMARY KEY,
	Employee_Name VARCHAR (100) NOT NULL,
	Warehouse_Id serial NOT NULL,
	Joining_Date DATE NOT NULL,
	Speciality VARCHAR (100) NOT NULL,
	Salary INTEGER NOT NULL,
	Experience SMALLINT
);

INSERT INTO Employee (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience)
VALUES
('101', 'Mo', '1', '2005-2-10', 'HR Manager', '40000', NULL),
('102', 'Michael', '1', '2018-07-23', 'Driver', '30000', NULL),
('103', 'Lukaku', '2', '2016-05-19', 'Conveyor', '25000', NULL),
('104', 'Robert', '2', '2017-12-28', 'Logistics Spcialist', '28000', NULL),
('105', 'Linda', '3', '2004-06-04', 'Logistics Spcialist', '42000', NULL),
('106', 'Kahn', '3', '2012-09-11', 'Manager', '30000', NULL),
('107', 'Bernice', '4', '2014-08-21', 'Medic', '32000', NULL),
('108', 'Karen', '4', '2011-10-17', 'Driver', '30000', NULL);
```

The tables should look like:

**Warehouse Table**

![Warehouse Table](/assets/warehouse.png)

**Employee Table**
![Employee Table](/assets/employee.png)

## Database Model

Here is the relational model for the database:

![DB Model](/assets/db_model.png)

**My favorite tool for creating neat DB documentation: https://dbdocs.io**

## Tasks

### 1. Connect to your Postgres database server and print its version.

**HINT**

- Write SQL query to get the database server version.
- Connect to the database and use cursor.execute() to execute this query.
- Next, use cursor.fetchone() to fetch the record.

### 2. Get Warehouse and Employee Information using warehouse Id and employee Id

Implement the functionality to read the details of a given employee from the employee table and Warehouse from the warehouse table. i.e., read records from Warehouse and Employee Tables as per given warehouse Id and Employee Id.

```python
def get_warehouse_detail(warehouse_id):
    #Read data from Warehouse table

def get_employee_detail(employee_id):
    # Read data from Employee table

get_warehouse_detail(2)
get_employee_detail(105)

```

**HINT**

- Connect to python_db and use cursor.execute() to execute the parameterized query.
- Next, use cursor.fetchall() to fetch the record.
- Next, iterate record/resultSet to print all column values

**Expected output**

```
Question 2: Read given warehouse and employee details
Printing Warehouse record
Warehouse Id: 2
Warehouse Name: Rewe Warehouse
Employee Count: 400

Printing Employee record
Employee Id: 105
Employee Name: Linda
Warehouse Id: 3
Joining Date: 2004-06-04
Specialty: Logistics Spcialist
Salary: 42000
Experience: None
```

### 3. Update Employee experience in years

The value of the experience column for each employee is null. Implement the functionality to update the experience of a given employee in years.

```python
def update_employee_experience(employee_id):
    # Update Emplyoee Experience in Years

update_employee_experience(101)
```

**HINT**

- The employee table has the joining date for each employee.
- Get a given employee's joining date.
- To get a difference in a year, we can calculate the difference between today’s date and joining-date in years.
- After calculating the difference in a year, you can execute the update table query to update the experience of a given employee.

**Expected output**

**BEFORE**

```
Printing Emplyoee record

Employee Id: 101
Emplyoee Name: Mo
Warehouse Id: 1
Joining Date: 2005-02-10
Specialty: HR Manager
Salary: 40000
Experience: None
```

**AFTER**

```
Printing Emplyoee record

Employee Id: 101
Emplyoee Name: Mo
Warehouse Id: 1
Joining Date: 2005-02-10
Specialty: HR Manager
Salary: 40000
Experience: 15
```

### 4. Get the list Of employees as per specialty and salary

Write a function (as below) to fetch all employees whose salary is higher than or equal to the input amount and specialty is the same as the input specialty.

```python
def get_specialist_employee_list(speciality, salary):
    #Fetch employee's details as per Speciality and Salary

get_specialist_eyployee_list("Driver", 30000)
```

**HINT**

- Define the parameterized select query to fetch data from the table as per the given specialty and salary.
- Next, use the cursor.execute() to execute the query.
- Next, get all records using cursor.fetchall()
- Iterate those records and print each row.

```
Printing employees whose specialty is Driver and salary greater than or equal to 30000
Employee Id:  102
Employee Name: Michael
Warehouse Id: 1
Joining Date: 2018-07-23
Specialty: Driver
Salary: 30000
Experience: None

Employee Id:  108
Employee Name: Karen
Warehouse Id: 4
Joining Date: 2011-10-17
Specialty: Driver
Salary: 30000
Experience: None
```

### 5. Insert a record for a new Employee

Lastly, write a function that adds new employees to your database. A new employee has the following details:

```
('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)
```

This function should look like:

```python
def create_employee(empolyeeSqlQuery):
    #Create new employee in database as per the SQL query passed to the function.

create_employee("INSERT INTO test (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience) \
      VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
)
```

# Test

Please use the ```test.py``` as a base test file for this exercise. You will have to update the ```test.py``` file with your own tests in order to test solutions. 
