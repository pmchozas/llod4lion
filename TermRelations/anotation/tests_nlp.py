#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:55:24 2021

@author: pmchozas
"""
import requests
import json
# f=open("estatuto_es.txt")
# string=f.read()

# word_list = string.split()

# number_of_words = len(word_list)
# print(number_of_words)


f = open("terms.txt")
text=f.read()

termlist=text.split('\n')

for term in termlist:
    params = {'txt':term}
    rpos= requests.get("https://ixasrl.linkeddata.es/pos?", params=params)
    rjson=json.loads(rpos.text)
    
    token=rjson['annotations'][0]
    if token['pos'][0]=='V':
        termlist.remove(term)
f2=open('entities.txt', 'w')        
for term in termlist:
    f2.write(term+'\n')
f2.close()


"""
import stanfordnlp

stanfordnlp.download('es')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("inevitablemente, pepino, algo más")
doc.sentences[0].print_dependencies
"""