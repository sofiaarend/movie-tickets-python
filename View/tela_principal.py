# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
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
from View.FrmFilme import Ui_FrmFilme
from View.FrmGenero import Ui_FrmGenero

class Ui_TelaPrincipal(object):
    
    def setupUi(self, Form, codcli):
        Form.setObjectName("Form")
        Form.resize(991, 691)
        Form.move(140,0)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 691))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
"    background-image: url(View/resources/bgPrincipal.jpg)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(140, 140, 701, 481))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: rgba(255, 255, 255, 0.3);\n"
"    border: 1px solid;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 0px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.perfilButton = QtWidgets.QPushButton(self.frame_2)
        self.perfilButton.setGeometry(QtCore.QRect(250, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.perfilButton.setFont(font)
        self.perfilButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.perfilButton.setObjectName("perfilButton")
        self.perfilButton.clicked.connect(lambda: self.clickedPerfil(self, Form, codcli))
        self.filmesButton = QtWidgets.QPushButton(self.frame_2)
        self.filmesButton.setGeometry(QtCore.QRect(250, 260, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.filmesButton.setFont(font)
        self.filmesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmesButton.setObjectName("filmesButton")
        self.filmesButton.clicked.connect(self.clickedFilmes)
        self.generosButton = QtWidgets.QPushButton(self.frame_2)
        self.generosButton.setGeometry(QtCore.QRect(250, 340, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.generosButton.setFont(font)
        self.generosButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generosButton.setObjectName("generosButton")
        self.generosButton.clicked.connect(self.clickedGeneros)
        self.filmesCadButton = QtWidgets.QPushButton(self.frame_2)
        self.filmesCadButton.setGeometry(QtCore.QRect(250, 180, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.filmesCadButton.setFont(font)
        self.filmesCadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmesCadButton.setObjectName("filmesCadButton")
        self.filmesCadButton.clicked.connect(self.clickedFilmesCad)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tessera"))
        self.perfilButton.setText(_translate("Form", "Usuários"))
        self.filmesButton.setText(_translate("Form", "Filmes"))
        self.generosButton.setText(_translate("Form", "Gêneros"))
        self.filmesCadButton.setText(_translate("Form", "Cadastrar Filme"))
        
    def clickedPerfil(self, estado, Form, codcli):
        self.frmUsuario = QtWidgets.QMainWindow()
        self.ui = Ui_ListUsuario()
        self.ui.setupUi(self.frmUsuario, codcli)
        self.frmUsuario.show()  
        Form.hide()
    
    def clickedFilmes(self, estado):
        self.frmFilme = QtWidgets.QMainWindow()
        self.ui = Ui_ListFilme()
        self.ui.setupUi(self.frmFilme)
        self.frmFilme.show() 

    def clickedGeneros(self, estado):
        self.frmGenero = QtWidgets.QMainWindow()
        self.ui = Ui_FrmGenero()
        self.ui.setupUi(self.frmGenero)
        self.frmGenero.show() 
        
    def clickedFilmesCad(self, estado):
        self.frmFilme = QtWidgets.QMainWindow()
        self.ui = Ui_FrmFilme()
        self.ui.setupUi(self.frmFilme, 0)
        self.frmFilme.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_ListUsuario()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

