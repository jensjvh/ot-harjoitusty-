import unittest
from services.budget_service import budget_service
from repositories.user_repository import user_repository
from entities.user import User
from entities.budget import Budget


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        budget_service.delete_all()
        self.user_test1 = User('test1', 'test1234')
        budget_service._user = self.user_test1

    def tearDown(self):
        user_repository.delete_all()
        budget_service.delete_all()

    def test_create_budget(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"
        tag = "allowance"

        expected_budget = Budget(
            self.user_test1.username, amount, category, date, tag)
        created_budget = budget_service.create_budget(
            self.user_test1, amount, category, date, tag)

        self.assertEqual(created_budget, expected_budget)

    def test_delete_budget_by_id(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"
        tag = "allowance"

        created_budget = budget_service.create_budget(
            self.user_test1, amount, category, date, tag)
        
        budget_service.delete_budget_by_id(created_budget.id)
        
        result_budgets = budget_service.get_user_budgets(self.user_test1)
        expected_budgets = []

        self.assertEqual(result_budgets, expected_budgets)

    def test_get_user_budgets(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"
        tag = "allowance"

        budget_service.create_budget(
            self.user_test1, amount, category, date, tag)

        result_budgets = budget_service.get_user_budgets(self.user_test1)
        expected_budgets = [
            Budget(self.user_test1.username, amount, category, date, tag)]

        self.assertEqual(result_budgets, expected_budgets)

    def test_no_user_get_budgets(self):
        user = None

        budgets = budget_service.get_user_budgets(user)

        expected_budgets = []

        self.assertEqual(budgets, expected_budgets)

    def test_delete_all_by_username(self):
        amount = 10
        category = "Income"
        date = "01.01.2024"
        tag = "allowance"

        budget_service.create_budget(
            self.user_test1, amount, category, date, tag)

        budget_service.delete_all_by_username(self.user_test1.username)

        result_budgets = budget_service.get_user_budgets(self.user_test1)

        expected_budgets = []

        self.assertEqual(result_budgets, expected_budgets)