#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:06:43 2021

@author: pmchozas
"""

from pynlp import StanfordCoreNLP
import requests
# print(requests.post('https://corenlp-tool.lynx-project.eu/', tagtype='pos'))


# pos_tagger = CoreNLPParser('https://corenlp-tool.lynx-project.eu/', tagtype='pos')

annotators = 'tokenize, ssplit, pos, lemma, ner, entitymentions, coref, sentiment, quote, openie'
options = {'openie.resolve_coref': True}

text="The employer takes maternity leave if needed"

doc=requests.post('https://corenlp.run/?properties={"annotators":"tokenize, ssplit, pos, lemma, ner, entitymentions, coref, sentiment, openie","outputFormat":"json"}', data = text, )
print(doc.text)


#no funciona, tiene que estar corenlp funcionando