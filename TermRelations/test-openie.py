#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:06:43 2021

@author: pmchozas
"""

from pynlp import StanfordCoreNLP

annotators = 'tokenize, ssplit, pos, lemma, ner, entitymentions, coref, sentiment, quote, openie'
options = {'openie.resolve_coref': True}

nlp = StanfordCoreNLP(annotators=annotators, options=options)

text="esto es una prueba"
document = nlp(text)

print(document) 

#no funciona, tiene que estar corenlp funcionando