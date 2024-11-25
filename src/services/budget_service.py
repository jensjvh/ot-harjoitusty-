from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class BudgetService:
    """
    A class representing the application logic of the app.
    """

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):
        """
        Create a new user and log in by default.

        Parameters
        ----------
            username (str): String representing the username.
            password (str): String representing the password.
            login (bool): Optional param, log the user in if True.
        """
        existing_user = self._user_repository.find_user(username)

        if existing_user:
            raise UserExistsError(f"User {username} already exists")

        if len(password) < 8:
            raise InvalidCredentialsError("Password should be at least 8 characters long")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        """
        Log the user in.
        """
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            return "Error"

        self._user = user

        return user

    def logout(self):
        """
        Log the user out.
        """
        self._user = None

    def get_current_user(self):
        return self._user


budget_service = BudgetService()
