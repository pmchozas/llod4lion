#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:54:50 2020

@author: pmchozas
"""
import stanza
import spacy
import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stanza.download('es')
nlp = stanza.Pipeline('es')
file=open('estatuto.txt')
f = file.read()


pos = nlp(f) #json con toda la info del postagging
f.close()
list=[]
for sentence in pos.sentences:
    for word in sentence.words:
        list.append(word.lemma+'|'+word.pos)

with open('estatuto_pos.txt', 'w') as f2:
    for item in list:
        f2.write("%s\n" % item)
    f2.close()


        
        


#or t1 in list:
 #   if t1=''