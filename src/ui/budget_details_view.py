from tkinter import ttk, constants
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.budget_service import budget_service
from services.user_service import user_service
from ui.build_graph import generate_budget_graph


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

        if self._graph_canvas:
            self._graph_canvas.get_tk_widget().destroy()

        self._graph_canvas = generate_budget_graph(budgets, self._frame)
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
