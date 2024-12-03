from entities.user import User
from entities.budget import Budget

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.budget_repository import (
    budget_repository as default_budget_repository
)


class UserExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class BudgetService:
    """
    A class representing the application logic of the app.
    """

    def __init__(self,
                 user_repository=default_user_repository,
                 budget_repository=default_budget_repository):
        self._user = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository

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
            raise InvalidCredentialsError(
                "Password should be at least 8 characters long")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def create_budget(self, amount, category, date):
        """Create and return a new budget object."""

        budget = Budget(user=self._user.username,
                        amount=amount,
                        category=category,
                        date=date)

        return self._budget_repository.create(budget)

    def get_user_budgets(self):
        """Return a list of all budget objects of a user."""

        if not self._user:
            return []

        budgets = self._budget_repository.find_by_username(self._user.username)

        if not budgets:
            return []

        return list(budgets)

    def login(self, username, password):
        """
        Log the user in.
        """
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

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
