#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:02:35 2020

@author: pmchozas
"""

import nltk
from nltk.corpus import framenet as fn
import spacy
#from spacy_spanish_lemmatizer import SpacyCustomLemmatizer
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import re



#framenet tests
'''
nltk.download('framenet_v17')

test=fn.frame_relations()

for t in test:
    print(t)

'''
f = open('estatuto.txt', 'r')

estatuto = f.readlines()

t = open('term_es.txt', 'r')

te=t.read()

terms=te.split('\n')
nlp = spacy.load('es_core_news_sm')

cleanterms=[]

v = open('legal_verbs.txt', 'r')
ve=v.read()
verbs=ve.split('\n')

#aquí limpio símbolos de los términos, todo lo que no sea alfanumérico y los lematizo


lemma=""

sololemmalist=[]
with open('lemmalist.txt', 'w') as l:
    for t in terms:
        mylist=[]
        clean=re.sub(r'[^\w]', ' ', t)
        lower=clean.lower()
        string = nlp(lower)
        for token in string:
            token=token.lemma_
            mylist.append(token)
        lemma = ' ' .join(mylist)
        sololemmalist.append(lemma)
        l.write(t+'|'+lemma+'\n')



e = open('estatuto_lema.txt', 'r')
estlema=e.readlines()

for lemma in sololemmalist:
    for line in estlema:
        if re.search(r'\b' + lemma + r'\b', line):
            termpos=line.index(lemma)
            for lemma2 in sololemmalist:
                if lemma!=lemma2 and re.search(r'\b' + lemma2 + r'\b', line):
                    termpos2=line.index(lemma2)
                    for verb in verbs:
                        if re.search(r'\b' + verb + r'\b', line):
                            verbpos=line.index(verb)
                            if verbpos > termpos and verbpos < termpos2:
                                print(lemma +'-------'+verb+'------'+lemma2)
                                print(line)
        
    
with open('cleantermlist.txt', 'w') as f:
    for term in cleanterms:
        f.write(term+'\n')



#print(len(estatuto))



#AQUÍ LEMATIZO EL ESTATUTO, SOLO UNA VEZ


'''        
file = open('estatuto.txt', 'r')
read=file.readlines()

with open('estatuto_lema.txt', 'w') as f:
    for line in read:
        doc = nlp(line)
        for token in doc:
            sourcetoken=token.lemma_
            f.write(sourcetoken+' ')
f.close()
'''



'''

#ESTO ES UNA PRUEBA STEMIZANDO QUE NO ME CONVENCE:
    
#stemizo términos y verbos. uso el snowball porque el porter lo deja prácticamente igual

snstemmer = SnowballStemmer(language='spanish')

#este código de abajo es para stemizar el estatuto, se hace una vez y ya está

with open('estatuto_clean.txt', 'w') as c:
    for line in estatuto:
        cleanest=re.sub(r'[^\w]', ' ', line)
        c.write(cleanest+'\n')
        
file = open('estatuto_clean.txt', 'r')
read=file.readlines()

with open('estatuto_stem.txt', 'w') as f:
    for line in read:
        doc = nlp(line)
        for token in doc:
            sourcetoken=token.text
            stemtoken=snstemmer.stem(sourcetoken)
            f.write(sourcetoken+'|'+stemtoken+' ')




termstemlist=[]
for term in cleanterms:
    if ' ' in term:
        compound=term.split(' ')
        for token in compound:
            tokenstem=snstemmer.stem(token)
            termstemlist.append(tokenstem)
    else:
        termstems=snstemmer.stem(term)
        termstemlist.append(termstems)
    #print(term + ' --> ' + snstemmer.stem(term))
    
verbstemlist=[]

for verb in verbs:
    verbstems=snstemmer.stem(verb)
    verbstemlist.append(verbstems)
    #print(verb + ' --> ' + verbstems)

#ahora tengo 4 listas. términos, verbos, términos stemizados y verbos stemizados. 
#busco coincidencias en el estatuto estemizado

# e = open('estatuto_stem.txt', 'r')
# text=e.readlines()

e = open('test.txt', 'r')
text=e.readlines()

with open('termlist.txt', 'w') as f:
    for term in termstemlist:
        f.write(term+'\n')

    

for term in termstemlist:
    for line in text:
        match=re.search('\w*\|'+term+'$', line, flags=0)
        if match!= None:
            print('TERM-------------->'+term)
            print(line)
            print(match)
        #if term in line:


'''


'''

Problemas: 
   - conjugación de verbos.
        puedo lematizar y buscar el lema + lo que siga hasta el espacio
        puedo buscar término + cualquier verbo usando estatuto pos + término
        puedo usar un conjugador de verbos (esto creo que no)
        
   - género y número de los términos
        puedo lematizar y buscar el lema, tanto del pos como de los términos
        
   - el problema es que el estatuto_pos lo tokeniza todo, entonces los términos compuestos no los encontraría
   - lematizar términos?



for term in terms:
    if term in estatuto:
        termpos=estatuto.index(term)
        if (termpos+5<len(estatuto)):
            verbrange=[termpos:termpos+5]
            for verb in verbs:
                if verb :
                    
'''                    
                    
                    