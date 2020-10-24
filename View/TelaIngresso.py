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
from Model.Filme import Filme
from Model.Ingresso import Ingresso
from Model.Cadeira import Cadeira
from Model.Sessao import Sessao
from Model.Venda import Venda
from Model.IngressoVenda import IngressoVenda
from View.TelaFinal import Ui_TelaFinal
from View.FrmUsuario import Ui_FrmUsuario
from Control.RestartApp import restart_program
from datetime import datetime

class Ui_TelaIngresso(object):
    def setupUi(self, MainWindow, codsessao, lista_lugares, codcli, Form, inicio):
        self.usu = codcli
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(109, 182, 760, 266))
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/LISTA_INGRESSOS/LISTA_C_INGRESSOS_FILMES.png) 0 0 0 0 stretch stretch;"
        "}\n"
        "QPushButton{\n"
        "    border-image: none;"
        "    border-radius: 12px;\n"
        "    background-color: white;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 22px;\n"
        "    color: #ff6859;\n"
        "}")
            
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("QWidget{\n"
        "    border-image: none;\n"
        "    font-family: \"Lato\";\n"
        "    font-size: 18px;\n"
        "}"
        "QTableWidget::item{"
        "    padding: 5px 15px;"
        "}\n")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        
        self.seguir = QtWidgets.QPushButton(self.centralwidget)
        self.seguir.setGeometry(QtCore.QRect(460, 480, 400, 48))
        self.seguir.clicked.connect(lambda: self.clickedComprar(self, MainWindow, lista_lugares, codsessao, inicio))
        self.seguir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seguir.setStyleSheet("QPushButton{\n"
        "    border-image: none;"
        "    border-radius: 12px;\n"
        "    background-color: transparent;\n"
        "}")
        
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(585, 545, 270, 20))
        self.cancelar.clicked.connect(lambda: self.clickedCancelar(self, MainWindow, lista_lugares, codsessao, inicio))
        self.cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelar.setStyleSheet("QPushButton{\n"
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

        self.list_ing = []
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.geraIngresssos(self, codsessao, lista_lugares)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingressos"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Filme"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Horário da sessão"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lugar"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sala"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Valor"))

    def geraIngresssos(self, estado, codsessao, lista_lugares):
        sessao =  Sessao.getById(codsessao)
        filme = Filme.getById(sessao[0][2])
        valor = 12.00
        self.valor_total = 0
        
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
        
        row = 0
        for lugar in lista_lugares:
            ref_lugar = Cadeira.getIdByNomeSala(lugar,sessao[0][3])

            self.tableWidget.insertRow(row)
            nome = QTableWidgetItem(str(filme[0][1]))
            hora = QTableWidgetItem(str(sessao[0][1]))
            cadeira = QTableWidgetItem(str(lugar))
            sala = QTableWidgetItem(str(sessao[0][3]))
            valor_ing = QTableWidgetItem("R$ " + str(valor))
            
            self.tableWidget.setItem(row, 0, nome)
            self.tableWidget.setItem(row, 1, hora)
            self.tableWidget.setItem(row, 2, cadeira)
            self.tableWidget.setItem(row, 3, sala)
            self.tableWidget.setItem(row, 4, valor_ing)
            
            row = row + 1
            self.valor_total += valor
            ing = Ingresso(valor,codsessao,ref_lugar[0])
            ing.save()
            ref_ing = ing.getSelfId()
            self.list_ing.append(ref_ing)
          
        self.tableWidget.insertRow(row)
        total = QTableWidgetItem("Total:")
        v_total = QTableWidgetItem("R$ "+str(self.valor_total))
        
        self.tableWidget.setItem(row, 3, total)
        self.tableWidget.setItem(row, 4, v_total)
        self.tableWidget.resizeColumnsToContents()
        
    def clickedComprar(self, estado, MainWindow, lista_lugares, codsessao, inicio):
        data = datetime.now()
        venda = Venda(self.valor_total, 0.0, data, self.usu)
        result = venda.save()
        
        if result == 1:
            ref_venda = venda.getSelfId()
    
            i = 0
            for lugar in lista_lugares:
                Sessao.updateLugares(codsessao,lugar)
                ing_v = IngressoVenda(self.list_ing[i], ref_venda)
                result = ing_v.save()
                i += 1
            
            if result == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Compra efetuada com sucesso.")
                msg.setWindowTitle("Sucesso")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_() 
                
                self.frmPrincipal = QtWidgets.QMainWindow()
                self.ui = Ui_TelaFinal()
                self.ui.setupUi(self.frmPrincipal, self.usu, inicio)
                self.frmPrincipal.show()  
                MainWindow.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Ocorreu um erro ao efetuar a compra.")
                msg.setWindowTitle("Sucesso")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ocorreu um erro ao efetuar a compra.")
            msg.setWindowTitle("Sucesso")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        
        
    def clickedCancelar(self, estado, MainWindow, lista_lugares, codsessao, inicio):
        for ingresso in self.list_ing:
            Ingresso.delete(ingresso)
        MainWindow.close()
        inicio.show()

        
    def clickedBack(self, estado, MainWindow, Form):
        for ingresso in self.list_ing:
            Ingresso.delete(ingresso)
        MainWindow.close()
        Form.show()
        
    def clickedUsu(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 
            
    def clickedLogout(self, estado):
        for ingresso in self.list_ing:
            Ingresso.delete(ingresso)
        restart_program()
        
        
        