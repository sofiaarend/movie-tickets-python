#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:28:57 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao 
class TipoUsuario(object):
    
    #def __init__(self, id, descricao):
     #   self._id = id
     #   self._descricao = descricao
    
    def getAll(self):
        con = Conexao('localhost', 'cinema', 'sofiaarend', 'postgres')
        tipos_usuario = con.consultar("select * from tipo_usuario")
        con.fechar
        return tipos_usuario
    
    def getById(self, id):
        con = Conexao('localhost', 'cinema', 'sofiaarend', 'postgres')
        tipo_usuario = con.consultar("select * from tipo_usuario where id = " + str(id))
        con.fechar
        return tipo_usuario