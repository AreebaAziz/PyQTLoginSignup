# from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from PyQt5.QtCore import Qt
import os
import logging

from PyQt5 import QtWidgets, uic
from package.backend import API

PACKAGE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
UI_PATH = os.path.join(PACKAGE_DIR, "ui")

welcome_window_ui = os.path.join(UI_PATH, "mainwindow.ui")
dashboard_window_ui = os.path.join(UI_PATH, "dashboard.ui")
welcome_window, QtBaseClass = uic.loadUiType(welcome_window_ui)

welcome_window_widget = None # use this to show the welcome window from the dashboard window

class MainWindow(QtWidgets.QMainWindow, welcome_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        welcome_window.__init__(self)
        self.setupUi(self)

        self.api = API()
        self.register_elements()

    def register_elements(self):
        global welcome_window_widget
        welcome_window_widget = self
        self.btn_login = self.findChild(QtWidgets.QPushButton, 'btn_login')
        self.btn_login.clicked.connect(self.clicked_btn_login)
        self.btn_signup = self.findChild(QtWidgets.QPushButton, 'btn_signup')
        self.btn_signup.clicked.connect(self.clicked_btn_signup)
        self.le_login_username = self.findChild(QtWidgets.QLineEdit, 'le_login_username')
        self.le_login_pass = self.findChild(QtWidgets.QLineEdit, 'le_login_pass')
        self.le_signup_username = self.findChild(QtWidgets.QLineEdit, 'le_signup_username')
        self.le_signup_pass1 = self.findChild(QtWidgets.QLineEdit, 'le_signup_pass1')
        self.le_signup_pass2 = self.findChild(QtWidgets.QLineEdit, 'le_signup_pass2')

    def clicked_btn_login(self):
        logging.debug("Login button clicked.")
        username = self.le_login_username.text()
        password = self.le_login_pass.text()
        logging.debug("Username: {}, Password: {}".format(username, password))
        res = self.api.login(username, password)
        if res: 
            logging.debug("Login successful.")
            self.switch_to_dashboard()
        else: 
            logging.debug("Login failed.")

    def clicked_btn_signup(self):
        logging.debug("Signup button clicked.")
        username = self.le_signup_username.text()
        pass1 = self.le_signup_pass1.text()
        pass2 = self.le_signup_pass2.text()
        logging.debug("Username: {}, Pass1: {}, Pass2: {}".format(username, pass1, pass2))
        res = self.api.signup(username, pass1, pass2)
        if res: 
            logging.debug("Signup successful.")
            self.switch_to_dashboard()
        else: 
            logging.debug("Signup failed.")

    def switch_to_dashboard(self):
        self.hide()
        dashboard = DashboardWindow(self, api=self.api)
        dashboard.show()

class DashboardWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, api=None):
        super(DashboardWindow, self).__init__(parent)
        uic.loadUi(dashboard_window_ui, self)
        self.api = api

        self.register_elements()

    def register_elements(self):
        self.lb_title = self.findChild(QtWidgets.QLabel, 'lb_title')
        self.lb_title.setText("{} [{}]".format(self.lb_title.text(), self.api.get_username()))
        self.ac_logout = self.findChild(QtWidgets.QAction, 'ac_logout')
        self.ac_logout.triggered.connect(self.logout)

    def logout(self):
        self.hide()
        welcome_window_widget.show()
