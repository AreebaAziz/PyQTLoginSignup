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
    def query(cls, qry):
        conn = cls.__getConn__()
        conn.cursor().execute(qry)
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
