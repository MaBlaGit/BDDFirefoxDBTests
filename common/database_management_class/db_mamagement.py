"""Browser database manager."""

import sqlite3
import os
from sqlite3 import Error


class BrowserDBManager(object):

    """DB browser manager to run queries against browser db's.
    All queries are stored in common_configs package db_queries module.
    To run queries use select_db_queries function and enter into function
    as a first args:

        select_all - extract all content from selected db
        check_if_empty - check if db is empty
        delete_all - delete al content from db

    As a second argument, pass to the function name of the table."""

    def __init__(self, path_to_dbs_folder, name_of_db):
        self.path_to_db = BrowserDBManager.if_db_exists(
                          BrowserDBManager.find_folder_with_dbs(path_to_dbs_folder) + name_of_db)
        self.conn = BrowserDBManager.create_connection(self.path_to_db)

    @staticmethod
    def find_folder_with_dbs(path_to_db):
        """Build path to dbs folder.
        :param path_to_db - entry path where temporary folder with DB's of Firefox
        is created.
        :return full path with temporary folder containing DB's"""
        for element in os.listdir(path_to_db):
            if element.startswith('rust_mozprofile'):
                return "{0}/{1}/".format(path_to_db, element)

    @staticmethod
    def if_db_exists(path_to_db):
        """Function checks if DB exists.
        :param path_to_db - path to database
        :return database"""
        if os.path.exists(path_to_db):
            return path_to_db
        else:
            raise Exception("No database found!")

    @staticmethod
    def create_connection(db_file):
        """Make connection to the db.
        :param db_file - validated path th selected database
        :return"""
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def list_all_dbs(self, path):
        """List all available DB's.
        :param path - connected database
        """
        db_directory = self.if_db_exists(path)
        dbs_container = os.listdir(db_directory)
        for db in dbs_container:
            if db.endswith('sqlite') or db.endswith('db'):
                print(db)
            else:
                continue

    def tables_available(self):
        """List all tables from selected BD."""
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
            print(cur.fetchall())
        except Error as e:
            print(e)

    def select_query_trigger(self, sql_query):
        """Select from table.
        :param sql_query(str) - selected sql query
        """
        cur = self.conn.cursor()
        cur.execute("{0}".format(sql_query))
        rows = cur.fetchall()
        return rows

    def delete_query_trigger(self, sql_query):
        """Delete from table.
        :param sql_query(str) - selected sql query
        """
        self.conn.cursor()
        self.conn.execute(sql_query)
        self.conn.commit()
