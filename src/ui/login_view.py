from tkinter import ttk, constants, StringVar
from services.user_service import user_service, InvalidCredentialsError

class LoginView:
    """
    A class representing the login view of the app.
    """

    def __init__(self, root, handle_login, handle_show_register_view):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._handle_login = handle_login
        self._handle_show_register_view = handle_show_register_view
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Display the login view."""
        self._frame.grid(row=0, column=0, sticky=constants.NSEW)

    def destroy(self):
        """Destroy the login view."""
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Please enter your username and password")
            return

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError as e:
            self._show_error(e)

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

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )
        self._error_label.grid(row=0, column=1, padx=10, pady=10)

        self._add_heading_label()
        self._initialize_username_input()
        self._initialize_password_input()

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler)

        register_button = ttk.Button(
            master=self._frame,
            text="Create account",
            command=self._handle_show_register_view
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=1020)

        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._hide_error()
