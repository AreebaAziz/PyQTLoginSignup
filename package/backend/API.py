from .models.user import UserDbMgr

class API:
    
    def __init__(self):
        self.user = None

    def login(self, username, password):
        # TODO: code for logging in user
        return True 

    def signup(self, username, pass1, pass2):
        if (pass1 == pass2):
            return UserDbMgr.createUser(username, pass1)
        return False 

    def get_username(self):
        # TODO: code for getting signed-in user's username
        return "Areeba"
