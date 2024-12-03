from tkinter import ttk, constants, Toplevel
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

    def _handle_create_budget(self):
        self._open_create_budget_view()

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

    def _add_budget_overview(self):
        """Add a budget overview table using Treeview."""
        self._budget_treeview = ttk.Treeview(
            master=self._budget_frame,
            columns=("Amount", "Category", "Date"),
            show="headings",
        )

        self._budget_treeview.heading("Amount", text="Amount")
        self._budget_treeview.heading("Category", text="Category")
        self._budget_treeview.heading("Date", text="Date")

        self._budget_treeview.column("Amount", width=150, anchor="e")
        self._budget_treeview.column("Category", width=150, anchor="w")
        self._budget_treeview.column("Date", width=150, anchor="w")

        self.refresh_budget_list()

        self._budget_treeview.grid(
            row=1, column=0, columnspan=2, sticky=constants.NSEW, padx=10, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._budget_frame = ttk.Frame(master=self._frame)

        self._add_heading_label()

        self._add_budget_overview()

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        create_budget_button = ttk.Button(
            master=self._frame,
            text="Create Budget",
            command=self._handle_create_budget
        )
        create_budget_button.grid(
            row=2, column=0, padx=5, pady=10, sticky=constants.EW)

        self._frame.grid_columnconfigure(1, weight=1, minsize=1020)

    def _open_create_budget_view(self):
        """Open the view for creating a new budget."""
        create_budget_window = Toplevel(self._root)
        create_budget_window.title("Create Budget")

        amount_label = ttk.Label(create_budget_window, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=5)
        amount_entry = ttk.Entry(create_budget_window)
        amount_entry.grid(row=0, column=1, padx=10, pady=5)

        category_label = ttk.Label(create_budget_window, text="Category:")
        category_label.grid(row=1, column=0, padx=10, pady=5)
        category_entry = ttk.Entry(create_budget_window)
        category_entry.grid(row=1, column=1, padx=10, pady=5)

        date_label = ttk.Label(create_budget_window, text="Date:")
        date_label.grid(row=2, column=0, padx=10, pady=5)
        date_entry = ttk.Entry(create_budget_window)
        date_entry.grid(row=2, column=1, padx=10, pady=5)

        def new_budget():
            amount = amount_entry.get()
            category = category_entry.get()
            date = date_entry.get()

            budget_service.create_budget(amount, category, date)

            self.refresh_budget_list()

            create_budget_window.destroy()

        new_budget_button = ttk.Button(
            create_budget_window, text="Create", command=new_budget)
        new_budget_button.grid(row=3, column=0, columnspan=2, pady=10)

    def refresh_budget_list(self):
        """Update the budget list."""
        for row in self._budget_treeview.get_children():
            self._budget_treeview.delete(row)

        budgets = budget_service.get_user_budgets()

        for budget in budgets:
            self._budget_treeview.insert(
                "", "end", values=(budget.amount, budget.category, budget.date)
            )
