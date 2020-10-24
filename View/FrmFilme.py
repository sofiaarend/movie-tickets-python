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
from Model.Genero import Genero
from Model.TipoAudio import TipoAudio
from Model.Classificacao import Classificacao
from Model.EstadoFilme import EstadoFilme
from Control.FilmeCtrl import FilmeCtrl

class Ui_FrmFilme(object):
    def setupUi(self, Form, codfilme, main, main_b, list_usu, list_gen, list_venda, codcli):
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

        self.nomeField = QtWidgets.QLineEdit(self.frame)
        self.nomeField.setGeometry(QtCore.QRect(120, 158, 390, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nomeField.setFont(font)
        self.nomeField.setObjectName("nomeField")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 183, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 241, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 298, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.duracaoField = QtWidgets.QLineEdit(self.frame)
        self.duracaoField.setGeometry(QtCore.QRect(120, 218, 390, 30))
        self.duracaoField.setInputMask("999")
        self.duracaoField.setFont(font)
        self.duracaoField.setObjectName("duracaoField")
        
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 360, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 650, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(120, 418, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(120, 477, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(328, 578, 200, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signupButton.setFont(font)
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setObjectName("signupButton")
        self.signupButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/buttonSignup.png) 0 0 0 10;"
        "}")
        self.signupButton.clicked.connect(lambda: self.cadastraFilme(self, codfilme, main, Form, list_usu, list_gen, list_venda, codcli))
        
        self.genComboBox = QtWidgets.QComboBox(self.frame)
        self.genComboBox.setGeometry(QtCore.QRect(120, 278, 390, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genComboBox.setFont(font)
        self.genComboBox.setObjectName("genComboBox")
        self.setGeneros()

        self.audioComboBox = QtWidgets.QComboBox(self.frame)
        self.audioComboBox.setGeometry(QtCore.QRect(120, 337, 390, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.audioComboBox.setFont(font)
        self.audioComboBox.setObjectName("audioComboBox")
        self.audioComboBox.addItem("Legendado", 2)
        self.audioComboBox.addItem("Dublado", 1)
        
        self.classifComboBox = QtWidgets.QComboBox(self.frame)
        self.classifComboBox.setGeometry(QtCore.QRect(120, 395, 390, 30))
        self.classifComboBox.setFont(font)
        self.classifComboBox.setObjectName("classifComboBox")
        self.classifComboBox.addItem("Livre", 1)
        self.classifComboBox.addItem("10", 2)
        self.classifComboBox.addItem("12", 3)
        self.classifComboBox.addItem("14", 4)
        self.classifComboBox.addItem("16", 5)
        self.classifComboBox.addItem("18", 6)
        
        self.statusComboBox = QtWidgets.QComboBox(self.frame)
        self.statusComboBox.setGeometry(QtCore.QRect(120, 455, 390, 30))
        self.statusComboBox.setFont(font)
        self.statusComboBox.setObjectName("statusComboBox")
        self.statusComboBox.addItem("Em Cartaz", 1)
        self.statusComboBox.addItem("Em Breve", 2)
        self.statusComboBox.addItem("Encerrado", 3)
        
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(120, 538, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        self.posterField = QtWidgets.QLineEdit(self.frame)
        self.posterField.setGeometry(QtCore.QRect(120, 515, 390, 30))
        self.posterField.setFont(font)
        self.posterField.setObjectName("posterField")
        
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(15, 20, 30, 40))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("signupButton")
        self.backButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/VOLTAR.png) 0 0 0 0 stretch stretch;"
        "}")
        self.backButton.clicked.connect(lambda: self.voltar(self, Form, main_b))
        
        if codfilme != 0:
            self.setDados(self, codfilme)

        self.retranslateUi(Form, codfilme)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, codfilme):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Filme"))
        self.label.setText(_translate("Form", "Nome*"))
        self.label_6.setText(_translate("Form", "Gênero*"))
        self.label_9.setText(_translate("Form", "Classificação indicativa*"))
        self.label_2.setText(_translate("Form", "Duração* (em minutos)"))
        self.label_8.setText(_translate("Form", " Campos marcados com (*) são obrigatórios"))
        self.label_7.setText(_translate("Form", "Áudio*"))
        self.label_10.setText(_translate("Form", "Estado*"))
        self.label_11.setText(_translate("Form", "Pôster*"))

        
    def setGeneros(self):
        generos = Genero.getAll()
        for genero in generos:
            for info in genero:
                if isinstance(info, int):
                    index = info
                else:
                    nomeGen = info
            self.genComboBox.addItem(nomeGen, index)
            
    def setDados(self, estado, codfilme):
        filme = Filme.getById(codfilme)
        print(filme)
        gen = Genero.getById(filme[0][3])
        audio = TipoAudio.getById(self,filme[0][4])
        classif = Classificacao.getById(self,filme[0][5])
        status = EstadoFilme.getById(self,filme[0][6])
        self.nomeField.setText(filme[0][1])
        self.duracaoField.setText(str(filme[0][2]))
        self.genComboBox.setCurrentIndex(self.genComboBox.findText(gen[0][1]))
        self.audioComboBox.setCurrentIndex(self.audioComboBox.findText(audio[0][1]))
        self.classifComboBox.setCurrentIndex(self.classifComboBox.findText(classif[0][1]))
        self.statusComboBox.setCurrentIndex(self.statusComboBox.findText(status[0][1]))
        self.posterField.setText(str(filme[0][7]))
        
    def cadastraFilme(self, estado, codfilme, main, Form, list_usu, list_gen, list_venda, codcli):
        FilmeCtrl.cadastroFilme(self, codfilme, Form, list_usu, list_gen, list_venda, codcli, main)
        
        
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