#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:34:28 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao
#from Model.Filme import Filme
class Sessao(object):
    def __init__(self, horario_inicio, ref_filme, ref_sala, horario_fim, id=None):
        self.id = id
        self.horario_inicio = horario_inicio
        self.ref_sala = ref_sala
        self.ref_filme = ref_filme
        self.horario_fim = horario_fim
        
    def save(self):
        try:
            con = Conexao()
            sql = ("insert into sessao values(default, '%s', %s, %s, '%s')" % (self.horario_inicio,self.ref_filme,self.ref_sala,self.horario_fim))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def update(id,horario_inicio,ref_filme,ref_sala,horario_fim):
        try:
            con = Conexao() 
            sql = ("update sessao set (horario_inicio,ref_filme,ref_sala,horario_fim) = (%s,%s,%s,%s) where id = %s" % (horario_inicio,ref_filme,ref_sala,horario_fim,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def updateLugares(id,cadeira_ocupada):
        
        try:
            con = Conexao() 
            lugares = con.consultar("select cadeiras_ocupadas from sessao where id = " + str(id))
            if lugares[0][0] != None: 
                sql = ("update sessao set cadeiras_ocupadas = CONCAT(cadeiras_ocupadas,',','%s') where id = %s" % (cadeira_ocupada,id))
            else:
                sql = ("update sessao set cadeiras_ocupadas = '%s' where id = %s" % (cadeira_ocupada,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("delete from sessao where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        sessoes = con.consultar("select * from sessao")
        con.fechar
        return sessoes
    
    def getById(id):
        con = Conexao()
        sessao = con.consultar("select * from sessao where id = " + str(id))
        con.fechar
        return sessao
    
    def getSessoesBySala(ref_sala):
        con = Conexao()
        sessoes = con.consultar("select * from sessao where ref_sala = " + str(ref_sala))
        con.fechar
        return sessoes
    
    def getSessoesByFilme(ref_filme):
        con = Conexao()
        sessoes = con.consultar("select * from sessao where ref_filme = " + str(ref_filme)+" order by horario_inicio")
        con.fechar
        return sessoes
    
    def getSessoesAtivasPorSala(ref_sala):
        con = Conexao()
        sessoes = con.consultar("select sessao.* "
                                "from sessao, filme "
                                "where ref_sala = " + str(ref_sala)+" and "
                                "sessao.ref_filme = filme.id and "
                                "filme.ref_estado_filme = 1 "
                                "order by horario_inicio")
        con.fechar
        return sessoes
    
    def getSessoesAtivas():
        con = Conexao()
        sessoes = con.consultar("select sessao.* "
                                "from sessao, filme "
                                "where sessao.ref_filme = filme.id and "
                                "filme.ref_estado_filme = 1 "
                                "order by horario_inicio")
        con.fechar
        return sessoes
    