#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:52:06 2020

@author: sofiaarend
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from View.FrmUsuario import Ui_FrmUsuario
from View.FrmFilme import Ui_FrmFilme

class Ui_FrmPrincipal(object):

	#BTNCLIENTE.CLICK
    def FrmCliente_Click(self):
        self.frmUsuario = QtWidgets.QMainWindow()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsuario, 'inserir', 0)
        self.frmUsuario.show()
        
    
    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.setWindowModality(QtCore.Qt.NonModal)  

        #BTN CLIENTE ###################
        self.btnCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCliente.setGeometry(QtCore.QRect(140, 10, 131, 81))
        self.btnCliente.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnCliente.setObjectName("btnCliente")
        ##  BTNCLIENTE CLICK EVENT  ###
        self.btnCliente.clicked.connect(self.FrmCliente_Click)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())