#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:01:30 2021

@author: pmchozas
"""

import requests
import json

def get_uri(term, lang):
    term="\""+term+"\""
    url = "http://sparql.lynx-project.eu/"
    query = """
    
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT ?c 
        WHERE {
        
        ?c a skos:Concept .
        ?c skos:prefLabel """+term+"""@"""+lang+""" .  }
  
        """
    print(query)
    headers = {'content-type': 'text/html; charset=UTF-8'}
    r=requests.get(url, params={'format': 'json', 'query': query})
    rjson=json.loads(r.text)
    
    
    if('results' in rjson.keys()):
        results=rjson['results']
        bindings=results['bindings']
        for b in range(len(bindings[0])):
            term_uri=bindings[b]['c']['value']

        
    
    return term_uri

term="contrato"
lang="es"


print(get_uri(term, lang))