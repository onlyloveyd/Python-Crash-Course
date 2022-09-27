import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.default_salary = 100000
        self.employee = Employee("Yi", "Dong", self.default_salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.default_salary + 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, self.default_salary + 10000)


if __name__ == "__main__":
    unittest.main()
