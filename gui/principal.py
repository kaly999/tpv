# -*- coding: utf-8 -*-

"""
Module implementing Principal.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_principal import Ui_Principal

from lista import Lista
from articulo import Articulo

class Principal(QMainWindow, Ui_Principal):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    
    @pyqtSignature("")
    def on_btnTpv_clicked(self):
        print("Tpv")
    
    @pyqtSignature("")
    def on_btnArticulo_clicked(self):
        articulo = Articulo(self)
        articulo.show()
    
    @pyqtSignature("")
    def on_btnCaja_clicked(self):
        print("Caja")
    
    @pyqtSignature("")
    def on_btnConfiguracion_clicked(self):
        lista = Lista(self)
        lista.show()
    
    @pyqtSignature("")
    def on_btnAyuda_clicked(self):
        print("ayuda")
    
    @pyqtSignature("")
    def on_btnSalir_clicked(self):
        self.close()
