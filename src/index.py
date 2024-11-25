import tkinter as tk
from ui.ui import UI


def main():
    window = tk.Tk()
    window.title("Budgeting App")

    window.geometry("1100x700")
    window.resizable(0, 0)
    
    ui_view = UI(window)
    ui_view.start()
    window.mainloop()


if __name__ == "__main__":
    main()
