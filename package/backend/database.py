import logging
import sqlite3
import os

class DbMgr:

    def __init__(self):
        logging.warning("DbMgr should not be instantiated.")

    @classmethod
    def setup(cls):
        cls.__createTables__()

    @classmethod
    def query(cls, qry, params=()):
        conn = cls.__getConn__()
        try:
            conn.cursor().execute(qry, params)
        except sqlite3.IntegrityError as e:
            raise DbIntegrityError(str(e))
        conn.commit()
        conn.close()

    @classmethod
    def __createTables__(cls):
        qry = cls.__getSchema__()
        cls.query(qry)

    @classmethod
    def __getSchema__(cls):
        try:
            f = open(os.path.join("package","backend","schema"), "r")
        except Exception as e:
            logging.error("Cannot open schema file.")
            raise e

        return f.read().replace('\n','')

    @classmethod
    def __getConn__(cls):
        return sqlite3.connect('data.sqlite')

class DbIntegrityError(Exception):
    pass
