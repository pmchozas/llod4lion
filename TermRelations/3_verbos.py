#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:54:00 2020

@author: pmchozas

"""
#en este script elimino los "verbos vacíos" de la lista de verbos más frecuentes
#así me quedo solo con los "verbos de dominio"
#los verbos vacíos los saco de la lista de stopwords
#guardo la lista de "verbos de dominio" en un nuevo archivo txt 'legal_verbs'

stoplist=list()
verblist=list()

stop=open('data/stop-esp.txt', 'r', encoding='utf-8')
mystop=stop.readlines()
#print(mystop)

#aquí limpio los saltos de línea porque si no sale term\n

for i in mystop:
    clean=i.strip('\n')
    stoplist.append(clean)
#print(stoplist)

verbs=open('data/verbos_estatuto.txt', 'r', encoding='utf-8')
myverbs=verbs.readlines()


for k in myverbs:
    cleanv=k.strip('\n')
    verblist.append(cleanv)
#print(verblist)


for j in verblist:
    for l in stoplist:
        if j==l:
            verblist.remove(j)
            
#print(verblist)            

with open('data/legal_verbs.txt', 'w') as f2:
    for item in verblist:
        f2.write("%s\n" % item)
    f2.close()
            