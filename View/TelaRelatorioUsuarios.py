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

class Ui_TelaRelatorioUsuarios(object):
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
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(470, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(150, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.simplesButton = QtWidgets.QPushButton(self.frame_2)
        self.simplesButton.setGeometry(QtCore.QRect(90, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.simplesButton.setFont(font)
        self.simplesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.simplesButton.setObjectName("simplesButton")
        self.simplesButton.clicked.connect(lambda: self.clickedRelatorio(self, 1))
        
        self.robustButton = QtWidgets.QPushButton(self.frame_2)
        self.robustButton.setGeometry(QtCore.QRect(450, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.robustButton.setFont(font)
        self.robustButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robustButton.setObjectName("robustButton")
        self.robustButton.clicked.connect(lambda: self.clickedRelatorio(self, 2))
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(430, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.audioComboBox = QtWidgets.QComboBox(self.frame_2)
        self.audioComboBox.setGeometry(QtCore.QRect(420, 200, 211, 31))
        self.audioComboBox.setObjectName("audioComboBox")
        self.audioComboBox.addItem("", 0)
        self.audioComboBox.addItem("Administrador", 1)
        self.audioComboBox.addItem("Cliente", 2)
        
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(430, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.classifComboBox = QtWidgets.QComboBox(self.frame_2)
        self.classifComboBox.setGeometry(QtCore.QRect(420, 270, 211, 31))
        self.classifComboBox.setObjectName("classifComboBox")
        self.classifComboBox.addItem("", 0)
        self.classifComboBox.addItem("Ativo", 1)
        self.classifComboBox.addItem("Inativo", 2)


        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(330, 60, 20, 391))
        self.line.setStyleSheet("Line{\n"
"    border-right: 1px solid white;\n"
"}\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatórios de Usuários"))
        self.label_2.setText(_translate("MainWindow", "Relatórios"))
        self.label_6.setText(_translate("MainWindow", "Com filtros"))
        self.label_9.setText(_translate("MainWindow", "Geral"))
        self.simplesButton.setText(_translate("MainWindow", "Gerar"))
        self.robustButton.setText(_translate("MainWindow", "Gerar"))
        self.label_3.setText(_translate("MainWindow", "Status"))
        self.audioComboBox.setItemText(1, _translate("MainWindow", "Administrador"))
        self.audioComboBox.setItemText(2, _translate("MainWindow", "Cliente"))
        self.label_4.setText(_translate("MainWindow", "Tipo de usuário"))


    def clickedRelatorio(self, estado, tipo_rel):
        ref_tipo_usuario = self.audioComboBox.itemData(self.audioComboBox.currentIndex())
        fl_ativo = self.classifComboBox.itemData(self.classifComboBox.currentIndex())

        if ref_tipo_usuario != 0 or fl_ativo != 0:   
            GeraRelatorio.gerarUsuariosFiltros(ref_tipo_usuario, fl_ativo)
            filename = 'listagem_usuarios_filtros.pdf'
        else:
            GeraRelatorio.gerarUsuarios()
            filename = 'listagem_usuarios.pdf'
        
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

        self.title = "Relatórios de Usuários"
        self.top    = 150
        self.left   = 300
        self.width  = 550
        self.height = 680
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 