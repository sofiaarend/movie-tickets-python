# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_relatorios.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Model.Genero import Genero
from Reports.RelatorioPy import GeraRelatorio
from pdf2image import convert_from_path
from PIL.ImageQt import ImageQt

class Ui_TelaRelatorio(object):
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
        
        self.genComboBox = QtWidgets.QComboBox(self.frame_2)
        self.genComboBox.setEnabled(True)
        self.genComboBox.setGeometry(QtCore.QRect(420, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genComboBox.setFont(font)
        self.genComboBox.setObjectName("genComboBox")
        self.genComboBox.addItem("", 0)
        self.setGeneros()
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(430, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.audioComboBox = QtWidgets.QComboBox(self.frame_2)
        self.audioComboBox.setGeometry(QtCore.QRect(420, 200, 211, 31))
        self.audioComboBox.setObjectName("audioComboBox")
        self.audioComboBox.addItem("", 0)
        self.audioComboBox.addItem("Legendado", 2)
        self.audioComboBox.addItem("Dublado", 1)
        
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(430, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.classifComboBox = QtWidgets.QComboBox(self.frame_2)
        self.classifComboBox.setGeometry(QtCore.QRect(420, 270, 211, 31))
        self.classifComboBox.setObjectName("classifComboBox")
        self.classifComboBox.addItem("", 0)
        self.classifComboBox.addItem("Livre", 1)
        self.classifComboBox.addItem("10", 2)
        self.classifComboBox.addItem("12", 3)
        self.classifComboBox.addItem("14", 4)
        self.classifComboBox.addItem("16", 5)
        self.classifComboBox.addItem("18", 6)
        
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(430, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.statusComboBox = QtWidgets.QComboBox(self.frame_2)
        self.statusComboBox.setGeometry(QtCore.QRect(420, 340, 211, 31))
        self.statusComboBox.setObjectName("statusComboBox")
        self.statusComboBox.addItem("", 0)
        self.statusComboBox.addItem("Em Cartaz", 1)
        self.statusComboBox.addItem("Em Breve", 2)
        self.statusComboBox.addItem("Encerrado", 3)
        
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(430, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatórios de Filmes"))
        self.label_2.setText(_translate("MainWindow", "Relatórios"))
        self.label_6.setText(_translate("MainWindow", "Com filtros"))
        self.label_9.setText(_translate("MainWindow", "Geral"))
        self.simplesButton.setText(_translate("MainWindow", "Gerar"))
        self.robustButton.setText(_translate("MainWindow", "Gerar"))
        self.label_3.setText(_translate("MainWindow", "Gênero"))
        self.audioComboBox.setItemText(1, _translate("MainWindow", "Legendado"))
        self.audioComboBox.setItemText(2, _translate("MainWindow", "Dublado"))
        self.label_4.setText(_translate("MainWindow", "Áudio"))
        self.classifComboBox.setItemText(1, _translate("MainWindow", "Livre"))
        self.classifComboBox.setItemText(2, _translate("MainWindow", "10"))
        self.classifComboBox.setItemText(3, _translate("MainWindow", "12"))
        self.classifComboBox.setItemText(4, _translate("MainWindow", "14"))
        self.classifComboBox.setItemText(5, _translate("MainWindow", "16"))
        self.classifComboBox.setItemText(6, _translate("MainWindow", "18"))
        self.label_5.setText(_translate("MainWindow", "Classificação"))
        self.statusComboBox.setItemText(1, _translate("MainWindow", "Em Cartaz"))
        self.statusComboBox.setItemText(2, _translate("MainWindow", "Em Breve"))
        self.statusComboBox.setItemText(3, _translate("MainWindow", "Encerrado"))
        self.label_10.setText(_translate("MainWindow", "Estado"))


    def setGeneros(self):
        generos = Genero.getAll()
        for genero in generos:
            for info in genero:
                if isinstance(info, int):
                    index = info
                else:
                    nomeGen = info
            self.genComboBox.addItem(nomeGen, index)

    def clickedRelatorio(self, estado, tipo_rel):
        ref_genero = self.genComboBox.itemData(self.genComboBox.currentIndex())
        ref_tipo_audio = self.audioComboBox.itemData(self.audioComboBox.currentIndex())
        ref_classificacao = self.classifComboBox.itemData(self.classifComboBox.currentIndex())
        ref_estado_filme = self.statusComboBox.itemData(self.statusComboBox.currentIndex())

        if ref_genero!=0 or ref_tipo_audio!=0 or ref_classificacao!=0 or ref_estado_filme!=0:   
            GeraRelatorio.gerarFilmesFiltros(ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme)
            filename = 'listagem_filme_filtros.pdf'
        else:
            GeraRelatorio.gerarFilmes()
            filename = 'listagem_filme.pdf'
       
        self.printDialog(filename)
        
      
    def printDialog(self, filename):
        self.winTable = WinTable()
        frame = QtWidgets.QWidget(self.winTable)
        frame.setGeometry(QtCore.QRect(20, 0, 530, 670))
        images = convert_from_path(filename, dpi=300, output_folder="tmp")

        for i, image in enumerate(images):
            qim = ImageQt(image)
            print(qim)
            pix = QtGui.QPixmap.fromImage(qim)
            label = QtWidgets.QLabel(frame)
            label.setGeometry(QtCore.QRect(0, 0, 500, 670))
            label.setScaledContents(True)
            label.setPixmap(pix)
            
        self.winTable.show()

        
 

class WinTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "Relatórios de Filmes"
        self.top    = 150
        self.left   = 300
        self.width  = 550
        self.height = 680
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 