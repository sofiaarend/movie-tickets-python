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
from View.TelaCadeira import Ui_TelaCadeira
from View.FrmUsuario import Ui_FrmUsuario
from Control.RestartApp import restart_program
from datetime import datetime

class Ui_TelaSessao(object):
    def setupUi(self, MainWindow, codfilme, codcli, Form):
        self.usu = codcli
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/SESSAO_FILMES/SESSAO_FILMES_FUNDO.png) 0 0 0 0 stretch stretch;"
        "}\n"
        "QPushButton{\n"
        "    border-image: none;"
        "    border: 2px solid #ff6859;\n"
        "    border-radius: 25px;\n"
        "    background-color: #ffb6b7;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 22px;\n"
        "    color: #ff6859;\n"
        "}")
            
        self.sessao1 = QtWidgets.QPushButton(self.centralwidget)
        self.sessao1.setObjectName("sessao1")
        self.sessao1.setGeometry(QtCore.QRect(340, 250, 330, 50))
        
        self.sessao2 = QtWidgets.QPushButton(self.centralwidget)
        self.sessao2.setObjectName("sessao1")
        self.sessao2.setGeometry(QtCore.QRect(340, 320, 330, 50))
        
        self.sessao3 = QtWidgets.QPushButton(self.centralwidget)
        self.sessao3.setObjectName("sessao1")
        self.sessao3.setGeometry(QtCore.QRect(340, 390, 330, 50))
        
        self.perfil = QtWidgets.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(797, 23, 46, 46))
        self.perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfil.setObjectName("sessaoButton")
        self.perfil.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
        "    border:none;"
        "}")
        self.perfil.clicked.connect(lambda: self.clickedUsu(self, MainWindow, codcli))
        
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(865, 23, 46, 46))
        self.logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout.setObjectName("sessaoButton")
        self.logout.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
        "    border:none;"
        "}")
        self.logout.clicked.connect(self.clickedLogout)
        
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(80, 23, 46, 46))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setObjectName("sessaoButton")
        self.back.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
        "    border:none;"
        "}")
        self.back.clicked.connect(lambda: self.clickedBack(self, MainWindow, Form))

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
        self.getTodasSessoes(self, MainWindow, codfilme, Form)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sessões"))


    def getTodasSessoes(self, estado, MainWindow, codfilme, Form):
        sessoes = Sessao.getSessoesByFilme(codfilme)

        self.sessao1.setText(str(sessoes[0][1])+" - "+str(sessoes[0][4])+"/SALA "+str(sessoes[0][3]))
       # if sessoes[0][1] > datetime.now().time():
        self.sessao1.clicked.connect(lambda: self.clickedSessao(self, MainWindow, sessoes[0][0], Form))
        self.sessao1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        if len(sessoes) > 1:
            self.sessao2.setText(str(sessoes[1][1])+" - "+str(sessoes[1][4])+"/SALA "+str(sessoes[1][3]))
            if sessoes[1][1] > datetime.now().time():
                self.sessao2.clicked.connect(lambda: self.clickedSessao(self, MainWindow, sessoes[1][0], Form))
                self.sessao2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if len(sessoes) > 2:
            self.sessao3.setText(str(sessoes[2][1])+" - "+str(sessoes[2][4])+"/SALA "+str(sessoes[2][3]))
            if sessoes[2][1] > datetime.now().time():
                self.sessao3.clicked.connect(lambda: self.clickedSessao(self, MainWindow, sessoes[2][0], Form))
                self.sessao3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def clickedSessao(self, estado, MainWindow, codsessao, Form):
        self.frmPrincipal = QtWidgets.QMainWindow()
        self.ui = Ui_TelaCadeira()
        self.ui.setupUi(self.frmPrincipal, codsessao, self.usu, MainWindow, Form)
        self.frmPrincipal.show()  
        MainWindow.close()
        
    def clickedBack(self, estado, MainWindow, Form):
        MainWindow.close()
        Form.show()
        
    def clickedUsu(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 
            
    def clickedLogout(self, estado):
        restart_program()
        
        

            