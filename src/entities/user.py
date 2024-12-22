class User:
    """A class used to represent a user.

    Attributes
    ----------
        username(str): The username of the user.
        password_hash(str): The hashed password of the user.
    """

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
