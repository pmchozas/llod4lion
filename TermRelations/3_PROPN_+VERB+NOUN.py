#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:16:47 2020

@author: pmchozas
"""


with open('data/estatuto_pos.txt') as f:
    poslist = [line.rstrip('\n') for line in f]
  #  print(poslist)
    

    
newlist=list()
postaglist=list()
wordlist=list()
resultlist=list()
verbrangelist=list()

for i in poslist:
    t=i.split('|')
    newlist.append(t)
#print(newlist)

for t in newlist:
    wordlist.append(t[0])
    postaglist.append(t[1])


for i in range(len(postaglist)):
    if('PROPN' == postaglist[i] or ('PROPN' == postaglist[i] and 'PROPN'== postaglist[i+1])): #cuando encuentra noun, posnoun vale la posicion de la lista, (1) en el primer caso
        posnoun=i
        posnoun2=i+1
        newword=wordlist[posnoun]+' '+wordlist[posnoun2] #correspondencia en wordlist con la posición i (artículo en el primer caso)
        #print( '->',newword)
        if(posnoun+5<len(postaglist)): #para que no compruebe más allá de la longitud de la lista
            verbrange=postaglist[posnoun:posnoun+5] #verbrange define el rango donde puede estar el verbo (desde la posición del nombre, 5 posiciones en adelante)
            #
            print('verbrange',verbrange)
            verbrangelist.append(verbrange)
            for pos in range(len(verbrange)):#recorremos el rango donde puede estar el verbo (5posiciones)
	            if('VERB' ==verbrange[pos]): #si encontramos un verbo en una de las posiciones de la lista
	                posverb=posnoun+pos #la posición del verbo será la posición del nombre anterior + la posición de la sublista (pos)
	                newword+=' '+wordlist[posverb] #+= lo que tenía la variable anteriormente más lo nuevo. ahora tenemos el noun, más el verbo que encontremos en wordlist en la posición posverb
	                #print('-->',newword)
	                nounrange=postaglist[posverb:posverb+5] #aquí hacemos otra sublista para buscar un nombre a partir de la posición del verbo
	                #print('nounrange-',nounrange)
	                for pos1 in range(len(nounrange)): #recorremos la sublista buscando un nombre
	                	if('NOUN' ==nounrange[pos1]):
	                		posnoun2=posverb+pos1 #la posición del segundo nombre, la calculamos igual a partir de la posición del verbo
	                		newword+=' '+wordlist[posnoun2] #y a lo que había le añadimos el nombre correspondiente
	                		print('--->',newword)
	                		resultlist.append(newword)


with open('data/PVN_resultlist.txt', 'w') as f2:
    for item in resultlist:
        f2.write("%s\n" % item)
    f2.close()
    
with open('data/PVN_verbrangelist.txt', 'w') as f2:
    for item in verbrangelist:
        f2.write("%s\n" % item)
    f2.close()