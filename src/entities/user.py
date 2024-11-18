class User:
    """A class used to represent a user.

    Attributes
    ----------
    username: str
        The username of the user
    password: str
        The password of the user
    """

    def __init__(self, username, password):
        """
        Parameters
        ----------
        username : str
            The username of the user
        password : str
            The password of the user
        """

        self.username = username
        self.password = password