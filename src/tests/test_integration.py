import unittest
from services.budget_service import budget_service
from services.user_service import user_service, UserExistsError
from repositories.budget_repository import budget_repository
from repositories.user_repository import user_repository
from entities.user import User
from entities.budget import Budget
from utils.password_utils import hash_password


class TestIntegration(unittest.TestCase):
    def setUp(self):
        budget_service.delete_all()
        user_repository.delete_all()
        hashed_password = hash_password('password123')
        self.user_test1 = User('test_user', hashed_password)
        user_repository.create(self.user_test1)
        self.budget_test1 = Budget(
            'test_user', 10, 'Expense', '22.12.2024', 'example1')
        self.budget_test2 = Budget(
            'test_user', 20, 'Income', '23.12.2024', 'example2')

    def tearDown(self):
        budget_service.delete_all()
        user_repository.delete_all()

    def test_create_valid_user_logs_in(self):
        username = "test"
        password = "testpassword"
        new_user = user_service.create_user(username, password)

        self.assertEqual(new_user, user_service.get_current_user())

    def test_user_log_in(self):
        user_service.login('test_user', 'password123')

        self.assertEqual(self.user_test1.username,
                         user_service.get_current_user().username)

    def test_user_log_out(self):
        user_service.login('test_user', 'password123')
        user_service.logout()

        self.assertEqual(None, user_service.get_current_user())

    def test_create_existing_user_raises_error(self):
        username = "test_user"
        password = "password123"

        with self.assertRaises(UserExistsError):
            user_service.create_user(username, password)

    def test_create_and_find_budget(self):
        budget_service.create_budget(self.user_test1,
                                     self.budget_test1.amount,
                                     self.budget_test1.category,
                                     self.budget_test1.date,
                                     self.budget_test1.tag)

        budgets = budget_repository.find_by_username(self.user_test1.username)

        expected_budgets = [self.budget_test1]

        self.assertEqual(budgets, expected_budgets)

    def test_create_multiple_budgets(self):
        budget_service.create_budget(self.user_test1,
                                     self.budget_test1.amount,
                                     self.budget_test1.category,
                                     self.budget_test1.date,
                                     self.budget_test1.tag)
        budget_service.create_budget(self.user_test1,
                                     self.budget_test2.amount,
                                     self.budget_test2.category,
                                     self.budget_test2.date,
                                     self.budget_test2.tag)

        budgets = budget_service.get_user_budgets(self.user_test1)

        expected_budgets = [self.budget_test1, self.budget_test2]

        self.assertEqual(budgets, expected_budgets)

    def test_delete_budget(self):
        created_budget = budget_service.create_budget(self.user_test1,
                                                      self.budget_test1.amount,
                                                      self.budget_test1.category,
                                                      self.budget_test1.date,
                                                      self.budget_test1.tag)

        budget_service.delete_budget_by_id(created_budget.id)

        budgets = budget_service.get_user_budgets(self.user_test1)

        expected_budgets = []

        self.assertEqual(budgets, expected_budgets)
