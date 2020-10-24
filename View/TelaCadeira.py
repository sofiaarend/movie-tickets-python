#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:57:18 2020

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
from Model.Cadeira import Cadeira
from Model.Ingresso import Ingresso
from View.TelaIngresso import Ui_TelaIngresso
from View.FrmUsuario import Ui_FrmUsuario
from Control.RestartApp import restart_program
import re


class Ui_TelaCadeira(object):
    def setupUi(self, MainWindow, codsessao, codcli, Form, inicio):
        self.usu = codcli
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/LUGARES_FILME/LUGARES_FILMES_SEM_SELECAO.png) 0 0 0 0 stretch stretch;"
        "}\n"
        "QPushButton{\n"
        "    border-image: none;"
        "    border-radius: 12px;\n"
        "    background-color: white;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 22px;\n"
        "    color: #ff6859;\n"
        "}"
        "QPushButton:checked{" 
        "background-color: #ff6859"
        "}")
        
        self.seguir = QtWidgets.QPushButton(self.centralwidget)
        self.seguir.setGeometry(QtCore.QRect(787, 597, 135, 40))
        self.seguir.clicked.connect(lambda: self.clickedSeguir(self, MainWindow, codsessao, inicio))
        self.seguir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seguir.setStyleSheet("QPushButton{\n"
        "    border-image: none;"
        "    border-radius: 12px;\n"
        "    background-color: transparent;\n"
        "}")

        self.perfil = QtWidgets.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(797, 23, 46, 46))
        self.perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfil.setObjectName("sessaoButton")
        self.perfil.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 23px;"
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
        self.getTodosLugares(self, MainWindow, codsessao)
        self.cadeiras_list = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lugares"))


    def getTodosLugares(self, estado, MainWindow, codsessao):
        sessao = Sessao.getById(codsessao)
        cadeiras = Cadeira.getAllBySala(sessao[0][3])
        
        ref_ocupadas = None
        ref_ocupadas = Ingresso.getCadeirasBySessaoDia(codsessao)
        print(ref_ocupadas)
        pos = 259
        alt = 484
        i = 1
        for cadeira in cadeiras:
            self.lugar = QtWidgets.QPushButton(self.centralwidget)
            self.lugar.setStyleSheet("QPushButton{\n"
            "    background-color: white;\n"
            "}"
            "QPushButton:checked{" 
                "background-color: #ff6859"
            "}")
            self.lugar.setObjectName(cadeira[3])
            self.lugar.setCheckable(True)
            self.lugar.setGeometry(QtCore.QRect(pos, alt, 25, 25))
            if cadeira[0] in ref_ocupadas:
                self.lugar.setChecked(True)
                self.lugar.setStyleSheet("QPushButton{\n"
                "    background-color: #ffa3a3;\n"
                "}")
            else:
                self.lugar.clicked.connect(self.clickedLugar)
            
            if pos == 355:
                pos+= 64
            elif pos == 547:
                pos+= 64
            else:
                pos+= 32  
            i+=1
            if i == 14:
                pos = 259
                i = 1 
                if alt == 453:
                    alt-=52
                else:
                    alt-=31
               
        

    def clickedLugar(self, estado):
        buttonClicked = self.centralwidget.sender()    
        nome = buttonClicked.objectName()
        
        if buttonClicked.isChecked():
            self.cadeiras_list.append(nome)
        else:
            self.cadeiras_list.remove(nome)
                

    def clickedSeguir(self, estado, MainWindow, codsessao, inicio):
        if self.cadeiras_list == []:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Nenhum acento foi selecionado.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.frmPrincipal = QtWidgets.QMainWindow()
            self.ui = Ui_TelaIngresso()
            self.ui.setupUi(self.frmPrincipal, codsessao, self.cadeiras_list, self.usu, MainWindow, inicio)
            self.frmPrincipal.show()  
            MainWindow.close()
     
    def clickedBack(self, estado, MainWindow, Form):
        self.cadeiras_list = []
        MainWindow.close()
        Form.show()
        
    def clickedUsu(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 
            
    def clickedLogout(self, estado):
        restart_program()
        

            