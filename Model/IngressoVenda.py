#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:03:34 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
class IngressoVenda(object):
    def __init__(self, ref_ingresso, ref_venda, id=None):
        self.id = id
        self.ref_venda = ref_venda
        self.ref_ingresso = ref_ingresso
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into ingresso_venda values(default, %s, %s)" % (self.ref_ingresso,self.ref_venda))
            print (sql)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def update(id,ref_ingresso,ref_venda):
        try:
            con = Conexao() 
            sql = ("update ingresso_venda set (ref_ingresso,ref_venda) = (%s,%s) where id = %s" % (ref_ingresso,ref_venda,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from ingresso_venda where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        ingressos_vendas = con.consultar("select * from ingresso_venda")
        con.fechar
        return ingressos_vendas
    
    def getById(self, id):
        con = Conexao()
        ingresso_venda = con.consultar("select * from ingresso_venda where id = " + str(id))
        con.fechar
        return ingresso_venda
    
    def getByVenda(ref_venda):
        con = Conexao()
        ingressos_venda = con.consultar("select * from ingresso_venda where ref_venda = " + str(ref_venda))
        con.fechar
        return ingressos_venda