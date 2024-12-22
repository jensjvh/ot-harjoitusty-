from entities.budget import Budget
from database_connection import get_database_connection


class BudgetRepository:
    """A class used for database operations on budget objects."""

    def __init__(self, connection):
        """
        Class constructor.
        Parameters
        ----------
            connection(Connection): SQLite `Connection` object.
        """
        self._connection = connection

    def create(self, budget):
        """
        Insert the budget object into the database.

        Parameters
        ----------
            budget(Budget): A budget object.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into budgets (user, amount, category, date, tag) values (?, ?, ?, ?, ?)",
            (budget.user, budget.amount, budget.category, budget.date, budget.tag)
        )

        self._connection.commit()

        budget_id = cursor.lastrowid

        return Budget(budget.user,
                      budget.amount,
                      budget.category,
                      budget.date,
                      budget.tag,
                      budget_id)

    def delete_budget_by_id(self, budget_id):
        """
        Delete a budget from the database given its ID.

        Parameters
        ----------
            budget_id(int): The id of the budget.
        """
        cursor = self._connection.cursor()
        cursor.execute('''
            DELETE FROM budgets
            WHERE id = ?
        ''', (budget_id,))
        self._connection.commit()

    def find_all(self):
        """Find all budgets from the database."""
        cursor = self._connection.cursor()

        cursor.execute("select * from budgets")

        rows = cursor.fetchall()

        return [Budget(row["user"], row["amount"], row["category"], row["date"]) for row in rows]

    def find_by_username(self, username):
        """
        Find all budget objects of a user.

        Parameters
        ----------
            username(str): Username string.
        """
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
                           row["date"],
                           row["tag"],
                           row["id"]) for row in rows]
        return None

    def delete_all_by_username(self, username):
        """
        Delete all budgets by username.

        Parameters
        ----------
            username(str): Username string.
        """
        cursor = self._connection.cursor()

        cursor.execute("""
                       delete from budgets
                       where user = ?
                       """,
                       (username,)
                       )

    def delete_all(self):
        """
        Delete all budgets from budgets table.
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from budgets")

        self._connection.commit()


budget_repository = BudgetRepository(get_database_connection())
