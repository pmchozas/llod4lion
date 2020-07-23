#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:55:54 2020

@author: pmchozas
"""

#esto lo he sacado de internet pero estaría bien cómo aprender a hacerlo
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

print(postaglist)

for i in range(len(postaglist)):
    if('NOUN' == postaglist[i]): #cuando encuentra noun, posnoun vale la posicion de la lista, (1) en el primer caso
        posnoun=i 
        newword=wordlist[posnoun] #correspondencia en wordlist con la posición i (artículo en el primer caso)
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


with open('data/resultlist.txt', 'w') as f2:
    for item in resultlist:
        f2.write("%s\n" % item)
    f2.close()
    
with open('data/verbrangelist.txt', 'w') as f2:
    for item in verbrangelist:
        f2.write("%s\n" % item)
    f2.close()

# for i in range(len(postaglist)):
#     if('NOUN' == postaglist[i]):
#         posnoun=i
#         if(posnoun+3<len(postaglist)):
#             j=postaglist[i+1:i+5]
#             print(j)
#             for pos in range(len(j)):
#  	            if('VERB' ==j[pos]):
#  	                posverb=pos
#  	                print(posverb)
                    
            
            
            
            
            
            # if('VERB' in j):
                # posverb=postaglist.index('VERB')
                # print(posverb)
               
                #print(wordlist[i]+' '+wordlist[i+2]+' '+wordlist[i+5])

 #and 'NOUN' in postaglist[i+3:i+9])       
#patrón NOUN+VERB+NOUN      


#patrón PROPN+VERB+NOUn
# 	if('PROPN' == postaglist[i]):
# 		posnoun=i
# 		if(postaglist[i+2]=='VERB' and postaglist[i+5]=='NOUN'):
# 			print(wordlist[i]+' '+wordlist[i+2]+' '+wordlist[i+5])            
            
#             if('PROPN' == postaglist[i]):
#             posnoun=i
#             if(postaglist[i+2]=='PROPN' and postaglist[i+3]=='VERB' and postaglist[i+5]=='NOUN'):
# 			print(wordlist[i]+' '+wordlist[i+2]+' '+wordlist[i+5])        
            
#-------intentos fallidos--------- 
# for k in postaglist:
#     if k=='NOUN':
#         posnoun=postaglist.index('NOUN')
#         print(posnoun)

#print(wordlist)


# with open('wordlist.txt', 'w') as wlist:
#     for item in wordlist:
#         wlist.write("%s\n" % item)
#     wlist.close()

# with open('postaglist.txt', 'w') as plist:
#     for item in postaglist:
#         plist.write("%s\n" % item)
#     plist.close()




        


#for k in postaglist:
 #   if k=='NOUN':
 #       posverb=postaglist.index('VERB')
  #      if pos
        
     
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        