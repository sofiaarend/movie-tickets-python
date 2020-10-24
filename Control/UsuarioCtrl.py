#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:40:10 2020

@author: sofiaarend
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Model.Usuario import Usuario
import hashlib 

class UsuarioCtrl(object):
    
    def cadastroUsuario(self, codcli, tipo_usu, Form):
        nome = self.nomeField.text()
        cpf = self.cpfField.text()
        email = self.mailField.text()
        telefone = self.telField.text()
        usuario = self.userField.text()
        senha = self.passField.text()
        senha_confirm = self.confirm_passField.text()

        fl_username = Usuario.getByUsuario(usuario)
        
        if tipo_usu == 1:
            fl_admin = self.checkBox.isChecked()
        else:
            fl_admin = None;
        
        if (not nome) or (not email) or (not usuario):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos marcados com (*) são obrigatórios.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif len(cpf) > 3 and len(cpf) < 14:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("CPF inválido.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif len(str(telefone)) > 2 and len(str(telefone)) < 12:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Telefone inválido.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        #else if email...
        else: 
            if codcli == 0:
                if fl_username:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("O nome de usuário escolhido já existe.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                elif not senha:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Por favor escolha uma senha.")
                    msg.setWindowTitle("Erro")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    if (senha != senha_confirm):
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("A senha deve ser a mesma nos campos Senha e Confirmar senha.")
                        msg.setWindowTitle("Erro")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                    else:
                        if fl_admin:
                            admin = 1
                        else:
                            admin = 2
                        h_senha = hashlib.md5(senha.encode('utf-8'))
                        hash_s = h_senha.hexdigest()
                        usu = Usuario(usuario, hash_s, nome, email, admin, cpf, telefone)
                        
                        success = usu.save()
                        if success == 1:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Usuário cadastrado com sucesso.")
                            msg.setWindowTitle("Sucesso")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()   
                            Form.close()
                        else: 
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Erro ao cadastrar usuário.")
                            msg.setWindowTitle("Erro")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
            else:
                if not senha:
                    if fl_admin:
                        admin = 1
                    else:
                        admin = 2
                    success = Usuario.update(codcli,usuario,nome,cpf,email,telefone,admin)
                    if success == 1:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Usuário editado com sucesso.")
                        msg.setWindowTitle("Sucesso")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()   
                        Form.close()
                    else: 
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Erro ao editar usuário.")
                        msg.setWindowTitle("Erro")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                else:
                    if (senha != senha_confirm):
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("A senha deve ser a mesma nos campos Senha e Confirmar senha.")
                        msg.setWindowTitle("Erro")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                    else:
                        h_senha = hashlib.md5(senha.encode('utf-8'))
                        hash_s = h_senha.hexdigest()
                        success = Usuario.updateSenha(codcli,usuario,hash_s,nome,cpf,email,telefone)
                        if success == 1:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Usuário editado com sucesso. Senha modificada.")
                            msg.setWindowTitle("Sucesso")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()  
                            Form.close()
                        else: 
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Erro ao editar usuário.")
                            msg.setWindowTitle("Erro")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                
    def loginUsuario(self, user, senha): 
        hashed_senha = hashlib.md5(senha.encode('utf-8'))

        usu = Usuario.getByUsuario(user)
        if not usu:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Usuário não existe.")
            msg.setWindowTitle("Erro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            if hashed_senha.hexdigest() == usu[0][2]:
               return usu 
            else:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Warning)
               msg.setText("Usuário ou senha incorretos.")
               msg.setWindowTitle("Erro")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.exec_()
               
        
        