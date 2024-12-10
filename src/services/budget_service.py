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

    def create_budget(self, user: User, amount: float, category: str, date: str):
        """Create and return a new budget object."""

        budget = Budget(user=user.username,
                        amount=amount,
                        category=category,
                        date=date)

        return self._budget_repository.create(budget)

    def get_user_budgets(self, user):
        """Return a list of all budget objects of a user."""

        if not user:
            return []

        budgets = self._budget_repository.find_by_username(user.username)

        if not budgets:
            return []

        return list(budgets)

budget_service = BudgetService()
