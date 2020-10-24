#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:17:34 2020

@author: sofiaarend
"""

from fpdf import FPDF
from Model.Usuario import Usuario
from Model.Filme import Filme
from Model.Genero import Genero
from Model.TipoAudio import TipoAudio
from Model.Classificacao import Classificacao
from Model.EstadoFilme import EstadoFilme

class GeraRelatorio(object):
    
    def setPdfUsuarios():   
        usuarios = Usuario.getAll()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial','B', 24)
        pdf.cell(60)
        pdf.cell(90, 10, "Dados dos usuários", 0, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-40)
        pdf.set_font('arial','B', 16)
        pdf.cell(50, 10, 'Nome', 1, 0, 'C')
        pdf.cell(40, 10, 'CPF', 1, 0, 'C')
        pdf.cell(40, 10, 'E-mail', 1, 0, 'C')
        pdf.cell(40, 10, 'Telefone', 1, 1, 'C')
        pdf.cell(10)
        pdf.set_font('arial', '', 12)
        for i in range(0, len(usuarios)):
            pdf.cell(50, 10, '%s' % (str(usuarios[i][3])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(usuarios[i][4])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(usuarios[i][5])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(usuarios[i][6])), 1, 1, 'C')
            pdf.cell(10)
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-30)
        pdf.output('usuarios.pdf', 'F')
        
    def setPdfFilmes():
        filmes = Filme.getAll() #fazer ordenado
         
        pdf = FPDF('L')
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial','B', 24)
        pdf.cell(60)
        pdf.cell(150, 10, "Filmes", 0, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-45)
        pdf.set_font('arial','B', 16)
        pdf.cell(70, 10, 'Nome', 1, 0, 'C')
        pdf.cell(30, 10, 'Duração', 1, 0, 'C')
        pdf.cell(40, 10, 'Gênero', 1, 0, 'C')
        pdf.cell(40, 10, 'Áudio', 1, 0, 'C')
        pdf.cell(40, 10, 'Classifição', 1, 0, 'C')
        pdf.cell(40, 10, 'Estado', 1, 1, 'C')
        pdf.cell(5)
        pdf.set_font('arial', '', 12)
        for i in range(0, len(filmes)):
            gen = Genero.getDescricaoById(filmes[i][3])
            aud = TipoAudio.getDescricaoById(filmes[i][4])         
            cla = Classificacao.getDescricaoById(filmes[i][5])
            est = EstadoFilme.getDescricaoById(filmes[i][6])
            
            pdf.cell(70, 10, '%s' % (str(filmes[i][1])), 1, 0, 'C')
            pdf.cell(30, 10, '%s' % (str(filmes[i][2])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(gen[0][0])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(aud[0][0])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(cla[0][0])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(est[0][0])), 1, 1, 'C')
            pdf.cell(5)
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-30)
        pdf.output('filmes.pdf', 'F')
        
