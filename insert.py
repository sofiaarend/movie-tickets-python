#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:07:55 2020

@author: sofiaarend
"""

#insert into sessao values (default, horario_inicio, ref_filme, ref_sala, horario_fim)

#from Model.Sessao import Sessao
#
#ses = Sessao('21:00', 21, 2, '23:06')
#ses.save()

#from Model.Cadeira import Cadeira

#rows = ['A','B','C','D','E','F']
#j=1
#for i in rows:
#    j=1
#    while j <= 13:
#        cad = Cadeira(True, 3, i+str(j))
#        cad.save()
#        j+=1
        
        
#insert into tipo_usuario values(default, 'Admin');
#insert into tipo_usuario values(default, 'Cliente');

#insert into tipo_audio values(default, 'Dublado');
#insert into tipo_audio values(default, 'Legendado');

#insert into estado_filme values(default, 'Em Cartaz');
#insert into estado_filme values(default, 'Em Breve');
#insert into estado_filme values(default, 'Encerrado');

#insert into classificacao values(default, 'L');
#insert into classificacao values(default, '10');
#insert into classificacao values(default, '12');
#insert into classificacao values(default, '14');
#insert into classificacao values(default, '16');
#insert into classificacao values(default, '18');

#insert into sala values(default, 117);
#insert into sala values(default, 117);
#insert into sala values(default, 117);


select distinct(venda.id), venda.valor_total, venda.data, venda.ref_usuario 
from venda,filme,sessao,ingresso,ingresso_venda 
where filme.id = sessao.ref_filme and sessao.id = ingresso.ref_sessao and 
ingresso.id = ingresso_venda.ref_ingresso and ingresso_venda.ref_venda = venda.id