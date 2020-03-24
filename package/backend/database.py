import logging
import sqlite3

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
        qry = '''  
            CREATE TABLE IF NOT EXISTS users (
                uid int PRIMARY KEY,
                username varchar(255) NOT NULL,
                password char(128),
                salt char(32),
                firstname varchar(255),
                lastname varchar(255)
            );
        '''
        cls.query(qry)

    @classmethod
    def __getConn__(cls):
        return sqlite3.connect('data.sqlite')
