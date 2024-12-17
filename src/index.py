import tkinter as tk
import pathlib
from ui.ui import UI


def main():
    window = tk.Tk()
    window.title("Budgeting App")

    window.resizable(False, False)
    img = tk.PhotoImage(file=pathlib.Path('src/ui/icons/icon.png'))
    window.iconphoto(False, img)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    ui_view = UI(window)
    ui_view.start()

    def on_closing():
        print("Exiting Budgeting App...")
        window.quit()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()


if __name__ == "__main__":
    main()
