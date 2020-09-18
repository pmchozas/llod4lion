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
file=open('estatuto_parrafo.txt')
f = file.read()

pos = nlp(f) #json con toda la info del postagging


for sentence in pos.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.pos)