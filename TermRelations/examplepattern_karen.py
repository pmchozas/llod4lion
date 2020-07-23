#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:01:32 2020

@author: pmchozas
"""


import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

textpatri = 'siempre que convivan con el empresario , el cónyuge , los descendientes , ascendientes y demás parientes por consanguinidad o afinidad , hasta el segundo grado inclusive y , en su caso , por adopción.f ) La actividad de las personas que intervengan en operaciones mercantiles por cuenta de uno o más empresarios , siempre que queden personalmente obligados a responder del buen fin de la operación asumiendo el riesgo y ventura de la misma.g ) En general , todo trabajo que se efectúe en desarrollo de relación distinta de la que define el apartado 1.A tales efectos se entenderá excluida del ámbito laboral la actividad de las personas prestadoras del servicio de transporte al amparo de autorizaciones administrativas de las que sean titulares , realizada , mediante el correspondiente precio , con vehículos comerciales de servicio público cuya propiedad o poder directo de disposición ostenten , aun cuando dichos servicios se realicen de forma continuada para un mismo cargador o comercializador.'
pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
pattern = list()
postaglist = list()
wordlist = list()
tag = pos_tagger.tag(textpatri.split(' '))
for t in tag:
	pattern.append(t)
	postaglist.append(t[1])
	wordlist.append(t[0])

print(wordlist)
print(postaglist)
#ejemplo: ADV+VERB+NOUN, pero hay ADV-SCONJ-VERB-ADP-DET-NOUN
