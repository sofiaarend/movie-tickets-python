#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:46:23 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
from Model.Usuario import Usuario
from datetime import datetime

class Venda(object):
    def __init__(self, valor_total, desconto, data, ref_usuario, id=None):
        self.id = id
        self.valor_total = valor_total
        self.desconto = desconto
        self.data = data
        self.ref_usuario = ref_usuario
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into venda values(default, %s, %s, '%s', %s)" % (self.valor_total, self.desconto, self.data, self.ref_usuario))
            print (sql)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getSelfId(self):
        con = Conexao()
        ing = con.consultar("select id from venda where data = '%s' and ref_usuario = %s" % (self.data, self.ref_usuario))
        con.fechar
        return ing[0][0]
    
    def update(id,valor_total,desconto):
        try:
            con = Conexao() 
            sql = ("update venda set (valor_total,desconto) = (%s,%s) where id = %s" % (valor_total,desconto,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from venda where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        vendas = con.consultar("select * from venda")
        con.fechar
        return vendas
    
    def getByUsuarioData(usu, data1, data2, filme):
        if filme in locals():
            Venda.getByUsuarioDataFilme(usu, data1, data2, filme)
        else:
            con = Conexao()
            sql = "select * from venda where 1=1"
            if len(str(usu)) > 0:
                ref_usu = Usuario.getIdByNome(usu)
                sql += (" and ref_usuario = %s " % (ref_usu))
    
            if len(str(data1)) > 2 and len(str(data2)) > 2:
                data1 = data1 + " 00:00:00"
                data2 = data2 + " 23:59:59"
                data_1 = datetime.strptime(data1, '%d/%m/%Y %H:%M:%S')
                data_2 = datetime.strptime(data2, '%d/%m/%Y %H:%M:%S')
                sql += " and data > '%s' and data < '%s' " % (data_1, data_2)
    
            sql += "order by data"
            venda = con.consultar(sql)    
            con.fechar
            return venda
        
    def getByUsuarioDataFilme(usu, data1, data2, filme):
        con = Conexao()
        sql = "select distinct venda.id , venda.valor_total , venda.data::date , venda.ref_usuario "
        sql += "from venda,filme,sessao,ingresso,ingresso_venda "
        sql += "where filme.id = sessao.ref_filme and sessao.id = ingresso.ref_sessao and "
        sql += "ingresso.id = ingresso_venda.ref_ingresso and ingresso_venda.ref_venda = venda.id"
        
        if filme != 0:
            sql += " and filme.id = %s" % (filme)
        
        if len(str(usu)) > 0:
            ref_usu = Usuario.getIdByNome(usu)
            sql += " and venda.ref_usuario = %s " % (ref_usu)

        if len(str(data1)) > 2 and len(str(data2)) > 2:
            data1 = data1 + " 00:00:00"
            data2 = data2 + " 23:59:59"
            data_1 = datetime.strptime(data1, '%d/%m/%Y %H:%M:%S')
            data_2 = datetime.strptime(data2, '%d/%m/%Y %H:%M:%S')
            sql += " and venda.data > '%s' and venda.data < '%s' " % (data_1, data_2)
        
        
        sql += " group by 1 order by data"
        venda = con.consultar(sql)    
        con.fechar
        return venda
    
    def getById(self, id):
        con = Conexao()
        venda = con.consultar("select * from venda where id = " + str(id))
        con.fechar
        return venda
    
    def getByUsuario(ref_usuario):
        con = Conexao()
        venda = con.consultar("select * from venda where ref_usuario = " + str(ref_usuario))
        con.fechar
        return venda
    
    def getByUsuarioDataRelatorio(ref_usu, data1, data2, filme):
        con = Conexao()
        sql = "select distinct venda.id, venda.valor_total, venda.data::date, venda.ref_usuario, usuario.nome , filme.nome "
        sql += "from venda , filme , sessao , ingresso , ingresso_venda , usuario "
        sql += "where filme.id = sessao.ref_filme and sessao.id = ingresso.ref_sessao and "
        sql += "ingresso.id = ingresso_venda.ref_ingresso and ingresso_venda.ref_venda = venda.id and "
        sql += "usuario.id = venda.ref_usuario "
        
        if filme != 0:
            sql += "and filme.id = %s" % (filme)
        
        if ref_usu != 0:
            sql += " and venda.ref_usuario = %s " % (ref_usu)

        if len(str(data1)) > 2 and len(str(data2)) > 2:
            data1 = data1 + " 00:00:00"
            data2 = data2 + " 23:59:59"
            data_1 = datetime.strptime(data1, '%d/%m/%Y %H:%M:%S')
            data_2 = datetime.strptime(data2, '%d/%m/%Y %H:%M:%S')
            sql += " and venda.data > '%s' and venda.data < '%s' " % (data_1, data_2)
        

        sql += "group by 1,5,6 order by usuario.nome"
        venda = con.consultar(sql)    
        con.fechar
        return venda
        