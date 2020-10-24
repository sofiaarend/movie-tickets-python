#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:13:45 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
class Cadeira(object):
    def __init__(self, estado_cadeira, ref_sala, nome, id=None):
        self.id = id
        self.ref_sala = ref_sala
        self.estado_cadeira = estado_cadeira
        self.nome = nome
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into cadeira values(default, %s, %s, '%s')" % (self.estado_cadeira, self.ref_sala, self.nome))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def update(id,estado_cadeira):
        try:
            con = Conexao() 
            sql = ("update cadeira set estado_cadeira = %s where id = %s" % (estado_cadeira,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from cadeira where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        cadeiras = con.consultar("select * from cadeira")
        con.fechar
        return cadeiras
    
    def getAllBySala(ref_sala):
        con = Conexao()
        cadeiras = con.consultar("select * from cadeira where ref_sala = "+str(ref_sala))
        con.fechar
        return cadeiras
    
    def getById(id):
        con = Conexao()
        cadeira = con.consultar("select * from cadeira where id = " + str(id))
        con.fechar
        return cadeira
    
    def getIdByNomeSala(nome, ref_sala):
        con = Conexao()
        cadeira = con.consultar("select id from cadeira where nome = '%s' and ref_sala = %s" % (nome,ref_sala))
        con.fechar
        return cadeira[0]