#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:28:17 2020

@author: sofiaarend
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:21:16 2020

@author: sofiaarend
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_relatorios.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Reports.RelatorioPy import GeraRelatorio
from pdf2image import convert_from_path
from PIL.ImageQt import ImageQt
from Model.Filme import Filme
from Model.Usuario import Usuario

class Ui_TelaRelatorioVendas(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 691)
        MainWindow.move(140,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{\n"
        "    border-image: url(View/resources/INICIO_FILMES/INICIO_FILMES_FUNDO_SEM.jpg) 20 0 0 0 stretch stretch;"
        "}\n")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.hide()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 991, 691))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
"    background: white;\n"
"    border-image: url(View/resources/INICIO_FILMES/INICIO_FILMES_FUNDO_SEM.jpg) 0 0 0 0 stretch stretch;"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(140, 180, 701, 481))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: #ffb6b7;\n"
"    border: none;\n"
"    border-image: none;"
"}\n"
"\n"
"QLabel{\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"    border-image: none;"
"    color: white;\n"
"    font-family: \"Lato\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 0px;\n"
"    border-image: none;"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border-image: none;"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-image: none;"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 121, 31))
        
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 25, 100, 40))
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.buscaField = QtWidgets.QComboBox(self.frame_2)
        self.buscaField.setGeometry(QtCore.QRect(200, 30, 300, 30))
        self.buscaField.setFont(font)
        self.buscaField.setObjectName("buscaField")
        self.buscaField.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        self.setUsuarios()
        
        self.label4 = QtWidgets.QLabel(self.frame_2)
        self.label4.setGeometry(QtCore.QRect(90, 82, 100, 40))
        self.label4.setFont(font)
        self.label4.setObjectName("label")
        
        self.filmeComboBox = QtWidgets.QComboBox(self.frame_2)
        self.filmeComboBox.setGeometry(QtCore.QRect(200, 80, 300, 40))
        self.filmeComboBox.setFont(font)
        self.filmeComboBox.setObjectName("filmeComboBox")
        self.setFilmes()
        
        self.label2 = QtWidgets.QLabel(self.frame_2)
        self.label2.setGeometry(QtCore.QRect(90, 130, 90, 40))
        self.label2.setFont(font)
        self.label2.setObjectName("label1")
        
        self.data1 = QtWidgets.QLineEdit(self.frame_2)
        self.data1.setGeometry(QtCore.QRect(200, 130, 100, 30))
        self.data1.setFont(font)
        self.data1.setObjectName("data1")
        self.data1.setInputMask("99/99/9999")
        self.data1.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        
        self.label3 = QtWidgets.QLabel(self.frame_2)
        self.label3.setGeometry(QtCore.QRect(345, 125, 20, 40))
        self.label3.setFont(font)
        self.label3.setObjectName("label2")
        
        self.data2 = QtWidgets.QLineEdit(self.frame_2)
        self.data2.setGeometry(QtCore.QRect(400, 130, 100, 30))
        self.data2.setFont(font)
        self.data2.setObjectName("data2")
        self.data2.setInputMask("99/99/9999")
        self.data2.setStyleSheet("QLineEdit{\n"
        "    background-color: white;\n"
        "    border-bottom: 2px solid black;"
        "}")
        
        self.simplesButton = QtWidgets.QPushButton(self.frame_2)
        self.simplesButton.setGeometry(QtCore.QRect(250, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.simplesButton.setFont(font)
        self.simplesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.simplesButton.setObjectName("simplesButton")
        self.simplesButton.clicked.connect(lambda: self.clickedRelatorio(self, 1))
        
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(430, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatórios de Vendas"))
        self.label.setText(_translate("Form", "Usuário"))
        self.label4.setText(_translate("Form", "Filme"))
        self.label2.setText(_translate("Form", "Datas   de"))
        self.label3.setText(_translate("Form", "a"))
        self.simplesButton.setText(_translate("MainWindow", "Gerar"))
        
    def setFilmes(self):
        filmes = Filme.getAll()
        self.filmeComboBox.addItem('', 0)
        for filme in filmes:
            self.filmeComboBox.addItem(filme[1], filme[0])
    
    def setUsuarios(self):
        usuarios = Usuario.getAll()
        self.buscaField.addItem('', 0)
        for usuario in usuarios:
            self.buscaField.addItem(usuario[1], usuario[0])

    def clickedRelatorio(self, estado, tipo_rel):  
        ref_usuario = self.buscaField.itemData(self.buscaField.currentIndex())
        filme = self.filmeComboBox.itemData(self.filmeComboBox.currentIndex())
        data1 = self.data1.text()
        data2 = self.data2.text()
        
        GeraRelatorio.gerarVendasFiltros(ref_usuario, data1, data2, filme)
        filename = 'listagem_vendas.pdf'

        self.printDialog(filename)
        
      
    def printDialog(self, filename):
        self.winTable = WinTable()
        frame = QtWidgets.QWidget(self.winTable)
        frame.setGeometry(QtCore.QRect(20, 0, 530, 670))
        images = convert_from_path(filename, dpi=300, output_folder="tmp")

        for i, image in enumerate(images):
            qim = ImageQt(image)
            
            pix = QtGui.QPixmap.fromImage(qim)
            label = QtWidgets.QLabel(frame)
            label.setGeometry(QtCore.QRect(0, 0, 500, 670))
            label.setScaledContents(True)
            label.setPixmap(pix)
            
        self.winTable.show()
        
        
class WinTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "Relatórios de Vendas"
        self.top    = 150
        self.left   = 300
        self.width  = 550
        self.height = 680
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 