from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.budget_main_view import BudgetMainView


class UI:
    """
    Class representing the user interface of the app.
    """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_budget_main_view,
            self._show_register_view
        )
        self._current_view.pack()

    def _show_budget_main_view(self):
        self._hide_current_view()

        self._current_view = BudgetMainView(self._root, self._show_login_view)

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._show_login_view,
            self._show_login_view
        )
        self._current_view.pack()