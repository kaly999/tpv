# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gui.principal import Principal
 
if __name__ == "__main__":
    # Iniciaar aplicación y crear ventana de inicio
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Principal()
    ui.show()
    sys.exit(app.exec_())   # MainLoop que me mantiene viva a la aplicación
