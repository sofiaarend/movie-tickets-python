#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:58:25 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao 
from Model.Genero import Genero
from Model.TipoAudio import TipoAudio
from Model.Classificacao import Classificacao
from Model.EstadoFilme import EstadoFilme

class Filme(object):
    
    def __init__(self, nome, duracao, ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme, poster_url, id=None):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.ref_genero = ref_genero
        self.ref_tipo_audio = ref_tipo_audio
        self.ref_classificacao = ref_classificacao
        self.ref_estado_filme = ref_estado_filme
        self.poster_url = poster_url
        
    def save(self):
        try:
            con = Conexao()
            sql = "insert into filme values(default, '" + self.nome + "'," + str(self.duracao) + "," + str(self.ref_genero) + ","+ str(self.ref_tipo_audio) + ","+ str(self.ref_classificacao) + ","+ str(self.ref_estado_filme) +",'"+ self.poster_url + "')"
            print(sql)
            con.manipular(sql)
            con.fechar
            return 1
        except:
            return 0
        
    def update(id,nome,duracao,ref_genero,ref_tipo_audio,ref_classificacao,ref_estado_filme,poster_url):
        try:
            con = Conexao() 
            sql = ("update filme set (nome,duracao,ref_genero,ref_tipo_audio,ref_classificacao,ref_estado_filme,poster_url) = ('%s', %s, %s, %s, %s, %s, '%s') where id = %s" % (nome,duracao,ref_genero,ref_tipo_audio,ref_classificacao,ref_estado_filme,poster_url,id))
            print (sql)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao()
            sql = "update filme set ref_estado_filme = 3 where id = " + str(id)
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        filmes = con.consultar("select * from filme order by nome")
        con.fechar
        return filmes
    
    def getById(id):
        con = Conexao()
        filme = con.consultar("select * from filme where id = " + str(id))
        con.fechar
        return filme
    
    def getGenero(self):
        genero = Genero()
        return genero.getById(self.ref_genero)
    
    def getTipoAudio(self):
        tipo_audio = TipoAudio()
        return tipo_audio.getById(self.ref_tipo_audio)
    
    def getClassificacao(self):
        classificacao = Classificacao()
        return classificacao.getById(self.ref_classificacao)
    
    def getEstadoFilme(self):
        estado_filme = EstadoFilme()
        return estado_filme.getById(self.ref_estado_filme)
    
    def getDuracaoById(id):
        con = Conexao()
        duracao = con.consultar("select duracao from filme where id = " + str(id))
        con.fechar
        return duracao
    
    def getAllComFiltros(ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme):
        con = Conexao()
        if ref_genero != 0:
            sql = (" and ref_genero = %s " % (ref_genero))
        else:
            sql = ""
        
        if ref_tipo_audio != 0:
            sql += (" and ref_tipo_audio = %s " % (ref_tipo_audio))
        else:
            sql += ""   
            
        if ref_classificacao != 0:
            sql += (" and ref_classificacao = %s " % (ref_classificacao))
        else:
            sql += ""
            
        if ref_estado_filme != 0:
            sql += (" and ref_estado_filme = %s " % (ref_estado_filme))
        else:
            sql += ""
        
        print(sql)
        filmes = con.consultar("select * from filme where 1 = 1" + sql)  
        con.fechar
        return filmes
    
