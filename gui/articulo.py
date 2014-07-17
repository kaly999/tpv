# -*- coding: utf-8 -*-

"""
Module implementing Articulo.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_articulo import Ui_Principal

class Articulo(QMainWindow, Ui_Principal):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
