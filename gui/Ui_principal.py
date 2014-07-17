# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaly\Python\tpv\gui\principal.ui'
#
# Created: Sun Jul 13 18:55:36 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName(_fromUtf8("Principal"))
        Principal.resize(800, 600)
        self.centralWidget = QtGui.QWidget(Principal)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 351, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnTpv = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTpv.sizePolicy().hasHeightForWidth())
        self.btnTpv.setSizePolicy(sizePolicy)
        self.btnTpv.setObjectName(_fromUtf8("btnTpv"))
        self.verticalLayout.addWidget(self.btnTpv)
        self.btnArticulo = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnArticulo.sizePolicy().hasHeightForWidth())
        self.btnArticulo.setSizePolicy(sizePolicy)
        self.btnArticulo.setObjectName(_fromUtf8("btnArticulo"))
        self.verticalLayout.addWidget(self.btnArticulo)
        self.btnCaja = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCaja.sizePolicy().hasHeightForWidth())
        self.btnCaja.setSizePolicy(sizePolicy)
        self.btnCaja.setObjectName(_fromUtf8("btnCaja"))
        self.verticalLayout.addWidget(self.btnCaja)
        self.btnConfiguracion = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConfiguracion.sizePolicy().hasHeightForWidth())
        self.btnConfiguracion.setSizePolicy(sizePolicy)
        self.btnConfiguracion.setObjectName(_fromUtf8("btnConfiguracion"))
        self.verticalLayout.addWidget(self.btnConfiguracion)
        self.btnAyuda = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAyuda.sizePolicy().hasHeightForWidth())
        self.btnAyuda.setSizePolicy(sizePolicy)
        self.btnAyuda.setObjectName(_fromUtf8("btnAyuda"))
        self.verticalLayout.addWidget(self.btnAyuda)
        self.btnSalir = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.verticalLayout.addWidget(self.btnSalir)
        Principal.setCentralWidget(self.centralWidget)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(_translate("Principal", "Principal", None))
        self.btnTpv.setText(_translate("Principal", "Tpv", None))
        self.btnArticulo.setText(_translate("Principal", "Articulos", None))
        self.btnCaja.setText(_translate("Principal", "Caja y cierres", None))
        self.btnConfiguracion.setText(_translate("Principal", "Configuración", None))
        self.btnAyuda.setText(_translate("Principal", "Ayuda", None))
        self.btnSalir.setText(_translate("Principal", "Salir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Principal = QtGui.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())

