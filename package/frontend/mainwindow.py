# from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from PyQt5.QtCore import Qt
import os
import logging

from PyQt5 import QtWidgets, uic
from package.backend import API

PACKAGE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
UI_PATH = os.path.join(PACKAGE_DIR, "ui")

qt_creator_file = os.path.join(UI_PATH, "mainwindow.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.api = API()

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

    def clicked_btn_signup(self):
        logging.debug("Signup button clicked.")
        username = self.le_signup_username.text()
        pass1 = self.le_signup_pass1.text()
        pass2 = self.le_signup_pass2.text()
        logging.debug("Username: {}, Pass1: {}, Pass2: {}".format(username, pass1, pass2))
