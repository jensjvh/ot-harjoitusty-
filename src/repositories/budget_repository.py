from entities.budget import Budget
from database_connection import get_database_connection


class BudgetRepository:
    """A class used for database operations on budget objects."""

    def __init__(self, connection):
        """Class constructor.

        Parameters
        ----------
            connection: SQLite `Connection` object.
        """
        self._connection = connection

    def create(self, budget):
        """Insert the budget object into the database."""
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into budgets (user, amount, category, date) values (?, ?, ?, ?)",
            (budget.user, budget.amount, budget.category, budget.date)
        )

        return budget

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from budgets")

        rows = cursor.fetchall()

        return [Budget(row["user"], row["amount"], row["category"], row["date"]) for row in rows]

    def find_by_username(self, username):
        """Find all budget objects of a user."""
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from budgets where user = ?",
            (username,)
        )

        rows = cursor.fetchall()

        if rows:
            return [Budget(row["user"],
                           row["amount"],
                           row["category"],
                           row["date"]) for row in rows]
        return None

    def delete_all(self):
        """
        Delete all budgets from budgets table.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from budgets")

        self._connection.commit()


budget_repository = BudgetRepository(get_database_connection())
