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
    def verifyLogin(username, password):
        salt = DbMgr.eqFetch1('''
            SELECT salt FROM users WHERE username = ?
        ''', (username, ))
        if salt is None:
            logging.debug("Cannot find user in database.")
            return False 
        salt = salt[0]
        pwd, s = UserDbMgr.__hashPwd__(password, salt)
        res = DbMgr.eqFetch1('''
            SELECT username FROM users WHERE
            username = ? AND
            password = ? AND
            salt = ?;
        ''', (username, pwd, salt))
        if res is not None:
            return User(res[0])

    @staticmethod
    def createUser(username, password):
        hashedPwd, salt = UserDbMgr.__hashPwd__(password)
        try:
            DbMgr.eq('''
                INSERT INTO users (username, password, salt)
                VALUES (?, ?, ?);
            ''', (username, hashedPwd, salt))
        except DbIntegrityError as e:
            logging.error(e)
            return None 
        return User(res[0]) 
    
    @staticmethod
    def __hashPwd__(pwd, salt=None):
        if salt is None:
            salt = uuid.uuid4().hex
        hashedPwd = hashlib.sha512(pwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return hashedPwd, salt
