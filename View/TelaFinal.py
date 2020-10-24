#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:13:59 2020

@author: sofiaarend
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:34:32 2020

@author: sofiaarend
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_filmes.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Sessao import Sessao
from View.FrmUsuario import Ui_FrmUsuario
from Control.RestartApp import restart_program

class Ui_TelaFinal(object):
    def setupUi(self, MainWindow, codcli, inicio):
        self.usu = codcli
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/INICIO_FILMES/INICIO_FILMES_FUNDO_SEM.jpg) 0 0 0 0 stretch stretch;"
        "}\n"
        "QPushButton{\n"
        "    border-image: none;"
        "    border: none;\n"
        "    border-radius: 25px;\n"
        "    background-color: #ffb6b7;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 22px;\n"
        "    color: white;\n"
        "}"
        "QLabel{\n"
        "    border-image: none;\n" 
        "    border: 0px;\n"
        "    color: #ffb6b7;\n"
        "}")
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(390, 220, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setFamily("Lato")
        self.label3.setFont(font)
        self.label3.setObjectName("label2")
            
        self.sessao1 = QtWidgets.QPushButton(self.centralwidget)
        self.sessao1.setObjectName("sessao1")
        self.sessao1.setGeometry(QtCore.QRect(340, 300, 330, 50))
        self.sessao1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessao1.clicked.connect(lambda: self.clickedInicio(self, MainWindow, inicio))
        
        self.sessao2 = QtWidgets.QPushButton(self.centralwidget)
        self.sessao2.setObjectName("sessao1")
        self.sessao2.setGeometry(QtCore.QRect(340, 370, 330, 50))
        self.sessao2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessao2.clicked.connect(self.clickedLogout)
        
        self.perfil = QtWidgets.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(840, 23, 46, 46))
        self.perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfil.setObjectName("sessaoButton")
        self.perfil.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
        "}")
        self.perfil.clicked.connect(lambda: self.clickedUsu(self, MainWindow, codcli))
        
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(907, 23, 46, 46))
        self.logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout.setObjectName("sessaoButton")
        self.logout.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
        "}")
        self.logout.clicked.connect(self.clickedLogout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compra Finalizada"))
        self.label3.setText(_translate("Form", "Retire seus ingressos"))
        self.sessao1.setText(_translate("MainWindow", "Voltar ao início"))
        self.sessao2.setText(_translate("MainWindow", "Encerrar sessão"))

    def clickedInicio(self, estado, MainWindow, inicio):
        MainWindow.close()
        inicio.show()

    def clickedUsu(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 

        
    def clickedLogout(self, estado):
        restart_program()
        

            