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

class FilmeCtrl(object):
    
    def cadastroFilme(self, codfilme, Form, list_usu, list_gen, list_venda, codcli, main):
        nome = self.nomeField.text()
        duracao = self.duracaoField.text()
        ref_genero = self.genComboBox.itemData(self.genComboBox.currentIndex())
        ref_tipo_audio = self.audioComboBox.itemData(self.audioComboBox.currentIndex())
        ref_classificacao = self.classifComboBox.itemData(self.classifComboBox.currentIndex())
        ref_estado_filme = self.statusComboBox.itemData(self.statusComboBox.currentIndex())
        poster_url = self.posterField.text()
        
        sessoes = Sessao.getSessoesByFilme(codfilme)
        
        if (not nome) or (not duracao):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos marcados com (*) são obrigatórios.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif ref_estado_filme == 1 and not sessoes:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("O filme deve ter sessões cadastradas para entrar em cartaz.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            if codfilme == 0:
                filme = Filme(nome, duracao, ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme, poster_url)
                success = filme.save()
                if success == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Filme cadastrado com sucesso.")
                    msg.setWindowTitle("Sucesso")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    FilmeCtrl.abreLista(codcli, list_usu, list_gen, list_venda, Form, main)
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Erro ao cadastrar filme.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
            else:
                success = Filme.update(codfilme,nome,duracao,ref_genero,ref_tipo_audio,ref_classificacao,ref_estado_filme, poster_url)
                if success == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Filme editado com sucesso.")
                    msg.setWindowTitle("Sucesso")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()   
                    FilmeCtrl.abreLista(codcli, list_usu, list_gen, list_venda, Form, main)
                else: 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Erro ao editar filme.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
            
    def deleteFilme(self, codfilme):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Tem certeza que deseja desativar o filme?")
        msgBox.setWindowTitle("Confirmar ação")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            if Filme.delete(codfilme) == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Filme desativado com sucesso.")
                msg.setWindowTitle("Sucesso")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Erro ao desativar filme.")
                msg.setWindowTitle("Erro")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                
    def abreLista(codcli, list_usu, list_gen, list_venda, Form, main):
        listFilme = QtWidgets.QMainWindow()
        ui = main
        ui.setupUi(listFilme, codcli, list_usu, list_gen, list_venda)
        listFilme.show()
        Form.close()
    