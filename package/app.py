import sys
import logging

from PyQt5.QtWidgets import QApplication

from .frontend.mainwindow import MainWindow
from .backend.database import DbMgr

def run():
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s - %(module)s.%(funcName)s: %(message)s', 
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    app = QApplication(sys.argv)
    DbMgr.setup()
    window = MainWindow()
    window.show()
    app.exec_()