#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:13:33 2020

@author: sofiaarend
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:29:47 2020

@author: sofiaarend
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Model.Filme import Filme
from Model.Sessao import Sessao
from datetime import datetime, timedelta

class SessaoCtrl(object):
    
    def cadastroSessao(self, main, Form):
        ref_filme = self.filmeComboBox.itemData(self.filmeComboBox.currentIndex())
        ref_sala = self.salaComboBox.itemData(self.salaComboBox.currentIndex())
        hora_inicio = self.inicioField.text()
        
        if (not ref_filme) or (not ref_sala) or (not hora_inicio):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos marcados com (*) são obrigatórios.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()            
        else:
            filme = Filme.getById(ref_filme)
            
            hora_inicio = datetime.strptime(hora_inicio, "%H:%M")
            hora_fim = (hora_inicio + timedelta(minutes=filme[0][2])).time()
            hora_inicio = (hora_inicio).time()

            sessoes = Sessao.getSessoesAtivasPorSala(ref_sala)
            
            continua = 1
            for sessao in sessoes:                
                if (sessao[1] > hora_inicio and sessao[1] < hora_fim) or (sessao[4] > hora_inicio and sessao[4] < hora_fim):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("O horário selecionado interfere com outra sessão já existente.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_() 
                    continua = 0
                elif sessao[1] == hora_inicio or sessao[1] == hora_fim or sessao[4] == hora_inicio or sessao[4] == hora_fim:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("O horário selecionado interfere com outra sessão já existente.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    continua = 0
                    
            if continua == 1:
                sessao = Sessao(hora_inicio, ref_filme, ref_sala, hora_fim)
                success = sessao.save()
                if success == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Sessão cadastrada com sucesso.")
                    msg.setWindowTitle("Sucesso")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    Form.close()
                    main.show()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Erro ao cadastrar sessão.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    Form.close()
                    main.show()

