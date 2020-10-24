#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:17:43 2020

@author: sofiaarend
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:54:08 2020

@author: sofiaarend
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Venda import Venda
from Model.IngressoVenda import IngressoVenda
from Model.Usuario import Usuario
from Model.Filme import Filme
from View.FrmUsuario import Ui_FrmUsuario
from View.FrmSessao import Ui_FrmSessao
from View.TelaRelatorioVendas import Ui_TelaRelatorioVendas
from Control.RestartApp import restart_program

class Ui_ListVendas(object):
    def setupUi(self, MainWindow, codusu, list_filme, list_usu, list_gen):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/ADMINISTRADOR/administrador_02.jpg) 0 0 0 0 stretch stretch;"
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
        self.genButton.clicked.connect(lambda: self.clickedGeneros(self, MainWindow, list_gen))
        
        self.usuButton = QtWidgets.QPushButton(self.widget_2)
        self.usuButton.setGeometry(QtCore.QRect(0, 240, 311, 51))
        self.usuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usuButton.setObjectName("usuButton")
        self.usuButton.clicked.connect(lambda: self.clickedPerfil(self, MainWindow, list_usu))
        
        self.filmesButton = QtWidgets.QPushButton(self.widget_2)
        self.filmesButton.setGeometry(QtCore.QRect(0, 120, 311, 51))
        self.filmesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmesButton.setObjectName("filmesButton")
        self.filmesButton.clicked.connect(lambda: self.clickedFilmes(self, MainWindow, list_filme))
        
        self.sessaoButton = QtWidgets.QPushButton(self.widget_2)
        self.sessaoButton.setGeometry(QtCore.QRect(0, 180, 311, 51))
        self.sessaoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessaoButton.setObjectName("sessaoButton")
        
        self.sessButton = QtWidgets.QPushButton(self.widget_2)
        self.sessButton.setGeometry(QtCore.QRect(0, 360, 311, 51))
        self.sessButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessButton.setObjectName("sessButton")
        self.sessButton.clicked.connect(lambda: self.clickedSessao(self, MainWindow, codusu))
        
        self.perfil = QtWidgets.QPushButton(self.widget_2)
        self.perfil.setGeometry(QtCore.QRect(15, 590, 80, 70))
        self.perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfil.setObjectName("sessaoButton")
        self.perfil.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-image: url(View/resources/ADMINISTRADOR/BOTAO_LOGIN_ICON.png) 0 0 0 0 stretch stretch;\n"
        "}")
        self.perfil.clicked.connect(lambda: self.clickedUsu(self, MainWindow, codusu))
        
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
        
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 25, 100, 40))
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.buscaField = QtWidgets.QLineEdit(self.widget)
        self.buscaField.setGeometry(QtCore.QRect(150, 30, 300, 30))
        self.buscaField.setFont(font)
        self.buscaField.setObjectName("buscaField")
        self.buscaField.setPlaceholderText("")
        self.buscaField.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        
        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setGeometry(QtCore.QRect(40, 82, 100, 40))
        self.label4.setFont(font)
        self.label4.setObjectName("label")
        
        self.filmeComboBox = QtWidgets.QComboBox(self.widget)
        self.filmeComboBox.setGeometry(QtCore.QRect(150, 80, 300, 40))
        self.filmeComboBox.setFont(font)
        self.filmeComboBox.setObjectName("filmeComboBox")
        self.setFilmes()
        
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(40, 130, 90, 40))
        self.label2.setFont(font)
        self.label2.setObjectName("label1")
        
        self.data1 = QtWidgets.QLineEdit(self.widget)
        self.data1.setGeometry(QtCore.QRect(150, 130, 100, 30))
        self.data1.setFont(font)
        self.data1.setObjectName("data1")
        self.data1.setInputMask("99/99/9999")
        self.data1.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(295, 125, 20, 40))
        self.label3.setFont(font)
        self.label3.setObjectName("label2")
        
        self.data2 = QtWidgets.QLineEdit(self.widget)
        self.data2.setGeometry(QtCore.QRect(350, 130, 100, 30))
        self.data2.setFont(font)
        self.data2.setObjectName("data2")
        self.data2.setInputMask("99/99/9999")
        self.data2.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        
        self.buscaButton = QtWidgets.QPushButton(self.widget)
        self.buscaButton.setGeometry(QtCore.QRect(555, 130, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.buscaButton.setFont(font)
        self.buscaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscaButton.setStyleSheet("QPushButton{\n"
        "    background-color: #ff6859;\n"
        "    border-radius: 15px;" 
        "    border: 1px solid #ff6859;\n"
        "    font-size: 16px;\n"
        "}")
        self.buscaButton.setObjectName("signupButton")
        self.buscaButton.clicked.connect(self.getTodasVendas)
        
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(21, 171, 667, 440))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    border-radius: 0px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.reltorios = QtWidgets.QPushButton(self.centralwidget)
        self.reltorios.setGeometry(QtCore.QRect(355, 615, 135, 30))
        self.reltorios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reltorios.clicked.connect(self.goRelatorios)
        self.reltorios.setObjectName("reltorios")
        self.reltorios.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 15px;"
        "    border-image: none;"
        "}")
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        
        self.getTodasVendas()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador"))
        self.label.setText(_translate("Form", "Nome cliente"))
        self.label4.setText(_translate("Form", "Filme"))
        self.label2.setText(_translate("Form", "Datas   de"))
        self.label3.setText(_translate("Form", "a"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código Venda"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total de Ingressos"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor Total"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data"))
        self.genButton.setText(_translate("MainWindow", "Gêneros"))
        self.usuButton.setText(_translate("MainWindow", "Usuários"))
        self.filmesButton.setText(_translate("MainWindow", "Filmes"))
        self.sessaoButton.setText(_translate("MainWindow", "Vendas"))
        self.buscaButton.setText(_translate("MainWindow", "Buscar"))
        self.sessButton.setText(_translate("MainWindow", "Cadastrar sessão"))
        
    def getTodasVendas(self):
        nome = self.buscaField.text()
        filme = self.filmeComboBox.itemData(self.filmeComboBox.currentIndex())
        data1 = self.data1.text()
        data2 = self.data2.text() 
        vendas = None
        vendas = Venda.getByUsuarioDataFilme(nome, data1, data2, filme)
        
        while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
        
        row = 0
        if vendas != None:
            for venda in vendas:
                total_ing = len(IngressoVenda.getByVenda(venda[0])) 
                usu = Usuario.getById(venda[3])
                
                self.tableWidget.insertRow(row)
                cod     = QTableWidgetItem(str(venda[0]))
                nome    = QTableWidgetItem(usu[0][3])
                total   = QTableWidgetItem(str(total_ing))
                valor   = QTableWidgetItem(str(venda[1]))
                data    = QTableWidgetItem(str(venda[2]))
              
                self.tableWidget.setItem(row, 0, cod)
                self.tableWidget.setItem(row, 1, nome)
                self.tableWidget.setItem(row, 2, total)
                self.tableWidget.setItem(row, 3, valor)
                self.tableWidget.setItem(row, 4, data)
                
                row = row + 1
                self.tableWidget.resizeColumnsToContents()
                
    def clickedItem(self, estado, acao, MainWindow):
        row = self.tableWidget.currentRow()
        codusu = self.tableWidget.item(row,1)
        if acao == "edit":
            self.frmUsuario = QtWidgets.QMainWindow()
            self.ui = Ui_FrmGenero()
            self.ui.setupUi(self.frmUsuario, codusu.text(), MainWindow)
            self.frmUsuario.show()
            MainWindow.close()
        if acao == "novo":
            self.frmUsuario = QtWidgets.QMainWindow()
            self.ui = Ui_FrmGenero()
            self.ui.setupUi(self.frmUsuario, 0, MainWindow)
            self.frmUsuario.show()
            MainWindow.close()
        elif acao == "delete": 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Tem certeza que deseja remover o gênero?")
            msgBox.setWindowTitle("Confirmar ação")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                if Genero.delete(codusu.text()) == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Gênero removido com sucesso.")
                    msg.setWindowTitle("Sucesso")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Erro ao remover gênero.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
            self.getTodosGeneros()
    
    def setFilmes(self):
        filmes = Filme.getAll()
        self.filmeComboBox.addItem('', 0)
        for filme in filmes:
            self.filmeComboBox.addItem(filme[1], filme[0])
    
    def goRelatorios(self, estado):
        self.frmFilme = QtWidgets.QMainWindow()
        self.ui = Ui_TelaRelatorioVendas()
        self.ui.setupUi(self.frmFilme)
        self.frmFilme.show()
        
    def clickedFilmes(self, estado, Form, list_filme):
        list_filme.show()
        Form.close() 

    def clickedPerfil(self, estado, Form, list_usu):
        list_usu.show()
        Form.close() 
        
    def clickedGeneros(self, estado, Form, list_gen):
        list_gen.show()
        Form.close()
        
    def clickedUsu(self, estado, Form, codusu):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codusu, 1, 1)
        self.frmUsu.show() 
        
    def clickedLogout(self, estado):
        restart_program()

    def clickedSessao(self, estado, Form, codcli):
        self.frmSess = QtWidgets.QWidget()
        self.ui = Ui_FrmSessao()
        self.ui.setupUi(self.frmSess, Form)
        self.frmSess.show() 
        Form.close()