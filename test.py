import unittest

# import functions from solutions
from solution_1 import read_database_version
from solution_2 import get_warehouse_detail, get_employee_detail
from solution_3 import update_employee_experience
from solution_4 import get_specialist_employee_list


class TestCalcSolution(unittest.TestCase):
    def test_solution_1(self):
        # Add the print statement from your solution 1 to the empty string below
        self.assertEqual(read_database_version, "")

    def test_solution_2(self):
        # Add the print statements from your solution 2 to the empty string below
        self.assertEqual(get_employee_detail(105), "")
        self.assertEqual(get_warehouse_detail(2), "")

    def test_solution_3(self):
        # Add the print statements from your solution 3 to the empty string below
        self.assertEqual(update_employee_experience(101), "")

    def test_solution_4(self):
        # Add the print statements from your solution 4 to the empty string below
        self.assertEqual(get_specialist_employee_list("Driver", 30000), "")
