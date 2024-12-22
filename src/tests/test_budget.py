import unittest
from entities.user import User
from entities.budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"
        tag = "allowance"
        self.user_test1 = User('test1', 'test1234')

        self.budget_example = Budget(
            self.user_test1.username, amount, category, date, tag)

    def test_add_income(self):
        self.budget_example.add_income(10)
        expected_amount = 20

        self.assertEqual(self.budget_example.amount, expected_amount)

    def test_repr(self):
        expected_str = "Budget(test1, 10, Income, 01.01.2024, allowance)"

        self.assertEqual(str(self.budget_example), expected_str)

    def test_invalid_comparison_returns_false(self):
        compare_string = "not a budget object"

        comparison_result = (self.budget_example == compare_string)

        self.assertFalse(comparison_result)
