#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:01:00 2020

@author: sofiaarend
"""


from Model.Conexao import Conexao 
class EstadoFilme(object):
    
    def __init__(self, id, descricao):
        self._id = id
        self._descricao = descricao
    
    def getAll(self):
        con = Conexao()
        estados_filme = con.consultar("select * from estado_filme")
        con.fechar
        return estados_filme
    
    def getById(self, id):
        con = Conexao()
        estado_filme = con.consultar("select * from estado_filme where id = " + str(id))
        con.fechar
        return estado_filme
    
    def getDescricaoById(id):
        con = Conexao()
        descricao = con.consultar("select descricao from estado_filme where id = " + str(id))
        con.fechar
        return descricao