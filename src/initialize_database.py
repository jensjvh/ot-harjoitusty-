from database_connection import get_database_connection


def drop_tables(connection):
    """
    Drop database tables.

    Parameters
    ----------
    connection: Connection
        SQLite `Connection` object.
    """
    cursor = connection.cursor()

    cursor.execute('''
                   drop table if exists budgets;
                ''')
    cursor.execute('''
                   drop table if exists users;
                ''')

    connection.commit()


def create_tables(connection):
    """
    Create database tables.

    Parameters
    ----------
    connection: Connection
        SQLite `Connection` object.
    """
    cursor = connection.cursor()

    cursor.execute('''
                   create table users (
                   username text primary key,
                   password_hash text
                   );
                ''')

    cursor.execute('''
                   create table budgets (
                   id integer primary key autoincrement,
                   user text,
                   amount real,
                   category text,
                   date text,
                   tag text,
                   foreign key (user) references users (username)
                   );
                ''')

    connection.commit()


def initialize_database():
    """
    Initialize database using functions `drop_tables` and `create_tables`.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
