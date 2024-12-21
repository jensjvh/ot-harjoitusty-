from tkinter import ttk, constants
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.budget_service import budget_service
from services.user_service import user_service
from utils.date_utils import convert_to_datetime


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

        self._add_graph()
        self._add_pie_chart()

    def _add_graph(self):
        """Add a graph to visualize expenses and income."""
        budgets = budget_service.get_user_budgets(
            user_service.get_current_user())

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

        if self._graph_canvas:
            self._graph_canvas.get_tk_widget().destroy()

        self._graph_canvas = FigureCanvasTkAgg(fig, master=self._frame)
        self._graph_canvas.draw()
        self._graph_canvas.get_tk_widget().grid(row=1, column=0, padx=5,
                                          pady=5, sticky=constants.W)

    def _add_pie_chart(self):
        """Add a pie chart to visualize expenses by tags."""
        budgets = budget_service.get_user_budgets(
            user_service.get_current_user())

        tag_dict = {}

        for budget in budgets:
            if budget.category == 'Expense':
                tag = budget.tag
                amount = budget.amount
                if tag in tag_dict:
                    tag_dict[tag] += amount
                else:
                    tag_dict[tag] = amount

        tags = list(tag_dict.keys())
        amounts = list(tag_dict.values())

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.pie(amounts, labels=tags, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Expenses by Tags')

        plt.tight_layout()

        if self._pie_chart_canvas:
            self._pie_chart_canvas.get_tk_widget().destroy()

        self._pie_chart_canvas = FigureCanvasTkAgg(fig, master=self._frame)
        self._pie_chart_canvas.draw()
        self._pie_chart_canvas.get_tk_widget().grid(row=1, column=1, padx=5,
                                          pady=5, sticky=constants.E)
