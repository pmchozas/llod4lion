#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:35:31 2020

@author: pmchozas
"""
termlist=list()
nonumlist=list()

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://publications.europa.eu/webapi/rdf/sparql")
sparql.setQuery("""
       PREFIX euvoc: <http://publications.europa.eu/ontology/euvoc#>
       PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
       PREFIX dct: <http://purl.org/dc/terms/>
       SELECT DISTINCT ?topuris ?toplabel ?suburi ?sublabel ?nauri ?nalabel
       WHERE {
       ?topuris dct:subject <http://eurovoc.europa.eu/100153>;
       skos:prefLabel ?toplabel.
       ?topuris skos:hasTopConcept ?suburi .
       ?suburi skos:prefLabel ?sublabel;
       skos:narrower ?nauri.
       ?nauri skos:prefLabel ?nalabel.
       FILTER (lang(?toplabel) = "es")
       FILTER (lang(?sublabel) = "es")
       FILTER (lang(?nalabel) = "es")
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

#print(results)

for result in results["results"]["bindings"]:
    termlist.append(result["toplabel"]["value"])


for result in results["results"]["bindings"]:
    termlist.append(result["sublabel"]["value"])

for result in results["results"]["bindings"]:
    termlist.append(result["nalabel"]["value"])
    
    
for i in termlist:
    result = ''.join([k for k in i if not k.isdigit()])
    nonumlist.append(result.strip())
    
    
clean_termlist = list(dict.fromkeys(nonumlist))


with open('eurovoc_terms.txt', 'w') as f2:
    for t in clean_termlist:
        f2.write("%s\n" % t)
    f2.close()

    

