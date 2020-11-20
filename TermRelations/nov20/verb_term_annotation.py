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
import stanza


#framenet tests
'''
nltk.download('framenet_v17')

test=fn.frame_relations()

for t in test:
    print(t)

'''
f = open('estatuto.txt', 'r')

estatuto = f.read()

t = open('term_es.txt', 'r')

te=t.read()

terms=te.split('\n')
nlp = spacy.load('es_core_news_sm')

cleanterms=[]

v = open('legal_verbs.txt', 'r')
ve=v.read()
verbs=ve.split('\n')

#stanza.download('es') 

#nlp = stanza.Pipeline('es')


#ESTO ES UNA PRUEBA LEMATIZANDO SOLO LOS VERBOS DE ESTATUTO Y BUSCANDO LOS TÉRMINOS DE SKETCHENGINE tal cual
test='A tales efectos se entenderá excluida del ámbito laboral la actividad de las personas prestadoras del servicio de transporte al amparo de autorizaciones administrativas de las que sean titulares, realizada, mediante el correspondiente precio, con vehículos comerciales de servicio público cuya propiedad o poder directo de disposición ostenten, aun cuando dichos servicios se realicen de forma continuada para un mismo cargador o comercializador. 4. La legislación laboral española será de aplicación al trabajo que presten los trabajadores españoles contratados en España al servicio de empresas españolas en el extranjero, sin perjuicio de las normas de orden público aplicables en el lugar de trabajo. Dichos trabajadores tendrán, al menos, los derechos económicos que les corresponderían de trabajar en territorio español. 5. A efectos de esta ley se considera centro de trabajo la unidad productiva con organización específica, que sea dada de alta, como tal, ante la autoridad laboral. En la actividad de trabajo en el mar se considerará como centro de trabajo el buque, entendiéndose situado en la provincia donde radique su puerto de base.'
#elimino duplicados
lines_seen = set() # holds lines already seen
with open("output_file.txt", "w") as output_file:
	for each_line in open("results.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)
#aquí lematizo los verbos del estatuto, solo una vez

'''
doc = nlp(estatuto)

for sent in doc.sentences:
    for word in sent.words:
        if word.upos == 'VERB':
            #sent= sent.replace(word.text, word.lemma)
            estatuto=re.sub(r'\b' + word.text + r'\b',word.lemma, estatuto)
            


file=open("estatuto_verb_lemma.txt", "w")
file.write(estatuto)
'''
'''
#aquí saco los patrones, solo una vez también 
file = open('estatuto_verb_lemma.txt', 'r')
text=file.readlines()
file2 = open('term_es.txt', 'r')
rfile2=file2.read()
termlist=rfile2.split('\n')

terms=[]
with open('clean_term_es.txt', 'w') as l:
    for t in termlist:
        mylist=[]
        clean=re.sub(r'[^\w]', ' ', t)
        lower=clean.lower()
        terms.append(lower)
        l.write(lower+'\n')

with open('results.txt', 'w') as r:
    for term in terms:
        for line in text:
            sentences=re.split(r"[.!?]", line) #separo cada párrafo en frases
            for sent in sentences:
                if re.search(r'\b' + term + r'\b', sent): #busco el término exacto con regex
                    termpos=sent.index(term)
                    for term2 in terms:
                        if term!=term2 and re.search(r'\b' + term2 + r'\b', sent): #si busco el segundo término exacto, que tiene que ser diferente al primero
                            termpos2=sent.index(term2)
                            for verb in verbs:
                                if re.search(r'\b' + verb + r'\b', sent): #busco un verbo en esa frase
                                    verbpos=sent.index(verb)
                                    if verbpos > termpos and verbpos < termpos2 and termpos2<=(termpos+80): #si el verbo está en una posición intermedia entre t1 y t2, y t2 está como mucho a 80 posiciones de t1, saco el patrón
                                        r.write(term+', '+verb+', '+term2+'\n')
                                        # print(term +str(termpos)+'-------'+verb+str(verbpos)+'------'+term2+str(termpos2))
                                        # print(sent)

'''

'''
#ESTO ES UNA PRUEBA LEMATIZANDO QUE NO ME CONVENCE:

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
                    
                    