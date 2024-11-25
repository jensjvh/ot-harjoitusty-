from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """A class used for database operations on users."""

    def __init__(self, connection):
        """Class constructor.

        Parameters
        ----------
        connection: SQLite `Connection` object.
        """
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def find_user(self, username):
        """
        Find user with the given username.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        result = cursor.fetchone()

        if result:
            return User(result["username"], result["password"])
        return None

    def create(self, user):
        """Add a user to the database.

        Parameters
        ----------
        user: `User` object.

        Returns
        -------
        user: The added user as an `User` object.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """
        Delete all users from users table.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
