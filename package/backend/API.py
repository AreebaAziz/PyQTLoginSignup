from .models.user import UserDbMgr

class API:

    user = None
    
    def login(self, username, password):
        user = UserDbMgr.verifyLogin(username, password)
        if user is not None:
            self.user = user
            return True 
        else:
            return False

    def signup(self, username, pass1, pass2):
        if (pass1 == pass2):
            user = UserDbMgr.createUser(username, pass1)
            if user is not None:
                self.user = user
                return True
        return False 

    def get_username(self):
        return self.user.username

    def logout(self):
        self.user = None
