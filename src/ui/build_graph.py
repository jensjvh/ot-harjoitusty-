import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.date_utils import convert_to_datetime


def generate_budget_graph(budgets, master):
    """
    Generate a graph to visualize expenses and income.

    Parameters
    ----------
    budgets(list[Budgets]): A list of budgets.
    master(ttk.Frame): The master frame.
    """
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

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    return canvas
