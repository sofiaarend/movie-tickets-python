#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:44:53 2020

@author: sofiaarend
"""

#import psycopg2
#con = psycopg2.connect(host='localhost', database='cinema',
 #                      user='sofiaarend', password='postgres')
#cur = con.cursor()
#sql = 'create table genero (id serial primary key, descricao varchar(60))'
#cur.execute(sql)
#sql = "insert into genero values (default,'Terror')"
#cur.execute(sql)
#con.commit()

#cur.execute('select * from genero')
#recset = cur.fetchall()
#con.close()

#from model.Conexao import Conexao
#con = Conexao('localhost', 'cinema', 'sofiaarend', 'postgres')
#sql = "insert into genero values (default, 'Aventura')"

#if con.manipular(sql):
#    print('inserido com sucesso!')
    
#print (con.proximaPK('genero', 'id'))
#rs=con.consultar("select * from genero")  
#for rec in rs:
 #   print (rec)
#con.fechar()
 
from model.Filme import Filme

#filme = Filme()
#filme.save

print(Filme.getAll())
print(Filme.getById(12))
#print (filme.nome)

#filmes = filme.getAll
#print (filmes)
#film = filme.getGenero
#print (film)
# open -a Designer : abrir qt designer





