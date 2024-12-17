import unittest
from services.budget_service import budget_service
from repositories.user_repository import user_repository
from entities.user import User
from entities.budget import Budget


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test1234')
        budget_service._user = self.user_test1

    def tearDown(self):
        user_repository.delete_all()

    def test_create_budget(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"

        expected_budget = Budget(
            self.user_test1.username, amount, category, date)
        created_budget = budget_service.create_budget(
            self.user_test1, amount, category, date)

        self.assertEqual(created_budget, expected_budget)

    def test_get_user_budgets(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"

        expected_budgets = [
            Budget(self.user_test1.username, amount, category, date)]
        result_budgets = budget_service.get_user_budgets(self.user_test1)

        self.assertEqual(result_budgets, expected_budgets)
