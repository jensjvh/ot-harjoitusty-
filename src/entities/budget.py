class Budget:
    """
    A class representing a Budget object of a user.
    """

    def __init__(self, user):
        self._user = user
        self._income = 0
        self._expenses = {}

    def add_income(self, amount):
        self._income += amount
