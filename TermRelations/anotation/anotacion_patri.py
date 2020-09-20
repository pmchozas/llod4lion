#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:58:56 2020

@author: pmchozas
"""

import nltk

from nltk.stem.snowball import SnowballStemmer





f=open('legal_verbs.txt', 'r', encoding='utf-8')
file=open('estatuto_es.txt', 'r', encoding='utf-8')
read=file.readlines()
new=open('estatuto_es_verb.txt', 'w')
span=open('estatuto_es_span.txt', 'r', encoding='utf-8')
newc=open('listTerms_conts.csv', 'w')


#ptstemmer = PorterStemmer()
snstemmer = SnowballStemmer(language='spanish')

verblist=[]
for i in f:
    k=i.strip('\n')
    verblist.append(k)

 
'''
for verb in verblist:
    stem=ptstemmer.stem(verb)
    print(verb + ' --> ' + stem)
'''

stemlist=[]
for verb in verblist:
    stem=snstemmer.stem(verb)
    stemlist.append(stem)
 
    
#text="2. Las disposiciones legales y reglamentarias se aplicarán con sujeción estricta al principio de jerarquía normativa. Las disposiciones reglamentarias desarrollarán los preceptos que establecen las normas de rango superior, pero no podrán establecer condiciones de trabajo distintas a las establecidas por las leyes a desarrollar."

#textlow=text.lower()
    
estatuto=span.read()


#print(textlow)
for j in stemlist:
    if j in estatuto:
        pos=estatuto.index(j)
        lenj=len(j)
        endpos=pos+lenj
        #print(endpos)
        for k in estatuto:
            #print(k)
            if estatuto[endpos]!=' ':
                endpos=endpos+1
                continue
        else:
            #print(endpos)
            #print(j+'-->'+str(pos)+', '+str(endpos))
            term=estatuto[pos:endpos]
            #print(term)
            tagterm='<span class="verb">'+estatuto[pos:endpos]+'</span>'
            estatuto=estatuto.replace(term, tagterm)
        
new.write(estatuto)

            
    


    
