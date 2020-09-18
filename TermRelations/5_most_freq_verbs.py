#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:19:02 2020

@author: pmchozas
"""


with open('data/results/MostFrequentLegalPatterns.txt') as f:
    g=f.readlines()

l=[]

for i in g:
    k=i.strip('\n[] \'')
    k=k.replace("'","").replace(" ","")
    k = k.split(',')
    l.append(k)


l2= set()
for t in l:
    l2.add(t[1])


#aquí se construye un diccionario que tenga los elementos del l2 + []
finalset= dict.fromkeys(l2, []) 
#print(finalset)

for word in l2:
    aux = []
    for t in range(len(l)):
        word2 = l[t][1]      
        if (word == word2):
            aux.append(t)
    finalset[word] = aux
           





# for key in finalset:
#     print(key+ '[%s]' % ', '.join(map(str, finalset[key])))
    
    
#    for i in finalset[key]:
#        print(str(i)+",")
#    print("\n\n\n")
#print(finalset)
            
    
    #print(t[0]+" "+t[1]+" "+t[2])         

''' 
esto hace algo raro que no entiendo
      
my_set_list = [set(t) for t in l]
print(my_set_list)

for i1, t in enumerate(my_set_list):
    for i2 in range(i1 + 1, len(my_set_list)):
        for val in (t & my_set_list[i2]):
            print("Index {} matched with index {} for value {}".format(i1,i2,val))


'''
