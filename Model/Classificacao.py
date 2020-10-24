#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:39:22 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao 
class Classificacao(object):
    
    #def __init__(self, id, descricao):
     #   self._id = id
     #   self._descricao = descricao
    
    def getAll(self):
        con = Conexao()
        classificacoes = con.consultar("select * from classificacao")
        con.fechar
        return classificacoes
    
    def getById(self, id):
        con = Conexao()
        classificacao = con.consultar("select * from classificacao where id = " + str(id))
        con.fechar
        return classificacao
    
    def getDescricaoById(id):
        con = Conexao()
        descricao = con.consultar("select descricao from classificacao where id = " + str(id))
        con.fechar
        return descricao