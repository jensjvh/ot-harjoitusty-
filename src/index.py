import tkinter as tk
import pathlib
from ui.ui import UI


def main():
    window = tk.Tk()
    window.title("Budgeting App")

    window.geometry("1100x700")
    window.resizable(False, False)  # Prevent resizing
    img = tk.PhotoImage(file=pathlib.Path('src/ui/icons/icon.png'))
    window.iconphoto(False, img)

    # Set the root window to fill the entire space
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
