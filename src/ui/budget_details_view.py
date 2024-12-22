from tkinter import ttk, constants
import matplotlib.pyplot as plt
from services.budget_service import budget_service
from services.user_service import user_service
from ui.build_graph import generate_budget_graph
from ui.build_pie_chart import generate_pie_chart


class BudgetDetailsView:
    """A class representing the budget graph, pie chart and other details view."""

    def __init__(self, root, handle_back):
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._graph_canvas = None
        self._pie_chart_canvas = None
        self._initialize()

    def pack(self):
        """Display the budget details view."""
        self._frame.grid(row=0, column=0, sticky=constants.NSEW)

    def destroy(self):
        """Destroy the budget details view."""
        if self._graph_canvas:
            self._graph_canvas.get_tk_widget().destroy()
        if self._pie_chart_canvas:
            self._pie_chart_canvas.get_tk_widget().destroy()
        plt.close('all')
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        back_button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        self._add_summary()
        self._add_graph()
        self._add_pie_chart()

    def _add_summary(self):
        """Add summary statistics for total income, total expenses, and net savings."""
        budgets = budget_service.get_user_budgets(
            user_service.get_current_user())

        total_income = sum(
            budget.amount for budget in budgets if budget.category == 'Income')
        total_expense = sum(
            budget.amount for budget in budgets if budget.category == 'Expense')
        net_savings = total_income - total_expense

        self._total_income_label = ttk.Label(
            master=self._frame, text=f"Total Income: {total_income:.2f} €")
        self._total_income_label.grid(
            row=2, column=0, padx=5, pady=5, sticky=constants.W)

        self._total_expense_label = ttk.Label(
            master=self._frame, text=f"Total Expenses: {total_expense:.2f} €")
        self._total_expense_label.grid(
            row=3, column=0, padx=5, pady=5, sticky=constants.W)

        self._net_savings_label = ttk.Label(
            master=self._frame, text=f"Net Savings: {net_savings:.2f} €")
        self._net_savings_label.grid(
            row=4, column=0, padx=5, pady=5, sticky=constants.W)

    def _add_graph(self):
        """Add a graph to visualize expenses and income."""
        budgets = budget_service.get_user_budgets(
            user_service.get_current_user())

        if self._graph_canvas:
            self._graph_canvas.get_tk_widget().destroy()

        self._graph_canvas = generate_budget_graph(budgets, self._frame)
        self._graph_canvas.get_tk_widget().grid(row=1, column=0, padx=5,
                                                pady=5, sticky=constants.W)

    def _add_pie_chart(self):
        """Add a pie chart to visualize expenses by tags."""
        budgets = budget_service.get_user_budgets(
            user_service.get_current_user())

        if self._pie_chart_canvas:
            self._pie_chart_canvas.get_tk_widget().destroy()

        self._pie_chart_canvas = generate_pie_chart(budgets, self._frame)
        self._pie_chart_canvas.get_tk_widget().grid(row=1, column=1, padx=5,
                                                    pady=5, sticky=constants.NSEW)
