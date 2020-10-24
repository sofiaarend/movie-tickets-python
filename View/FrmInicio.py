# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from View.FrmUsuario import Ui_FrmUsuario
from Control.UsuarioCtrl import UsuarioCtrl 
from View.TelaAdmin import Ui_TelaAdmin
from View.TelaPrincipalFilmes import Ui_TelaPrincipalFilmes

class Ui_FrmInicio(object):
    
    def setupUi(self, initPage):
        initPage.setObjectName("initPage")
        initPage.resize(991, 691)
        initPage.move(140,0)
        initPage.setBaseSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        initPage.setFont(font)
        initPage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        initPage.setAccessibleName("")
        initPage.setAutoFillBackground(False)
        initPage.setStyleSheet("")
        self.frame = QtWidgets.QFrame(initPage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 691))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
        "    border-image: url(View/resources/LOGIN/LOGIN_FUNDO.jpg) 0 0 0 0 stretch stretch;"
        "}\n"
        "QLineEdit{\n"
        "    border-bottom: 2px; border-style: solid; border-color: black;\n"
        "}\n"
        "QLabel{\n"
        "    border-image: none;\n" 
        "    border: 0px;\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.userField = QtWidgets.QLineEdit(self.frame)
        self.userField.setGeometry(QtCore.QRect(120, 275, 390, 40))
        self.userField.setFont(font)
        self.userField.setObjectName("userField")
        self.userField.setPlaceholderText("Usuário")

        self.passField = QtWidgets.QLineEdit(self.frame)
        self.passField.setGeometry(QtCore.QRect(120, 360, 390, 40))
        self.passField.setFont(font)
        self.passField.setObjectName("passField")
        self.passField.setEchoMode(2)
        self.passField.setPlaceholderText("Senha")
        
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(100, 443, 225, 85))
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "    border-image: url(View/resources/buttonLogin.png) 0 0 0 10;"
        "}")
        self.loginButton.clicked.connect(lambda: self.clickedLogin(self, initPage))
        
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(308, 478, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setUnderline(True)
        self.signupButton.setFont(font)
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setStyleSheet("QPushButton{\n"
        "    background-color: transparent;\n"
        "}")
        self.signupButton.setObjectName("signupButton")
        self.signupButton.clicked.connect(lambda: self.clickedSignup(self, initPage))
        
        self.texto = QtWidgets.QLabel(self.frame)
        self.texto.setGeometry(QtCore.QRect(314, 457, 200, 32))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.texto.setFont(font)
        
        self.infoButton = QtWidgets.QPushButton(self.frame)
        self.infoButton.setGeometry(QtCore.QRect(610, 24, 30, 30))
        self.infoButton.setFont(font)
        self.infoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.infoButton.setStyleSheet("QPushButton{\n"
        "    border-image: url(View/resources/info_icon.png) 0 0 0 0;"
        "}")
        self.infoButton.setObjectName("infoButton")
        self.infoButton.clicked.connect(lambda: self.clickedSignup(self, initPage))

        self.retranslateUi(initPage)
        QtCore.QMetaObject.connectSlotsByName(initPage)

    def retranslateUi(self, initPage):
        _translate = QtCore.QCoreApplication.translate
        initPage.setWindowTitle(_translate("initPage", "Tessera"))
        self.signupButton.setText(_translate("initPage", "CLIQUE AQUI"))
        self.texto.setText(_translate("initPage", "Ainda não é cadastrado?"))
        
    def clickedSignup(self, estado, initPage):
        self.frmUsuario = QtWidgets.QMainWindow()
        self.ui = Ui_FrmUsuario()
        self.ui.setupUi(self.frmUsuario, 0, 2, 1)
        self.frmUsuario.show()   
        
    def clickedLogin(self, estado, initPage):
        usu = UsuarioCtrl.loginUsuario(self, self.userField.text(),self.passField.text())

        if usu:
            tipo_usu = usu[0][7] 
            if tipo_usu == 1:
                self.frmPrincipal = QtWidgets.QMainWindow()
                self.ui = Ui_TelaAdmin()
                codcli = int(usu[0][0])
                self.ui.setupUi(self.frmPrincipal, codcli, initPage)
                self.frmPrincipal.show()  
                initPage.close()
            else:
                self.frmPrincipal = QtWidgets.QMainWindow()
                self.ui = Ui_TelaPrincipalFilmes()
                codcli = int(usu[0][0])
                self.ui.setupUi(self.frmPrincipal, codcli, initPage)
                self.frmPrincipal.show()  
                initPage.close()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)    
    initPage = QtWidgets.QMainWindow()
    ui = Ui_FrmInicio()
    ui.setupUi(initPage) 
    initPage.show()
    sys.exit(app.exec_())

