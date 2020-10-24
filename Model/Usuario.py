#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:41:14 2020

@author: sofiaarend
"""

from Model.Conexao import Conexao 
from Model.TipoUsuario import TipoUsuario

class Usuario(object):
    
    def __init__(self, usuario, senha, nome, email, ref_tipo_usuario, cpf=None, telefone=None, id=None, fl_ativo=None):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.ref_tipo_usuario = ref_tipo_usuario
        self.fl_ativo = fl_ativo

    def save(self):
        try:
            con = Conexao() 
            sql = ("insert into usuario values(default, '%s', '%s', '%s', '%s', '%s', '%s', '%s', default)" % (self.usuario,self.senha,self.nome,self.cpf,self.email,self.telefone,self.ref_tipo_usuario))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
        
    def update(id,usuario,nome,cpf,email,telefone,admin):
        try:
            con = Conexao() 
            sql = ("update usuario set (usuario,nome,cpf,email,telefone,ref_tipo_usuario) = ('%s', '%s', '%s', '%s', '%s',%s) where id = %s" % (usuario,nome,cpf,email,telefone,admin,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def updateSenha(id,usuario,senha,nome,cpf,email,telefone):
        try:
            con = Conexao() 
            sql = ("update usuario set (usuario,senha,nome,cpf,email,telefone) = ('%s', '%s', '%s', '%s', '%s', '%s') where id = %s" % (usuario,senha,nome,cpf,email,telefone,id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def desativarUsuario(self,id):
        try:
            con = Conexao() 
            sql = ("update usuario set fl_ativo = false where id = %s" % (id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def delete(id):
        try:
            con = Conexao() 
            sql = ("update usuario set fl_ativo = FALSE where id ="+ str(id))
            con.manipular(sql)
            con.fechar
        except:
            return 0
        return 1
    
    def getAll():
        con = Conexao()
        usuarios = con.consultar("select * from usuario")
        con.fechar
        return usuarios
    
    def getById(id):
        con = Conexao()
        usuario = con.consultar("select * from usuario where id = " + str(id))
        con.fechar
        return usuario
    
    def getByUsuario(usuario):
        try:
            con = Conexao()
            usuario = con.consultar("select * from usuario where usuario = '" + str(usuario) + "'")
            con.fechar
            return usuario
        except:
            return 0
        
    def getIdByNome(nome):
        try:
            con = Conexao()
            usuario = con.consultar("select id from usuario where nome = '" + str(nome) + "'")
            con.fechar
            return usuario[0][0]
        except:
            return 0
    
    def getTipoUsuario(self):
        tipo_usuario = TipoUsuario()
        return tipo_usuario.getById(self.ref_tipo_usuario)
    
    def getAllComFiltros(ref_tipo_usuario, fl_ativo):
        con = Conexao()
        if ref_tipo_usuario != 0:
            sql1 = (" and ref_tipo_usuario = %s" % (ref_tipo_usuario))
        else:
            sql1 = ""
        
        if fl_ativo == 1:
            sql2 = (" and fl_ativo = true")
        elif fl_ativo == 2:
            sql2 = (" and fl_ativo = false")
        else:
            sql2 = ""   

        filmes = con.consultar("select * from usuario where 1 = 1" + sql1 + sql2)  
        con.fechar
        return filmes