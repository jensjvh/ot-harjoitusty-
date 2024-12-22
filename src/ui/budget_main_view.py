from datetime import datetime
from tkinter import ttk, constants, Toplevel, StringVar, OptionMenu
from tkcalendar import DateEntry
from services.budget_service import budget_service
from services.user_service import user_service
from utils.date_utils import convert_to_datetime
from ui.budget_details_view import BudgetDetailsView

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates

BUDGET_CATEGORIES = ['Income', 'Expense']


class BudgetMainView:
    """A class representing the main Budget overview view."""

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = user_service.get_current_user()
        self._frame = None
        self._create_budget = None
        self._budget_main_frame = None
        self._frame = None
        self._error_variable = None
        self._error_label = None
        self._income_label = None
        self._canvas = None

        self._initialize()

    def pack(self):
        """Display the main budget view."""
        view_width = 1050
        view_height = 700

        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()

        position_x = (screen_width - view_width) // 2
        position_y = (screen_height - view_height) // 2

        self._root.geometry(
            f"{view_width}x{view_height}+{position_x}+{position_y}")

        self._frame.grid(row=0, column=0, sticky=constants.NSEW)
        self.refresh_budget_list()

    def destroy(self):
        """Destroy the main budget view."""
        if self._canvas:
            self._canvas.get_tk_widget().destroy()
        plt.close('all')
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _handle_create_budget(self):
        self._open_create_budget_view()

    def _handle_delete_budget(self):
        self._delete_budget()

    def _handle_show_details_view(self):
        self.destroy()
        details_view = BudgetDetailsView(
            self._root, self._handle_back_to_main_view)
        details_view.pack()

    def _handle_back_to_main_view(self):
        self.destroy()
        self._initialize()
        self.pack()

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
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

    def _add_budget_overview(self):
        """Add a budget overview table using Treeview."""
        self._budget_treeview = ttk.Treeview(
            master=self._budget_frame,
            columns=("Amount", "Category", "Date", "Tag"),
            show="headings",
        )

        self._budget_treeview.heading("Amount", text="Amount")
        self._budget_treeview.heading("Category", text="Category")
        self._budget_treeview.heading("Date", text="Date")
        self._budget_treeview.heading("Tag", text="Tag")

        self._budget_treeview.column("Amount", width=100, anchor="e")
        self._budget_treeview.column("Category", width=100, anchor="w")
        self._budget_treeview.column("Date", width=100, anchor="w")
        self._budget_treeview.column("Tag", width=100, anchor="w")

        self.refresh_budget_list()

        self._budget_treeview.grid(
            row=1, column=0, columnspan=2, sticky=constants.NSEW, padx=10, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )
        self._error_label.grid(row=0, column=2, padx=10, pady=5)

        self._budget_frame = ttk.Frame(master=self._frame)

        self._add_heading_label()

        self._add_budget_overview()

        self._budget_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.NSEW
        )

        create_budget_button = ttk.Button(
            master=self._frame,
            text="Create Budget",
            command=self._handle_create_budget
        )
        create_budget_button.grid(
            row=2, column=0, padx=5, pady=2, sticky=constants.EW)

        delete_budget_button = ttk.Button(
            master=self._frame,
            text="Delete Selected Budget",
            command=self._handle_delete_budget
        )
        delete_budget_button.grid(
            row=3, column=0, padx=5, pady=2, sticky=constants.EW)

        show_details_button = ttk.Button(
            master=self._frame,
            text="Show details",
            command=self._handle_show_details_view
        )

        show_details_button.grid(
            row=2, column=1, padx=5, pady=2, sticky=constants.EW)

        self._income_label = ttk.Label(
            self._frame, text="Total Income - Total Expenses: 0 €")
        self._income_label.grid(row=4, column=0, padx=5,
                                pady=10, sticky=constants.W)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)

        self._add_graph()

    def _validate_input(self, amount: str, date: str):
        try:
            float_amount = float(amount)
            if float_amount <= 0:
                raise ValueError("Amount must be greater than 0")
            # generoitu koodi alkaa
            if '.' in str(amount) and len(str(amount).split('.')[1]) > 2:
                raise ValueError(
                    "Amount must not have more than two decimal places")
            # generoitu koodi päättyy
        except ValueError:
            raise ValueError("Invalid amount")
        try:
            convert_to_datetime(date)
        except ValueError:
            raise ValueError("Invalid date format")

    def _open_create_budget_view(self):
        """Open the view for creating a new budget."""
        create_budget_window = Toplevel(self._root)
        create_budget_window.title("Create Budget")
        # generoitu koodi alkaa
        create_budget_window.protocol(
            "WM_DELETE_WINDOW", create_budget_window.destroy)
        # generoitu koodi päättyy

        amount_label = ttk.Label(create_budget_window,
                                 text="Amount (eg. 2.5):")
        amount_label.grid(row=0, column=0, padx=10, pady=5)
        amount_entry = ttk.Entry(create_budget_window, width=30)
        amount_entry.grid(row=0, column=1, padx=10, pady=5)

        category_label = ttk.Label(create_budget_window, text="Category:")
        category_label.grid(row=1, column=0, padx=10, pady=5)

        category_variable = StringVar(create_budget_window)
        category_variable.set(BUDGET_CATEGORIES[0])
        category_menu = OptionMenu(
            create_budget_window, category_variable, *BUDGET_CATEGORIES)
        category_menu.grid(row=1, column=1, padx=10, pady=5)

        date_label = ttk.Label(create_budget_window, text="Date (DD.MM.YYYY):")
        date_label.grid(row=2, column=0, padx=10, pady=5)
        date_entry = DateEntry(create_budget_window,
                               width=29, date_pattern='dd.mm.yyyy')
        date_entry.grid(row=2, column=1, padx=10, pady=5)

        tag_label = ttk.Label(create_budget_window, text="Tag:")
        tag_label.grid(row=3, column=0, padx=10, pady=5)
        tag_entry = ttk.Entry(create_budget_window, width=30)
        tag_entry.grid(row=3, column=1, padx=10, pady=5)

        error_label = ttk.Label(create_budget_window,
                                text="", foreground="red")
        error_label.grid(row=4, column=0, columnspan=2,
                         padx=10, pady=5, sticky=constants.SW)

        def new_budget():
            amount = amount_entry.get()
            category = category_variable.get()
            date = date_entry.get()
            tag = tag_entry.get()

            try:
                self._validate_input(amount, date)
            except ValueError as e:
                error_label.config(text=str(e))
                return

            try:
                budget_service.create_budget(
                    self._user, amount, category, date, tag)
            except Exception as e:
                error_label.config(text=str(e))
                return

            self.refresh_budget_list()
            create_budget_window.destroy()

        new_budget_button = ttk.Button(
            create_budget_window, text="Create", command=new_budget)
        new_budget_button.grid(row=4, column=0, columnspan=2, pady=10)

    def _delete_budget(self):
        selected_item = self._budget_treeview.selection()
        if not selected_item:
            self._show_error("No item selected")
            return

        item = self._budget_treeview.item(selected_item)
        budget_id = item['values'][4]

        try:
            budget_service.delete_budget_by_id(budget_id)
            self.refresh_budget_list()
        except Exception as e:
            self._show_error(str(e))

    def refresh_budget_list(self):
        total_income = 0
        total_expense = 0

        for row in self._budget_treeview.get_children():
            self._budget_treeview.delete(row)

        budgets = budget_service.get_user_budgets(self._user)

        for budget in budgets:
            self._budget_treeview.insert(
                "", "end", values=(budget.amount, budget.category, budget.date, budget.tag, budget.id)
            )

            if budget.category == 'Income':
                total_income += float(budget.amount)
            elif budget.category == 'Expense':
                total_expense += float(budget.amount)

        if self._income_label:
            if self._income_label.winfo_exists():
                self._income_label.config(
                    text=f"Total Income - Total Expenses: {total_income - total_expense:.2f} €"
                )

        self._add_graph()

    def _add_graph(self):
        """Add a graph to visualize expenses and income."""
        budgets = budget_service.get_user_budgets(self._user)

        income_dict = {}
        expense_dict = {}

        for budget in budgets:
            date = convert_to_datetime(budget.date)
            amount = budget.amount
            category = budget.category

            if category == 'Income':
                if date in income_dict:
                    income_dict[date] += amount
                else:
                    income_dict[date] = amount
            elif category == 'Expense':
                if date in expense_dict:
                    expense_dict[date] += amount
                else:
                    expense_dict[date] = amount

        income_dates = sorted(income_dict.keys())
        income_amounts = [income_dict[date] for date in income_dates]

        expense_dates = sorted(expense_dict.keys())
        expense_amounts = [expense_dict[date] for date in expense_dates]

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(income_dates, income_amounts,
                label='Income', color='green', marker='o')
        ax.plot(expense_dates, expense_amounts,
                label='Expense', color='red', marker='o')

        # AutoDateLocator used so the app does not crash if points are too far apart
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
        fig.autofmt_xdate()

        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        ax.set_xlabel('Date')
        ax.set_ylabel('Amount')
        ax.set_title('Income and Expenses Over Time')
        ax.legend()

        plt.tight_layout()

        if self._canvas:
            self._canvas.get_tk_widget().destroy()

        self._canvas = FigureCanvasTkAgg(fig, master=self._frame)
        self._canvas.draw()
        self._canvas.get_tk_widget().grid(row=1, column=2, padx=10,
                                          pady=10, sticky=constants.NSEW)
