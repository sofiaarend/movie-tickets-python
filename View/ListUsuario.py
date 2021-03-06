# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Usuario import Usuario
from Control.UsuarioCtrl import UsuarioCtrl
from View.FrmUsuario import Ui_FrmUsuario
from View.TelaRelatorioUsuarios import Ui_TelaRelatorioUsuarios
from View.FrmSessao import Ui_FrmSessao
from Control.RestartApp import restart_program

class Ui_ListUsuario(object):
    def setupUi(self, MainWindow, codusu, list_filme, list_gen, list_venda):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/ADMINISTRADOR/administrador_01.jpg) 0 0 0 0 stretch stretch;"
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
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.hide()
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
        
        self.filmesButton = QtWidgets.QPushButton(self.widget_2)
        self.filmesButton.setGeometry(QtCore.QRect(0, 120, 311, 51))
        self.filmesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmesButton.setObjectName("filmesButton")
        self.filmesButton.clicked.connect(lambda: self.clickedFilmes(self, MainWindow, list_filme))
        
        self.sessaoButton = QtWidgets.QPushButton(self.widget_2)
        self.sessaoButton.setGeometry(QtCore.QRect(0, 180, 311, 51))
        self.sessaoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sessaoButton.setObjectName("sessaoButton")
        self.sessaoButton.clicked.connect(lambda: self.clickedVenda(self, MainWindow, list_venda))
        
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
        
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(21, 21, 667, 540))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    border-radius: 0px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(131)
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
        
        self.editar = QtWidgets.QPushButton(self.centralwidget)
        self.editar.setGeometry(QtCore.QRect(630, 615, 95, 30))
        self.editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editar.clicked.connect(lambda: self.clickedItem(self, "edit"))
        self.editar.setObjectName("editar")
        self.editar.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 15px;"
        "    border-image: none;"
        "}")
        
        self.deletar = QtWidgets.QPushButton(self.centralwidget)
        self.deletar.setGeometry(QtCore.QRect(735, 615, 115, 30))
        self.deletar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deletar.clicked.connect(lambda: self.clickedItem(self, "delete"))
        self.deletar.setObjectName("deletar")
        self.deletar.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 15px;"
        "    border-image: none;"
        "}")
        
        self.novo = QtWidgets.QPushButton(self.centralwidget)
        self.novo.setGeometry(QtCore.QRect(843, 614, 120, 30))
        self.novo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.novo.clicked.connect(lambda: self.clickedItem(self, "novo"))
        self.novo.setObjectName("novo")
        self.novo.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-bottom: none;"
        "    border-radius: 15px;"
        "    border-image: none;\n"
        "}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        
        self.getTodosUsuarios()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Usuário"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "E-mail"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Admin"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ativo"))
        self.genButton.setText(_translate("MainWindow", "Gêneros"))
        self.usuButton.setText(_translate("MainWindow", "Usuários"))
        self.filmesButton.setText(_translate("MainWindow", "Filmes"))
        self.sessaoButton.setText(_translate("MainWindow", "Vendas"))
        self.sessButton.setText(_translate("MainWindow", "Cadastrar sessão"))
        
    def getTodosUsuarios(self):
        usuarios = Usuario.getAll()

        while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
        
        row = 0
        for usuario in usuarios:
            self.tableWidget.insertRow(row)
            cod     = QTableWidgetItem(str(usuario[0]))
            nome    = QTableWidgetItem(usuario[3])
            usu     = QTableWidgetItem(usuario[1])
            cpf     = QTableWidgetItem(usuario[4])
            email   = QTableWidgetItem(usuario[5])
            tel     = QTableWidgetItem(usuario[6])
            if usuario[7] == 1: 
                admin = QTableWidgetItem("Sim")
            else:
                admin = QTableWidgetItem("Não")
            if usuario[8] == 1:
                ativo = QTableWidgetItem("Sim")
            else:
                ativo = QTableWidgetItem("Não")

            icon = QtGui.QIcon('View/resources/select.png')
            escolhido = QTableWidgetItem()
            escolhido.setIcon(icon)
            self.tableWidget.setIconSize(QtCore.QSize(40, 40))

            self.tableWidget.setItem(row, 0, escolhido)            
            self.tableWidget.setItem(row, 1, cod)
            self.tableWidget.setItem(row, 2, nome)
            self.tableWidget.setItem(row, 3, usu)
            self.tableWidget.setItem(row, 4, cpf)
            self.tableWidget.setItem(row, 5, email)
            self.tableWidget.setItem(row, 6, tel)
            self.tableWidget.setItem(row, 7, admin)
            self.tableWidget.setItem(row, 8, ativo)
            
            row = row + 1
            self.tableWidget.resizeColumnsToContents()
            
    def clickedItem(self, estado, acao):
        row = self.tableWidget.currentRow()
        codusu = self.tableWidget.item(row,1)
        if acao == "edit":
            self.frmUsuario = QtWidgets.QMainWindow()
            self.ui = Ui_FrmUsuario()
            self.ui.setupUi(self.frmUsuario, codusu.text(), 1, 0)
            self.frmUsuario.show()
        if acao == "novo":
            self.frmUsuario = QtWidgets.QMainWindow()
            self.ui = Ui_FrmUsuario()
            self.ui.setupUi(self.frmUsuario, 0, 1, 1)
            self.frmUsuario.show()
        elif acao == "delete": 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Tem certeza que deseja desativar o usuário?")
            msgBox.setWindowTitle("Confirmar ação")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                if Usuario.desativarUsuario(self, codusu.text()) == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Usuáro desativado com sucesso.")
                    msg.setWindowTitle("Sucesso")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Erro ao desativar usuário.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
        self.getTodosUsuarios()
        
    def goRelatorios(self, estado):
        self.frmFilme = QtWidgets.QMainWindow()
        self.ui = Ui_TelaRelatorioUsuarios()
        self.ui.setupUi(self.frmFilme)
        self.frmFilme.show()
        
    def clickedFilmes(self, estado, Form, list_filme):
        list_filme.show()
        Form.close() 

    def clickedGeneros(self, estado, Form, list_gen):
        list_gen.show()
        Form.close() 
        
    def clickedVenda(self, estado, Form, list_venda):
        list_venda.show()
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