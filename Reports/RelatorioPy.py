#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:03:44 2020

@author: sofiaarend
"""
import os
from py3o.template import Template
from Model.Filme import Filme
from Model.Genero import Genero
from Model.TipoAudio import TipoAudio
from Model.Classificacao import Classificacao
from Model.EstadoFilme import EstadoFilme
from Model.Usuario import Usuario
from Model.Venda import Venda


class Item(object):    
    def __init__(self, val1 = None , val2 = None, val3 = None, val4 = None, val5 = None, val6 = None):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        self.val5 = val5
        self.val6 = val6
    pass

class GeraRelatorio(object):
    
    def gerarFilmes():
        filmes = Filme.getAll()
        
        t = Template("template_filme.odt", "listagem_filme.odt")
        
        items = list()
        for filme in filmes:
            gen = Genero.getDescricaoById(filme[3])
            aud = TipoAudio.getDescricaoById(filme[4])         
            cla = Classificacao.getDescricaoById(filme[5])
            est = EstadoFilme.getDescricaoById(filme[6])
            
            item = Item(filme[1], filme[2], gen[0][0], aud[0][0], cla[0][0], est[0][0])
            item.val1 = filme[1]
            item.val2 = filme[2]
            item.val3 = gen[0][0]
            item.val4 = aud[0][0]
            item.val5 = cla[0][0]
            item.val6 = est[0][0]
            items.append(item)
        
        document = Item(filme[1], filme[2], gen[0][0], aud[0][0], cla[0][0], est[0][0])
        
        data = dict(items=items, document=document)
        t.render(data)
        
        os.system('unoconv -f pdf listagem_filme.odt')        

        
    def gerarFilmesFiltros(ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme):      
        filmes = Filme.getAllComFiltros(ref_genero, ref_tipo_audio, ref_classificacao, ref_estado_filme)
        
        t = Template("template_filme.odt", "listagem_filme_filtros.odt")
        
        items = list()
        for filme in filmes:
            gen = Genero.getDescricaoById(filme[3])
            aud = TipoAudio.getDescricaoById(filme[4])         
            cla = Classificacao.getDescricaoById(filme[5])
            est = EstadoFilme.getDescricaoById(filme[6])
            
            item = Item(filme[1], filme[2], gen[0][0], aud[0][0], cla[0][0], est[0][0])
            item.val1 = filme[1]
            item.val2 = filme[2]
            item.val3 = gen[0][0]
            item.val4 = aud[0][0]
            item.val5 = cla[0][0]
            item.val6 = est[0][0]
            items.append(item)
        
        document = Item()
        
        data = dict(items=items, document=document)
        t.render(data)
        
        os.system('unoconv -f pdf listagem_filme_filtros.odt')
        
    def gerarUsuariosFiltros(ref_tipo_usuario, fl_ativo):      
        usuarios = Usuario.getAllComFiltros(ref_tipo_usuario, fl_ativo)
        
        t = Template("template_usuarios.odt", "listagem_usuarios_filtros.odt")
        
        items = list()
        for usu in usuarios:
            item = Item()
            item.val1 = usu[3]
            item.val2 = usu[4]
            item.val3 = usu[5]
            item.val4 = usu[6]
            items.append(item)
        
        document = Item()
        
        data = dict(items=items, document=document)
        t.render(data)
        
        os.system('unoconv -f pdf listagem_usuarios_filtros.odt')
        
    def gerarUsuarios():
        usuarios = Usuario.getAll()
        
        t = Template("template_usuarios.odt", "listagem_usuarios.odt")
        
        items = list()
        for usu in usuarios:
            item = Item()
            item.val1 = usu[3]
            item.val2 = usu[4]
            item.val3 = usu[5]
            item.val4 = usu[6]
            items.append(item)
        
        document = Item()
        
        data = dict(items=items, document=document)
        t.render(data)
        
        os.system('unoconv -f pdf listagem_usuarios.odt')
        
    def gerarVendasFiltros(usuario, data1, data2, filme):
        vendas = None
        vendas = Venda.getByUsuarioDataRelatorio(usuario, data1, data2, filme)
        
        t = Template("template_vendas.odt", "listagem_vendas.odt")
        
        items = list()
        for venda in vendas:
            item = Item()
            item.val1 = venda[4]
            item.val2 = venda[5]
            item.val3 = venda[1]
            item.val4 = venda[2]
            items.append(item)
        
        document = Item()
        
        data = dict(items=items, document=document)
        t.render(data)
        
        os.system('unoconv -f pdf listagem_vendas.odt')