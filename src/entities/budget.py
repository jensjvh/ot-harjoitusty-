class Budget:
    """
    A class representing a Budget object of a user.
    """

    def __init__(self, user, amount, category, date, budget_id=None):
        self._id = budget_id
        self._user = user
        self._amount = amount
        self._category = category
        self._date = date

    @property
    def user(self):
        return self._user

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def date(self):
        return self._date

    def add_income(self, income):
        self._amount += income

    def __repr__(self):
        return f"Budget(id={self._id}, user='{self._user}',amount={self._amount}, category='{self._category}', date='{self._date}')"

    def to_tuple(self):
        """
        Convert class instance to a tuple for easier database insertion.
        """

        return (self._user, self._amount, self._category, self._date)
