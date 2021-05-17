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




'''

esta función es para sacar los términos 

'''
with open('labourlaw_thesaurus.json') as jsonfile:
    data= json.load(jsonfile)
    for alldata in data:
        for topconcept in alldata['@graph']:
            try:
                for concept in topconcept['http://www.w3.org/2004/02/skos/core#prefLabel']:
                    if concept['@language'] == 'es':
                        preflist_es.append(concept['@value'])
                    if concept['@language'] == 'en':
                        preflist_en.append(concept['@value'])
            except:
                continue
            try:
                for concept in topconcept['http://www.w3.org/2004/02/skos/core#altLabel']:
                    if concept['@language'] == 'es':
                        altlist_es.append(concept['@value'])
                    if concept['@language'] == 'en':
                        altlist_en.append(concept['@value'])
            except:
                continue
        


print(preflist_en)
print(preflist_es)
print(altlist_en)
print(altlist_es)


with open('llterms_es.txt', 'w') as f:
    for item in preflist_es:
        f.write("%s\n" % item)
    for syn in altlist_es:
        f.write("%s\n" % syn)
        
        
f.close()
