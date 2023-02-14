"""
Exercise 11-3
TEST FILE
"""
import unittest

from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Unit tests for 'Employee' class in 'employee.py' module."""
    
    def setUp(self):
        """Creates an employee for use in all test methods."""
        self.employee = Employee(
            first_name='Alfred',
            last_name='Pennyworth',
            annual_salary=60_000
        )
    
    def test_give_default_raise(self):
        """Tests the 'give_raise' method for a default ammount of money."""
        old_annual_salary = self.employee.annual_salary
        
        self.employee.give_raise()
        new_annual_salary = self.employee.annual_salary
        
        self.assertEqual(
            first=new_annual_salary,
            second=old_annual_salary + 5000
        )
    
    def test_give_custom_raise(self):
        """Tests the 'give_raise' method for a custom ammount of money."""
        old_annual_salary = self.employee.annual_salary
        
        self.employee.give_raise(10_000)
        new_annual_salary = self.employee.annual_salary
        
        self.assertEqual(
            first=new_annual_salary,
            second=old_annual_salary + 10_000
        )

if __name__ == '__main__':
    unittest.main()
