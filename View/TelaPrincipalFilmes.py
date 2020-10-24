# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_filmes.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Filme import Filme
from Model.Genero import Genero
from Model.TipoAudio import TipoAudio
from Model.Classificacao import Classificacao
from Model.EstadoFilme import EstadoFilme
from View.TelaSessao import Ui_TelaSessao
from View.FrmUsuario import Ui_FrmUsuario
from Control.RestartApp import restart_program

class Ui_TelaPrincipalFilmes(object):
    def setupUi(self, MainWindow, codcli, Ui_FrmInicio):
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
        "    font-family: \"Lato\";\n"
        "    font-size: 46px;\n"
        "    font-weight: bold;"
        "    color: black;\n"
        "}\n"
        "QLabel{\n"
        "    border-image: none;"
        "    font-family: \"Lato\";\n"
        "    font-size: 46px;\n"
        "    font-weight: bold;"
        "    color: black;\n"
        "}")
        
        filmes = Filme.getAll()
        num_filmes = len(filmes)
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(-15, 140, 991, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
        "    background: transparent;\n"
        "    border-image: none;\n"
        "}"
        "QTableWidget::item{"
        "    padding: 0px 15px;"
        "    font-family: \"Lato\";\n"
        "    border-top: 2px solid transparent;"
        "}\n")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(num_filmes)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(310)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        
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
        self.getTodosFilmes(self, MainWindow, filmes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filmes"))


    def getTodosFilmes(self, estado, MainWindow, filmes):
        while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
        
        num_filmes = len(filmes)
        self.tableWidget.insertRow(0)
        i=0
        while i < num_filmes:
            if filmes[i][6] == 3:
                filmes.remove(filmes[i])
                num_filmes = len(filmes)
                self.tableWidget.setColumnCount(num_filmes)
                
            cod = filmes[i][0]
                
            filme = QtWidgets.QPushButton()
            filme.setFixedHeight(400)
            filme.setObjectName(str(cod))
            filme.setStyleSheet("QPushButton#"+str(cod)+"{"
                                "border-image: url(View/resources/"+str(filmes[i][7])+");"
                                "margin-bottom: 20px;}")
            
            if filmes[i][6] == 2:
                #filme.setText()
                label = QLabel("EM BREVE", filme)
                label.setGeometry(QtCore.QRect(20, 140, 250, 50))
                self._addOpacityEffect(filme, 0.5)
                self._addShadowEffect(label)
            else:
                filme.clicked.connect(lambda: self.clickedFilme(self, MainWindow))
                filme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.tableWidget.setCellWidget(0, i, filme)
            
            i+=1
                
        self.tableWidget.insertRow(1)
        i=0
        while i < num_filmes:        
            nome = QTableWidgetItem(filmes[i][1])
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            nome.setFont(font)
            nome.setTextAlignment(QtCore.Qt.AlignLeft )
            self.tableWidget.setItem(1, i, nome)
            i+=1
        
        self.tableWidget.insertRow(2)
        i=0
        while i < num_filmes:   
            gen = Genero.getDescricaoById(filmes[i][3])
            
            clas = Classificacao.getDescricaoById(filmes[i][5])
            classif = QTableWidgetItem(str(gen[0][0])+"/"+str(clas[0][0]))
            classif.setTextAlignment(QtCore.Qt.AlignLeft )
            
            self.tableWidget.setItem(2, i, classif)
            i+=1
            
        self.tableWidget.insertRow(3)
        i=0
        while i < num_filmes:
            au = TipoAudio.getDescricaoById(filmes[i][4])
            audio = QTableWidgetItem(str(au[0][0]))
            audio.setTextAlignment(QtCore.Qt.AlignLeft )

            self.tableWidget.setItem(3, i, audio)
            i+=1
            
        self.tableWidget.resizeRowsToContents()

    def clickedFilme(self, estado, MainWindow):
        buttonClicked = self.tableWidget.sender()
        postitionOfWidget = buttonClicked.pos()    
        index = self.tableWidget.indexAt(postitionOfWidget)
        
        item = self.tableWidget.cellWidget(0,index.column())
        codfilme = item.objectName()
        
        if codfilme != 0:
            self.frmPrincipal = QtWidgets.QMainWindow()
            self.ui = Ui_TelaSessao()
            self.ui.setupUi(self.frmPrincipal, codfilme, self.usu, MainWindow)
            self.frmPrincipal.show()  
            MainWindow.close()
            
    def clickedUsu(self, estado, Form, codcli):
        self.frmUsu = QtWidgets.QWidget()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsu, codcli, 1, 1)
        self.frmUsu.show() 
            
    def clickedLogout(self, estado):
        restart_program()
        
        
    def _addOpacityEffect(self, item, op):
        effect = QtWidgets.QGraphicsOpacityEffect()
        effect.setOpacity(op)
        item.setGraphicsEffect(effect)
        
    def _addShadowEffect(self, item):
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(0.8)
        effect.setColor(QtGui.QColor("#ff6859"))
        effect.setOffset(2,2)
        item.setGraphicsEffect(effect)
            