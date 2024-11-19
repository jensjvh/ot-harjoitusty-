import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test123')

    def test_create(self):
        user_repository.create(self.user_test1)
        users = user_repository.find_all()

        self.assertEqual(users[0].username, self.user_test1.username)

    def test_create_returns_user(self):
        user = user_repository.create(self.user_test1)

        self.assertEqual(user, self.user_test1)

    def test_delete_all_users(self):
        user_repository.create(self.user_test1)
        user_repository.delete_all()
        users = user_repository.find_all()

        self.assertEqual(users, [])