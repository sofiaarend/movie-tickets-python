#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:19:34 2020

@author: sofiaarend
"""
from Model.Conexao import Conexao 
class Genero(object):
    
    def __init__(self, descricao, id=None):
        self.id = id
        self.descricao = descricao
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into genero values(default, '" + self.descricao + "')")
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def update(id,descricao):
        try:
            con = Conexao() 
            sql = ("update genero set descricao = '%s' where id = %s" % (descricao,id))
            print(sql)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from genero where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        generos = con.consultar("select * from genero order by descricao")
        con.fechar
        return generos
    
    def getById(id):
        con = Conexao()
        genero = con.consultar("select * from genero where id = " + str(id))
        con.fechar
        return genero
    
    def getDescricaoById(id):
        con = Conexao()
        nome_genero = con.consultar("select descricao from genero where id = " + str(id))
        con.fechar
        return nome_genero
    

