#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:31:02 2020

@author: sofiaarend
"""

from Model.Venda import Venda
from Model.IngressoVenda import IngressoVenda
from Model.Ingresso import Ingresso
from Model.Usuario import Usuario

class VendaCtrl(object):
     
    def cadastroVenda(self, ref_usuario, ingressos):
        valor_total = 0
        venda = Venda(valor_total, 0, "hoje", ref_usuario)
        venda.save()
        ref_venda = venda[0]
        for ingresso in ingressos:
            valor_total += ingresso[1]
            ing_venda = IngressoVenda(ingresso[0],ref_venda)
            ing_venda.save()
            
        Venda.update(ref_venda, valor_total, 0)