# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Control.UsuarioCtrl import UsuarioCtrl 
from Model.Usuario import Usuario

class Ui_FrmUsuario(object):
    def setupUi(self, Form, codcli, tipo_usu, usu_atual):
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
        font = QtGui.QFont()
        font.setFamily("Lato")
        fontCampo = QtGui.QFont()
        fontCampo.setFamily("Lato")
        fontCampo.setPointSize(18)
        
        self.nomeField = QtWidgets.QLineEdit(self.frame)
        self.nomeField.setGeometry(QtCore.QRect(120, 161, 390, 30)) 
        self.nomeField.setFont(fontCampo)
        self.nomeField.setObjectName("nomeField")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 183, 390, 40))
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 241, 390, 40))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.cpfField = QtWidgets.QLineEdit(self.frame)
        self.cpfField.setGeometry(QtCore.QRect(120, 219, 390, 30))
        self.cpfField.setFont(fontCampo)
        self.cpfField.setObjectName("cpfField")
        self.cpfField.setMaxLength(14)
        self.cpfField.setInputMask("999.999.999-99")
        self.cpfField.setPlaceholderText("00000000000")
        
        self.mailField = QtWidgets.QLineEdit(self.frame)
        self.mailField.setGeometry(QtCore.QRect(120, 276, 390, 30))
        self.mailField.setObjectName("mailField")
        self.mailField.setPlaceholderText("example@mail.com")
        self.mailField.setFont(fontCampo)
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 298, 390, 40))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.telField = QtWidgets.QLineEdit(self.frame)
        self.telField.setGeometry(QtCore.QRect(120, 333, 390, 30))
        self.telField.setObjectName("telField")
        self.telField.setMaxLength(13)
        self.telField.setInputMask("(99)999999999")
        #self.telField.setPlaceholderText("00000000000")
        self.telField.setFont(fontCampo)
        
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 355, 390, 40))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 650, 390, 40))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.userField = QtWidgets.QLineEdit(self.frame)
        self.userField.setGeometry(QtCore.QRect(120, 391, 390, 30))
        self.userField.setFont(fontCampo)
        self.userField.setObjectName("userField")
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 413, 390, 40))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 470, 390, 40))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.passField = QtWidgets.QLineEdit(self.frame)
        self.passField.setGeometry(QtCore.QRect(120, 448, 390, 30))
        self.passField.setFont(fontCampo)
        self.passField.setObjectName("passField")
        self.passField.setEchoMode(2)
        
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 528, 390, 40))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.confirm_passField = QtWidgets.QLineEdit(self.frame)
        self.confirm_passField.setGeometry(QtCore.QRect(120, 506, 390, 30))
        self.confirm_passField.setFont(fontCampo)
        self.confirm_passField.setObjectName("confirm_passField")
        self.confirm_passField.setEchoMode(2)
        
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(328, 578, 200, 80))
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setObjectName("signupButton")
        self.signupButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/buttonSignup.png) 0 0 0 10;"
        "}")
        self.signupButton.clicked.connect(lambda: UsuarioCtrl.cadastroUsuario(self, codcli, tipo_usu, Form))
        
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(15, 20, 30, 40))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("signupButton")
        self.backButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/VOLTAR.png) 0 0 0 0 stretch stretch;"
        "}")
        self.backButton.clicked.connect(lambda: self.voltar(self, Form))
        
        if tipo_usu == 1:
            self.checkBox = QtWidgets.QCheckBox("Administrador", self.frame)
            self.checkBox.setChecked(False)
            self.checkBox.setGeometry(QtCore.QRect(120, 600, 191, 41))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.checkBox.setFont(font)
            
            if usu_atual != 1:
                self.nomeField.setReadOnly(True)
                self.nomeField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.cpfField.setReadOnly(True)
                self.cpfField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.mailField.setReadOnly(True)
                self.mailField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.telField.setReadOnly(True)
                self.telField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.userField.setReadOnly(True)
                self.userField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.passField.setReadOnly(True)
                self.passField.setStyleSheet("QLineEdit{background-color: grey;}")
                self.confirm_passField.setReadOnly(True)
                self.confirm_passField.setStyleSheet("QLineEdit{background-color: grey;}")
                        
        if codcli != 0:
            self.setDados(self, codcli)

        self.retranslateUi(Form, codcli)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, codcli):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Usuário"))
        self.label.setText(_translate("Form", "Nome*"))
        self.label_2.setText(_translate("Form", "CPF"))
        self.label_6.setText(_translate("Form", "E-mail*"))
        self.label_7.setText(_translate("Form", "Telefone"))
        self.label_8.setText(_translate("Form", " Campos marcados com (*) são obrigatórios"))
        self.label_3.setText(_translate("Form", "Nome de usuário*"))
        self.label_4.setText(_translate("Form", "Senha*"))
        self.label_5.setText(_translate("Form", "Confirmar senha*"))
        
    def setDados(self, estado, codcli):
        usu = Usuario.getById(codcli)
        self.nomeField.setText(usu[0][3])
        self.cpfField.setText(usu[0][4])
        self.mailField.setText(usu[0][5])
        self.telField.setText(usu[0][6])
        self.userField.setText(usu[0][1])
        if usu[0][7] == 1:
            self.checkBox.setChecked(True)
            
    def voltar(self, estado, Form):
        Form.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FrmUsuario()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


