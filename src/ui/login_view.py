from tkinter import ttk, constants


class LoginView:
    """
    A class representing the login view of the app.
    """

    def __init__(self, root):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Display the login view."""
        self._frame.grid(row=0, column=0, sticky=constants.NSEW)

    def destroy(self):
        """"Destroy the login view."""
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

    def _add_heading_label(self):
        heading_label = ttk.Label(
            master=self._frame, text="Login or Create account")

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

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler)

        register_button = ttk.Button(
            master=self._frame,
            text="Create account"
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
