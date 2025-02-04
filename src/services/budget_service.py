from entities.budget import Budget
from entities.user import User

from repositories.budget_repository import (
    budget_repository as default_budget_repository
)


class BudgetService:
    """
    A class representing the application logic of the app.
    """

    def __init__(self, budget_repository=default_budget_repository):
        self._budget_repository = budget_repository

    def create_budget(self, user: User, amount: float, category: str, date: str, tag: str = None):
        """
        Create and return a new budget object.

        Parameters
        ----------
            user(User): User object.
            amount(float): The budget amount in float.
            category(str): Category string.
            date(str): Date in string format.
            tag(str|None): Tag string, defaults to none.
        """

        budget = Budget(user=user.username,
                        amount=amount,
                        category=category,
                        date=date,
                        tag=tag)

        return self._budget_repository.create(budget)

    def delete_budget_by_id(self, budget_id):
        """
        Delete a budget by its ID.

        Parameters
        ----------
            budget_id(int): Integer ID.
        """
        self._budget_repository.delete_budget_by_id(budget_id)

    def get_user_budgets(self, user: User):
        """
        Return a list of all budget objects of a user.

        Parameters
        ----------
            user(User): User object.
        """

        if not user:
            return []

        budgets = self._budget_repository.find_by_username(user.username)

        if not budgets:
            return []

        return list(budgets)

    def delete_all(self):
        """Delete all budgets."""
        self._budget_repository.delete_all()

    def delete_all_by_username(self, username):
        """
        Delete all budgets by username.

        Parameters
        ----------
            username(str): Username string.
        """
        self._budget_repository.delete_all_by_username(username)


budget_service = BudgetService()
