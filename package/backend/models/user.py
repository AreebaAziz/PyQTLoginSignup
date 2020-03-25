import logging
import hashlib, uuid
from package.backend.database import DbMgr, DbIntegrityError

class User:

    username = None
    password = None
    firstname = None
    lastname = None

    def __init__(self, 
        username,
        firstname=None,
        lastname=None
    ):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

class UserDbMgr:

    @staticmethod
    def getUserPwd(username, password):
        q = DbMgr.query("SELECT 1 FROM users WHERE username = areeba")
        q.fetchone()

    @staticmethod
    def createUser(username, password):
        salt = uuid.uuid4().hex
        hashedPwd = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        try:
            DbMgr.query('''
                INSERT INTO users (username, password, salt)
                VALUES (?, ?, ?);
            ''', (username, hashedPwd, salt))
        except DbIntegrityError as e:
            logging.error(e)
            return False 

        return True 
