# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_genero.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Model.Genero import Genero

class Ui_FrmGenero(object):
    def setupUi(self, Form, codgen, MainWindow):
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
        "QCheckBox{\n"
        "    color: #ffb6b7;\n"
        "}\n"
        "QLabel{\n"
        "    border-image: none;\n" 
        "    border: 0px;\n"
        "    color: #ffb6b7;\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label3 = QtWidgets.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(120, 250, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setFamily("Lato")
        self.label3.setFont(font)
        self.label3.setObjectName("label2")

        self.descField = QtWidgets.QLineEdit(self.frame)
        self.descField.setGeometry(QtCore.QRect(120, 308, 390, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.descField.setFont(font)
        self.descField.setObjectName("descField")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 338, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(328, 508, 200, 80))
        self.loginButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/buttonSignup.png) 0 0 0 10;"
        "}")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(lambda: self.cadastroGenero(self, Form, codgen, MainWindow))
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 650, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        if codgen != 0:
            self.setDados(self, codgen)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Gênero"))
        self.label.setText(_translate("Form", "Descrição*"))
        self.label3.setText(_translate("Form", "Gênero"))
        self.loginButton.setText(_translate("Form", ""))
        self.label_8.setText(_translate("Form", " Campos marcados com (*) são obrigatórios"))
        
    def setDados(self, estado, codgen):
        gen = Genero.getById(codgen)
        self.descField.setText(gen[0][1])


    def cadastroGenero(self, estado, Form, codgen, MainWindow):
        descricao = self.descField.text()
        
        if codgen == 0:
            genero = Genero(descricao)
            success = genero.save()
            if success == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Gênero cadastrado com sucesso.")
                msg.setWindowTitle("Sucesso")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                Form.close()
                MainWindow.show()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Erro ao cadastrar gênero.")
                msg.setWindowTitle("Erro")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                
        else:
            success = Genero.update(codgen,descricao)
            if success == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Gênero editado com sucesso.")
                msg.setWindowTitle("Sucesso")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                Form.close()
                MainWindow.show()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Erro ao editar gênero.")
                msg.setWindowTitle("Erro")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FrmGenero()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
