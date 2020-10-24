# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from View.FrmUsuario import Ui_FrmUsuario
from View.ListUsuario import Ui_ListUsuario
from View.ListFilme import Ui_ListFilme
from View.ListGenero import Ui_ListGenero
from View.ListVendas import Ui_ListVendas
from View.FrmSessao import Ui_FrmSessao
from Control.RestartApp import restart_program

class Ui_TelaAdmin(object):
    def opcoesMenu(self, estado, codcli):
        self.frmUsuario = QtWidgets.QMainWindow()
        self.ui1 = Ui_ListUsuario()       
        
        self.frmFilme = QtWidgets.QMainWindow()
        self.ui2 = Ui_ListFilme()
              
        self.frmGenero = QtWidgets.QMainWindow()
        self.ui3 = Ui_ListGenero()
        
        self.frmVendas = QtWidgets.QMainWindow()
        self.ui4 = Ui_ListVendas()
        
        self.ui1.setupUi(self.frmUsuario, codcli, self.frmFilme, self.frmGenero, self.frmVendas)
        self.ui2.setupUi(self.frmFilme, codcli, self.frmUsuario, self.frmGenero, self.frmVendas)
        self.ui3.setupUi(self.frmGenero, codcli, self.frmFilme, self.frmUsuario, self.frmVendas)
        self.ui4.setupUi(self.frmVendas, codcli, self.frmFilme, self.frmUsuario, self.frmGenero)
    
    def setupUi(self, MainWindow, codcli, Ui_FrmInicio):
        self.usu = codcli
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/ADMINISTRADOR/adm_01_fundo.jpg) 0 0 0 0 stretch stretch;"
        "}\n"
        "QPushButton{\n"
        "    border: none;\n"
        "    border-bottom: 1px solid white;\n"
        "    background: transparent;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 22px;\n"
        "    color: white;\n"
        "}")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, -10, 691, 651))
        self.widget.setStyleSheet("QWidget{\n"
        "    border-image: none;\n"
        "}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(-1, -1, 311, 651))
        self.widget_2.setStyleSheet("QWidget{\n"
        "    border-image: none;\n"
        "}")
        self.widget_2.setObjectName("widget_2")
        
        self.genButton = QtWidgets.QPushButton(self.widget_2)
        self.genButton.setGeometry(QtCore.QRect(0, 300, 311, 51))
        self.genButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.genButton.setObjectName("genButton")
        self.genButton.clicked.connect(lambda: self.clickedGeneros(self, MainWindow, codcli))
        
        self.usuButton = QtWidgets.QPushButton(self.widget_2)
        self.usuButton.setGeometry(QtCore.QRect(0, 240, 311, 51))
        self.usuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usuButton.setObjectName("usuButton")
        self.usuButton.clicked.connect(lambda: self.clickedUsuarios(self, MainWindow, codcli))
        
        self.filmesButton = QtWidgets.QPushButton(self.widget_2)
        self.filmesButton.setGeometry(QtCore.QRect(0, 120, 311, 51))
        self.filmesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmesButton.setObjectName("filmesButton")
        self.filmesButton.clicked.connect(lambda: self.clickedFilmes(self, MainWindow, codcli))
        
        self.sessaoButton = QtWidgets.QPushButton(self.widget_2)
        self.sessaoButton.setGeometry(QtCore.QRect(0, 180, 311, 51))
        self.sessaoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessaoButton.setObjectName("sessaoButton")
        self.sessaoButton.clicked.connect(lambda: self.clickedVendas(self, MainWindow, codcli))
        
        self.sessButton = QtWidgets.QPushButton(self.widget_2)
        self.sessButton.setGeometry(QtCore.QRect(0, 360, 311, 51))
        self.sessButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessButton.setObjectName("sessButton")
        self.sessButton.clicked.connect(lambda: self.clickedSessao(self, MainWindow, codcli))
        
        self.perfil = QtWidgets.QPushButton(self.widget_2)
        self.perfil.setGeometry(QtCore.QRect(15, 590, 80, 70))
        self.perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfil.setObjectName("sessaoButton")
        self.perfil.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-image: url(View/resources/ADMINISTRADOR/BOTAO_LOGIN_ICON.png) 0 0 0 0 stretch stretch;\n"
        "}")
        self.perfil.clicked.connect(lambda: self.clickedPerfil(self, MainWindow, codcli))
        
        self.sair = QtWidgets.QPushButton(self.widget_2)
        self.sair.setGeometry(QtCore.QRect(85, 595, 59, 59))
        self.sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sair.setObjectName("sairButton")
        self.sair.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-image: url(View/resources/BOTAO_SAIR.png) 0 0 0 0 stretch stretch;\n"
        "}")
        self.sair.clicked.connect(self.clickedLogout)
        
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
        self.opcoesMenu(self, codcli)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador"))
        self.genButton.setText(_translate("MainWindow", "Gêneros"))
        self.usuButton.setText(_translate("MainWindow", "Usuários"))
        self.filmesButton.setText(_translate("MainWindow", "Filmes"))
        self.sessaoButton.setText(_translate("MainWindow", "Vendas"))
        self.sessButton.setText(_translate("MainWindow", "Cadastrar sessão"))
        
    def clickedUsuarios(self, estado, Form, codcli):
        self.frmUsuario.show()  
        Form.close()
    
    def clickedFilmes(self, estado, Form, codcli):
        self.frmFilme.show() 
        Form.close()

    def clickedGeneros(self, estado, Form, codcli):
        self.frmGenero.show() 
        Form.close()
        
    def clickedVendas(self, estado, Form, codcli):
        self.frmVendas.show() 
        Form.close()
        
    def clickedPerfil(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 
        
    def clickedSessao(self, estado, Form, codcli):
        self.frmSess = QtWidgets.QWidget()
        self.ui = Ui_FrmSessao()
        self.ui.setupUi(self.frmSess, Form)
        self.frmSess.show() 
        Form.close()
        
    def clickedLogout(self, estado):
        restart_program()
              
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_TelaAdmin()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

