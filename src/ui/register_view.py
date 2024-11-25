from tkinter import ttk, constants
from services.budget_service import budget_service


class RegisterView:
    """A class representing the register view of the app."""

    def __init__(self, root, handle_show_login_view):
        """
        Class constructor for creating a new register view.
        
        Parameters
        ----------
            root: Tkinter widget.
        """

        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._handle_show_login_view = handle_show_login_view

        self._initialize()

    def pack(self):
        """Display the register view."""
        self._frame.grid(row=0, column=0, sticky=constants.NSEW)

    def destroy(self):
        """"Destroy the register view."""
        self._frame.destroy()

    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        budget_service.create_user(username, password)

    def _add_heading_label(self):
        heading_label = ttk.Label(
            master=self._frame, text="Create account")

        heading_label.grid(padx=5, pady=5, row=0, column=0,
                           columnspan=2, sticky=constants.W)

    def _initialize_username_input(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=(constants.W))
        self._username_entry.grid(
            row=1, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize_password_input(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(
            row=2, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._add_heading_label()
        self._initialize_username_input()
        self._initialize_password_input()

        register_button = ttk.Button(
            master=self._frame,
            text="Create account",
            command=self._register_handler
        )

        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._handle_show_login_view)

        
        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        back_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        