import unittest
from unittest.mock import Mock, MagicMock
from services.user_service import user_service, UserService, InvalidCredentialsError, UserExistsError
from repositories.user_repository import user_repository
from entities.user import User
from utils.password_utils import hash_password


class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test1234')

    def tearDown(self):
        user_repository.delete_all()

    def test_invalid_register_credentials(self):
        with self.assertRaises(InvalidCredentialsError) as context:
            user_service.create_user('test_invalid', 'short')

        self.assertEqual(str(context.exception),
                         "Password should be at least 8 characters long")

    def test_invalid_login_credentials(self):
        with self.assertRaises(InvalidCredentialsError) as context:
            user_service.login('test_invalid', 'unknownuser')

        self.assertEqual(str(context.exception),
                         "Invalid username or password")

    def test_user_already_exists(self):
        user_service.create_user('new_user', 'password123')
        with self.assertRaises(UserExistsError) as context:
            user_service.create_user('new_user', 'password123')

        self.assertEqual(str(context.exception),
                         "User new_user already exists")

    def test_get_current_user(self):
        user = user_service.create_user('new_user', 'password123', login=True)

        self.assertEqual(user, user_service.get_current_user())

    def test_create_user_logs_in_user(self):
        mock_user_repository = Mock()
        user_service = UserService(user_repository=mock_user_repository)
        username = "new_user"
        password = "password123"
        hashed_password = hash_password(password)
        mock_user_repository.find_user.return_value = None
        mock_user_repository.create.return_value = User(
            username, hashed_password)

        user = user_service.create_user(username, password, login=True)

        self.assertEqual(user, user_service._user)

    def test_create_user_does_not_log_in_user(self):
        mock_user_repository = Mock()
        user_service = UserService(user_repository=mock_user_repository)
        username = "new_user"
        password = "password123"
        hashed_password = hash_password(password)
        mock_user_repository.find_user.return_value = None
        mock_user_repository.create.return_value = User(
            username, hashed_password)

        user = user_service.create_user(username, password, login=False)

        self.assertEqual(user_service._user, None)

    def test_invalid_login_credentials(self):
        mock_user_repository = MagicMock()
        user_service = UserService(user_repository=mock_user_repository)
        mock_user_repository.find_user.return_value = None
        with self.assertRaises(InvalidCredentialsError) as context:
            user_service.login('test_invalid', 'password123')

        self.assertEqual(str(context.exception),
                         "Invalid username or password")

    def test_hash_matches_login(self):
        user_service.create_user('new_user', 'password123')
        mock_password_utils = Mock()
        mock_password_utils.verify_password.return_value = True
        user = user_service.login('new_user', 'password123')

        self.assertEqual(user, user_service._user)

    def test_hash_does_not_match_login(self):
        user_service.create_user('new_user', 'password123')
        mock_password_utils = Mock()
        mock_password_utils.verify_password.return_value = None

        with self.assertRaises(InvalidCredentialsError) as context:
            user = user_service.login('new_user', 'password124')

        self.assertEqual(str(context.exception),
                         "Invalid username or password")

    def test_logout_works(self):
        user_service.create_user('new_user', 'password123', login=True)
        user_service.logout()

        self.assertEqual(user_service._user, None)
