#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:50:55 2020

@author: sofiaarend
"""

from View.FrmInicio import *
from View.FrmUsuario import *
from View.TelaAdmin import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)    
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmInicio()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())