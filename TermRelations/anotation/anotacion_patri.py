#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:58:56 2020

@author: pmchozas
"""
from verbecc import Conjugator
import nltk

from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer


#intento de anotacion de patri, que basicamente es script de karen pero sin procesar json.

#funcion para poner en plural
def plural(termlist):
    singular=[]
    plural=[]
    valuelist_all=[]
    
    for i in termlist:
        if('es' not in i[-2:] or 's' not in i[-1:] ):
            singular.append(i)
            if('a' in i[-1:] or 'e' in i[-1:] or 'o' in i[-1:]):
                plu=i+'s'
                plural.append(plu)
                valuelist_all.append(plu)
                
            elif('ón' in i[-2:] or 'l' in i[-1:] or 'y' in i[-1:] or 'd' in i[-1:] or 'r' in i[-1:]):
                plu=i+'es'
                #print(plu)
                plural.append(plu)
                valuelist_all.append(plu)
            elif('z' in i[-1:]):
                plu=i[:-1]+'ces'
                #print(plu)
                plural.append(plu)
                valuelist_all.append(plu)
        else:
            plural.append(i)
            if('es' in i[-2:]):
                sing=i[:-2]
                #print(sing)
                singular.append(sing)
                valuelist_all.append(sing)
            elif('s' in i[-1:] ):
                sing=i[:-1]
                singular.append(sing)
                valuelist_all.append(sing)
            
            elif('ces' in i[-1:]):
                sing=i[:-3]+'z'
                #print(sing)
                singular.append(sing)
                valuelist_all.append(sing)
                

    
    #print(plural)
    #print(singular)

    
    return(plural, singular, valuelist_all)

def labelled(valuelist):
    file=open('estatuto_es.txt', 'r', encoding='utf-8')
    read=file.readlines()
    new=open('estatuto_es_br.txt', 'w')
    newc=open('listTerms_conts.csv', 'w')
    #conts = csv.writer(newc)
    
    
    ready=[]
    
    
    for i in read:
        cont=0
        for j in valuelist[1]:
            low=i.lower()
            
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3='<br>'+find2+'</br>'
                i=i.replace(find2, find3)
        for j in valuelist[2]:
            low=i.lower()
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3=' <br>'+find2+'</br> '
                i=i.replace(' '+find2+' ', find3)
        for j in valuelist[3]:
            low=i.lower()
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3=' <br>'+find2+'</br> '
                i=i.replace(' '+find2+' ', find3)
            
            
        new.write(i)


    
    new.close()



f=open('legal_verbs.txt', 'r', encoding='utf-8')
file=open('estatuto_es.txt', 'r', encoding='utf-8')
read=file.readlines()
new=open('estatuto_es_br.txt', 'w')
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
 
    
text="2. Las disposiciones legales y reglamentarias se aplicarán con sujeción estricta al principio de jerarquía normativa. Las disposiciones reglamentarias desarrollarán los preceptos que establecen las normas de rango superior, pero no podrán establecer condiciones de trabajo distintas a las establecidas por las leyes a desarrollar."

textlow=text.lower()

for j in stemlist:
    if j in textlow:
        #print(j)
        pos=textlow.index(j)
        lenj=len(j)
        endpos=pos+lenj
        #print(endpos)
        for k in textlow:
            if textlow[endpos]!=' ':
                endpos=endpos+1
                continue
        else:
            #print(endpos)
            print(j+'-->'+str(pos)+', '+str(endpos))
        
             
            
        


'''    
for i in read:
    for j in verblist:
        low=i.lower()
        find=low.find(j)
        if(find>0):
            tam=len(j)+find
            find2=i[find:tam]
            find3='<br>'+find2+'</br>'
            i=i.replace(find2, find3)   
    new.write(i)
new.close()
'''     
        
'''
cg = Conjugator(lang='es')
conjugation = cg.conjugate('dictar')

print(conjugation)
'''

#labelled(verblist)
    
