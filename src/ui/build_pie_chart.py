import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, constants


def generate_pie_chart(budgets, master):
    """
    Visualize expenses by tags with a Matplotlib pie chart.

    Parameters
    ----------
    budgets(list[Budget]): A list of budgets.
    master(ttk.Frame): The master frame.
    """
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
    total_expense = sum(amounts)

    fig, ax = plt.subplots(figsize=(5, 4))
    wedges, texts, autotexts = ax.pie(
        amounts, labels=tags, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Expenses by Tags')

    plt.tight_layout()

    pie_chart_canvas = FigureCanvasTkAgg(fig, master=master)
    pie_chart_canvas.draw()

    label_frame = ttk.Frame(master=master)
    label_frame.grid(row=2, column=1, padx=5, pady=5, sticky=constants.E)

    for tag, amount, wedge in zip(tags, amounts, wedges):
        percentage = (amount / total_expense) * 100
        label = ttk.Label(
            master=label_frame,
            text=f"{tag}: {percentage:.1f}% ({amount:.2f} €)"
        )
        label.pack(anchor=constants.W)

    return pie_chart_canvas
