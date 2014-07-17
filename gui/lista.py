# -*- coding: utf-8 -*-

"""
Module implementing Lista.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_lista import Ui_Principal

class Lista(QMainWindow, Ui_Principal):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

