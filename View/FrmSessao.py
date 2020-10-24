#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:51:07 2020

@author: sofiaarend
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_filme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Filme import Filme
from Model.Sessao import Sessao
from Control.SessaoCtrl import SessaoCtrl

class Ui_FrmSessao(object):
    def setupUi(self, Form, main):
        Form.setObjectName("Form")
        Form.resize(991, 691)
        Form.move(140,0)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 691))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
        "    border-image: url(View/resources/CADASTRO/FUNDO_CADASTRO.png) 0 0 0 0 stretch stretch;\n"
        "}\n"
        "QLineEdit{\n"
        "    border-bottom: 2px; border-style: solid; border-color: black;\n"
        "}\n"
        "QComboBox{\n"
        "    color: black;\n"
        "    border-bottom: 2px; border-style: solid; border-color: black;"
        "}\n"
        "QLabel{\n"
        "    border-image: none;\n" 
        "    border: 0px;\n"
        "    color: #ffb6b7;\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 265, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.filmeComboBox = QtWidgets.QComboBox(self.frame)
        self.filmeComboBox.setGeometry(QtCore.QRect(120, 240, 390, 30))
        self.filmeComboBox.setFont(font)
        self.filmeComboBox.setObjectName("filmeComboBox")
        self.setFilmes(self, Form, main)
        
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(120, 340, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.salaComboBox = QtWidgets.QComboBox(self.frame)
        self.salaComboBox.setGeometry(QtCore.QRect(120, 315, 390, 30))
        self.salaComboBox.setFont(font)
        self.salaComboBox.setObjectName("salaComboBox")
        self.setSalas(self, Form, main)
        
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(120, 415, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        self.inicioField = QtWidgets.QLineEdit(self.frame)
        self.inicioField.setGeometry(QtCore.QRect(120, 390, 390, 30))
        self.inicioField.setFont(font)
        self.inicioField.setObjectName("inicioField")
        
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(328, 500, 200, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signupButton.setFont(font)
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setObjectName("signupButton")
        self.signupButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/buttonSignup.png) 0 0 0 10;"
        "}")
        self.signupButton.clicked.connect(lambda: self.cadastraSessao(self, main, Form))
        
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(15, 20, 30, 40))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("signupButton")
        self.backButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/VOLTAR.png) 0 0 0 0 stretch stretch;"
        "}")
        self.backButton.clicked.connect(lambda: self.voltar(self, Form, main))
        
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 650, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Sessão"))
        self.label_8.setText(_translate("Form", " Campos marcados com (*) são obrigatórios"))
        self.label_7.setText(_translate("Form", "Filme*"))
        self.label_10.setText(_translate("Form", "Sala*"))
        self.label_11.setText(_translate("Form", "Horário de início*"))

        
    def setFilmes(self, estado, Form, main):
        filmes = Filme.getAll()
        for filme in filmes:
            sessoes = Sessao.getSessoesByFilme(filme[0])
            if len(sessoes) < 3 and filme[6] != 3:
                self.filmeComboBox.addItem(filme[1], filme[0])
        if self.filmeComboBox.count() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Todos os filmes disponíveis já atingiram o número máximo de sessões")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        main.show()
        Form.close()

    def setSalas(self, estado, Form, main):
        i=1
        while i < 4:
            sessoes = Sessao.getSessoesAtivasPorSala(i)
            if len(sessoes) < 5:
                self.salaComboBox.addItem("Sala "+str(i), i)
            i+=1
        if self.salaComboBox.count() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Todas as salas atingiram o máximo de sessões possíveis. Retire algum filme de cartaz para colocar novas sessões")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            Form.close()
            main.show()
        
    def cadastraSessao(self, estado, main, Form):
        SessaoCtrl.cadastroSessao(self, main, Form)
        
    def voltar(self, estado, Form, main_b):
        main_b.show()
        Form.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FrmFilme()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())