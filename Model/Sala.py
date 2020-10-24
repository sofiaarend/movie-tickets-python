#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:10:11 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
class Sala(object):
    def __init__(self, total_cadeiras, id=None):
        self.id = id
        self.total_cadeiras = total_cadeiras
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into sala values(default, %s)" % (self.total_cadeiras))
            print (sql)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def update(id,total_cadeiras):
        try:
            con = Conexao() 
            sql = ("update sala set total_cadeiras = %s where id = %s" % (total_cadeiras,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from sala where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        salas = con.consultar("select * from sala")
        con.fechar
        return salas
    
    def getById(self, id):
        con = Conexao()
        sala = con.consultar("select * from sala where id = " + str(id))
        con.fechar
        return sala