from tkinter import ttk, constants
from services.budget_service import budget_service


class BudgetMainView:
    """A class representing the main Budget overview view."""

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = budget_service.get_current_user()
        self._frame = None
        self._create_budget = None
        self._budget_main_frame = None
        self._frame = None

        self._initialize()

    def pack(self):
        """Display the main budget view."""
        self._frame.grid(row=0, column=0, sticky=constants.NSEW)

    def destroy(self):
        """Destroy the login view."""
        self._frame.destroy()

    def _logout_handler(self):
        budget_service.logout()
        self._handle_logout()

    def _add_heading_label(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Welcome, {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._budget_frame = ttk.Frame(master=self._frame)

        self._add_heading_label()

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=1020)
