import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

connection = sqlite3.connect(DATABASE_PATH)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
