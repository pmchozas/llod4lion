#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:47:19 2020

@author: pmchozas
"""


#in this script, we want to select the structures whose verbs are in the legal_verb list
#this is, we are only interested in those "domain patterns"

nvnlist=list()
verblist=list()
tokenlist=list()
resultlist=list()
cleanlist=list()
cleanerlist=list()

nvn=open('data/results/NVN_resultlist.txt', 'r', encoding='utf-8')
mynvn=nvn.readlines()

#aquí limpio los saltos de línea porque si no sale term\n

for i in mynvn:
    clean=i.strip('\n')
    nvnlist.append(clean)
#print(nvnlist)

verbs=open('data/legal_verbs.txt', 'r', encoding='utf-8')
myverbs=verbs.readlines()


for k in myverbs:
    cleanv=k.strip('\n')
    verblist.append(cleanv)

#we are looking only for those patterns that contain most frequent verb in pos1
#nvnlist1=['gobierno establecer norma', 'pedro tener casa']
#verblist1=['designar', 'establecer']
for j in nvnlist:
    t=j.split(' ')
    for v in verblist:
        if v in t[1]:
            resultlist.append(t)



#here I remove patterns with more than 4 tokens (those are not correct)
for w in resultlist:
    if len(w)==3:
        cleanlist.append(w)

#we are now removing duplicates

for x in cleanlist:
    if x not in cleanerlist:
        cleanerlist.append(x)
    

with open('data/results/MostFrequentLegalPatterns.txt', 'w') as f2:
    for item in cleanerlist:
        f2.write("%s\n" % item)
    f2.close()