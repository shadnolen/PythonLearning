import sqlite3
from sqlite3 import Error

import rook


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"BreadStixTracker.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS user (
                                        id INT PRIMARY KEY,
                                        userName text NOT NULL,
                                        beginDate DATE,
                                        endDate DATE
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tracker (
                                    id INT PRIMARY KEY,
                                    areaGrinded text NOT NULL,
                                    income INT NOT NULL,
                                    priority INT,                                    
                                    dateWorked DATE NOT NULL,
                                    timeStart TIME(0) NOT NULL,
                                    timeEnd TIME(0) NOT NULL,  
                                    expense INT NOT NULL,
                                    gasCost INT NOT NULL,
                                    milesDriven INT NOT NULL,
                                                                      
                                    FOREIGN KEY (dateWorked) REFERENCES user (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    rook.start(token='eaffdcffc205a2a475278a038ef15c86feae68ce0d9fff73630e56837ca78549', labels={"env": "dev"})
    main()
