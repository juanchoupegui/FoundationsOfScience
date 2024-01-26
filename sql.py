import sqlite3

from sqlite3 import Error

# create a database
db_filename = r"C:\Users\jotap\PycharmProjects\Introduction\db\sqlite.db"


def create_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# create database connection


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# create sql statement for creating our tables


def sql_table():
    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
        id integer PRIMARY KEY,
        firstname text NOT NULL,
        lastname text NOT NULL);
    """

    sql_create_task_table = """CREATE TABLE IF NOT EXISTS task (
        id integer PRIMARY KEY,
        name text,
        start_date text NOT NULL,
        end_date text NOT NULL,
        priority integer,
        user_id integer NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user (id));
    """
    # create db conn
    conn = create_connection(db_filename)
    # create tables
    if conn is not None:
        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_task_table)
    else:
        print("Error! No db connection")


# create user


def create_user(conn, user):
    sql = """INSERT INTO user(firstname, lastname)
    VALUES(?,?);"""
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()
    return c.lastrowid


# create task
def create_task(conn, task):
    sql = """INSERT INTO task(name, start_date, end_date, priority, user_id)
    VALUES(?,?,?,?,?);"""
    c = conn.cursor()
    c.execute(sql, task)
    conn.commit()
    return c.lastrowid


def insert_content():
    conn = create_connection(db_filename)
    with conn:
        user = ('Mia', 'Meir')
        user_id = create_user(conn, user)

        task_1 = ("learn python", '2023-11-23', '2024-11-23', 1, user_id)
        task_2 = ("learn deutsch", '2023-11-23', '2024-11-23', 3, user_id)
        create_task(conn, task_1)
        create_task(conn, task_2)


# create_database(db_filename)
# sql_table()
# insert_content()
