#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:54:50 2020

@author: pmchozas
"""
# import stanza
import spacy

# stanza.download('es')
# nlp = stanza.Pipeline('es')
file=open('data/estatuto.txt')
f = file.read()


#pos stanza
'''
pos = nlp(f) #json con toda la info del postagging
f.close()
list=[]
for sentence in pos.sentences:
    for word in sentence.words:
        list.append(word.lemma+'|'+word.pos)

with open('data/estatuto_pos.txt', 'w') as f2:
    for item in list:
        f2.write("%s\n" % item)
    f2.close()

'''
        
#ner stanza      
'''
ner = stanza.Pipeline(lang='es', processors='tokenize,ner')
estner = ner(f)

nerlist=[]

for sent in estner.sentences:
    for token in sent.tokens:
        nerlist.append('token: '+token.text + ', ' + 'ner: '+ token.ner)
        
with open('data/estatuto_ner_stanza.txt', 'w') as f3:
    for l in nerlist:
        f3.write("%s\n" % l)
    f3.close()
'''
    
#ner spacy 2.1 debería probar con el modelo más nuevo.
    
nlp = spacy.load("es_core_news_sm")

test= nlp(f)
spacylist=[]
for ent in test.ents:
    spacylist.append('token: '+ent.text + ', ' + 'ner: '+ent.label_)
    
    
with open('data/estatuto_ner_spacy.txt', 'w') as f3:
    for l in spacylist:
        f3.write("%s\n" % l)
    f3.close()