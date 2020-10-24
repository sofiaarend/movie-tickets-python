#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:42:12 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
class Ingresso(object):
    def __init__(self, valor, ref_sessao, ref_cadeira, id=None):
        self.id = id
        self.ref_sessao = ref_sessao
        self.ref_cadeira = ref_cadeira
        self.valor = valor
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into ingresso values(default, %s, %s, %s)" % (self.valor, self.ref_sessao, self.ref_cadeira))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getSelfId(self):
        con = Conexao()
        ing = con.consultar("select id from ingresso where valor = %s and ref_sessao = %s and ref_cadeira = %s" % (self.valor, self.ref_sessao, self.ref_cadeira))
        con.fechar
        return ing[0][0]
    
    def update(id,ref_sessao,ref_cadeira,valor):
        try:
            con = Conexao() 
            sql = ("update ingresso set (valor,ref_sessao,ref_cadeira) = (%s,%s,%s) where id = %s" % (valor,ref_sessao,ref_cadeira,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from ingresso where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        ingressos = con.consultar("select * from ingresso")
        con.fechar
        return ingressos
    
    def getById(self, id):
        con = Conexao()
        ingresso = con.consultar("select * from ingresso where id = " + str(id))
        con.fechar
        return ingresso
    
    def getCadeirasBySessaoDia(ref_sessao):
        con = Conexao()
        ingresso = None
        ingresso = con.consultar("select ingresso.ref_cadeira from ingresso, ingresso_venda, venda "
                                 "where ingresso.id = ingresso_venda.ref_ingresso and "
                                 "venda.id = ingresso_venda.ref_venda and venda.data::date = now()::date and "
                                 "ingresso.ref_sessao =" + str(ref_sessao))
        con.fechar
        list_oc = []
        if ingresso != None:
            for ing in ingresso:
                list_oc.append(ing[0])
        return list_oc
        
        
        
        