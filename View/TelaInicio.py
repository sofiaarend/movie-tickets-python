# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaInicio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.tela_principal import Ui_TelaPrincipal

class Ui_MainWindow(object):
    def clickedLogin(self, estado, MainWindow):
        self.frmPrincipal = QtWidgets.QMainWindow()
        self.ui = Ui_TelaPrincipal()
        #codcli = int(usu[0][0])
        self.ui.setupUi(self.frmPrincipal, 0)
        self.frmPrincipal.show()
        MainWindow.hide()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(993, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 991, 691))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
"    background-image: url(:/images/bg2.jpeg)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(300, 160, 391, 471))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: rgba(0, 0, 0, 0.4);\n"
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
"QPushButton{\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.userField = QtWidgets.QLineEdit(self.frame_2)
        self.userField.setGeometry(QtCore.QRect(70, 150, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userField.setFont(font)
        self.userField.setObjectName("userField")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 120, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passField = QtWidgets.QLineEdit(self.frame_2)
        self.passField.setGeometry(QtCore.QRect(70, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passField.setFont(font)
        self.passField.setObjectName("passField")
        self.loginButton = QtWidgets.QPushButton(self.frame_2)
        self.loginButton.setGeometry(QtCore.QRect(100, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(lambda: self.clickedLogin(self, MainWindow))
        self.signupButton = QtWidgets.QPushButton(self.frame_2)
        self.signupButton.setGeometry(QtCore.QRect(140, 380, 113, 32))
        self.signupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupButton.setStyleSheet("QPushButton{\n"
"    background-color: transparent;\n"
"}")
        self.signupButton.setObjectName("signupButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Usuário"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.loginButton.setText(_translate("MainWindow", "Entrar"))
        self.signupButton.setText(_translate("MainWindow", "Cadastre-se"))
        
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

