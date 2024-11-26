import unittest
from services.budget_service import budget_service
from repositories.user_repository import user_repository
from entities.user import User


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test123')

    def tearDown(self):
        user_repository.delete_all()
