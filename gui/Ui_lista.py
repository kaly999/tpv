# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaly\Python\tpv\gui\lista.ui'
#
# Created: Sun Jul 13 19:59:11 2014
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
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(30, 20, 611, 551))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        Principal.setCentralWidget(self.centralWidget)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(_translate("Principal", "Principal", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Principal = QtGui.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())

