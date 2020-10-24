#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:17:43 2020

@author: sofiaarend
"""
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication 


Form, Window = uic.loadUiType("apresentacao/tela_inicio.ui")

app = QApplication(sys.argv)

window = Window()

form = Form()
form.setupUi(window)

window.show()

sys.exit(app.exec_())
        

