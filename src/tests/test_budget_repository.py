import unittest
from repositories.budget_repository import budget_repository
from entities.budget import Budget


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()
        self.budget_test1 = Budget('test_user', 10, 'expense', '3.12.2024')

    def tearDown(self):
        budget_repository.delete_all()

    def test_create(self):
        budget_repository.create(self.budget_test1)
        budgets = budget_repository.find_all()

        self.assertEqual(budgets[0].user, 'test_user')

    def test_create_returns_budget(self):
        budget = budget_repository.create(self.budget_test1)

        self.assertEqual(budget, self.budget_test1)

    def test_find_by_username(self):
        budget_repository.create(self.budget_test1)
        budgets = budget_repository.find_by_username('test_user')

        self.assertEqual(budgets[0].user, 'test_user')

    def test_find_by_username_does_not_exist(self):
        budget_repository.create(self.budget_test1)
        budgets = budget_repository.find_by_username('test_user2')

        self.assertEqual(budgets, None)
