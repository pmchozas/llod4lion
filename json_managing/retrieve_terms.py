#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:05:34 2020

@author: pmchozas
"""


import json


preflist_es=[]
altlist_es=[]
preflist_en=[]
altlist_en=[]




with open('llterms.json') as jsonfile:
    data= json.load(jsonfile)
    for p in data:
        for l in p['@graph']:
            try:
                for i in l['http://www.w3.org/2004/02/skos/core#prefLabel']:
                    if i['@language'] == 'es':
                        preflist_es.append(i['@value'])
                    if i['@language'] == 'en':
                        preflist_en.append(i['@value'])
            except:
                continue
            try:
                for i in l['http://www.w3.org/2004/02/skos/core#altLabel']:
                    if i['@language'] == 'es':
                        altlist_es.append(i['@value'])
                    if i['@language'] == 'en':
                        altlist_en.append(i['@value'])
            except:
                continue
        


print(preflist_en)
print(preflist_es)
print(altlist_en)
print(altlist_es)


with open('term_en.txt', 'w') as f:
    for item in preflist_en:
        f.write("%s\n" % item)
    for o in altlist_en:
        f.write("%s\n" % o)
        
        
f.close()
