import unittest
import datetime

# import functions from solutions
from solution_1 import read_database_version
from solution_2 import get_warehouse_detail, get_employee_detail
from solution_3 import update_employee_experience
from solution_4 import get_specialist_employee_list

version = read_database_version()


class TestCalcSolution(unittest.TestCase):
    def test_solution_1(self):
        # Expected output
        expected_output = version
        # Actual output
        actual_output = read_database_version()
        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

    # test_solution_2
    def test_get_warehouse_detail(self):
        expected_output = (2, 'Rewe Warehouse', 400)
        actual_output = get_warehouse_detail(2)
        self.assertEqual(expected_output, actual_output)

    def test_update_employee_experience(self):
        expected_output = None
        actual_output = update_employee_experience(101)
        self.assertEqual(expected_output, actual_output)

    def test_solution_3(self):
        # Expected output
        expected_output = None
        # Actual output
        actual_output = update_employee_experience(101)
        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

    def test_solution_4(self):
        # Expected output
        expected_output = None
        # Actual output
        actual_output = get_specialist_employee_list("Driver", 30000)
        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()

# OUTPUT:
# PostgreSQL 15.4 (Ubuntu 15.4-0ubuntu0.23.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 12.3.0-1ubuntu1~23.04) 12.3.0, 64-bit
# Printing Warehouse record
# Warehouse Id: 2
# Warehouse Name: Rewe Warehouse
# Employee Count: 400
# Printing Employee record
# Employee Id: 105
# Employee Name: Linda
# Warehouse Id: 3
# Joining Date: 2004-06-04
# Specialty: Logistics Spcialist
# Salary: 42000
# Experience: None
# Printing Employee record

# Employee ID:  101
# Employee Name:  Mo
# Warehouse ID:  1
# Joining Date:  2005-02-10
# Specility:  HR Manager
# Salary:  40000
# Experience:  18

# Printing employees whose specialty is Driver and salary greater than or equal to 30000

# Employee ID:  102
# Employee Name:  Michael
# Warehouse ID:  1
# Joining Date:  2018-07-23
# Specialty:  Driver
# Salary:  30000
# Experience:  None

# Employee ID:  108
# Employee Name:  Karen
# Warehouse ID:  4
# Joining Date:  2011-10-17
# Specialty:  Driver
# Salary:  30000
# Experience:  None

# New Employee Created
# PostgreSQL 15.4 (Ubuntu 15.4-0ubuntu0.23.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 12.3.0-1ubuntu1~23.04) 12.3.0, 64-bit
# .PostgreSQL 15.4 (Ubuntu 15.4-0ubuntu0.23.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 12.3.0-1ubuntu1~23.04) 12.3.0, 64-bit
# ..
# Printing employees whose specialty is Driver and salary greater than or equal to 30000

# Employee ID:  102
# Employee Name:  Michael
# Warehouse ID:  1
# Joining Date:  2018-07-23
# Specialty:  Driver
# Salary:  30000
# Experience:  None

# Employee ID:  108
# Employee Name:  Karen
# Warehouse ID:  4
# Joining Date:  2011-10-17
# Specialty:  Driver
# Salary:  30000
# Experience:  None
# ..
# ----------------------------------------------------------------------
# Ran 5 tests in 0.110s

# OK
