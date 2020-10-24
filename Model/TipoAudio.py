#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:45:15 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao 
class TipoAudio(object):
    
    #def __init__(self, id, descricao):
     #   self._id = id
     #   self._descricao = descricao
    
    def getAll(self):
        con = Conexao()
        tipos_audio = con.consultar("select * from tipo_audio")
        con.fechar
        return tipos_audio
    
    def getById(self, id):
        con = Conexao()
        tipo_audio = con.consultar("select * from tipo_audio where id = " + str(id))
        con.fechar
        return tipo_audio
    
    def getDescricaoById(id):
        con = Conexao()
        descricao = con.consultar("select descricao from tipo_audio where id = " + str(id))
        con.fechar
        return descricao