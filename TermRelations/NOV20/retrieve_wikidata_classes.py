#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:28:37 2020

@author: pmchozas
"""

import csv
import requests

url = 'https://query.wikidata.org/sparql'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

retrieve_query = """
SELECT * {
       ?item rdfs:label "TERM"@es.
      OPTIONAL {
        ?item wdt:P279 ?brterm.
      }
      }
    """

broader_query = """
SELECT * {
       brID rdfs:label ?label.
       FILTER (lang(?label) = "en")
      }
"""



with open('500rel_out1.csv', newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    with open('500rel_outall.csv', 'w', newline='') as outfile:
        writer=csv.writer(outfile, quoting=csv.QUOTE_ALL)

        for row in reader:
            
            #print(row)
            term1=row[2].strip()
            print(term1)
            query = retrieve_query.replace("TERM", term1)     
            #print(query)
            r1 = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
            data1 = r1.json()
            if len(data1['results']['bindings']) !=0:
                data1bindings=data1['results']['bindings']
                #print(data1bindings)
                for bind in data1bindings:
                    try:
                        if bind['brterm']['value']:
                            brURI1=bind['brterm']['value']
                            brID1=brURI1.replace("http://www.wikidata.org/entity/", "wd:")
                            brquery = broader_query.replace("brID", brID1)
                            #print(brquery)
                            br1 = requests.get(url, params={'format': 'json', 'query': brquery}, headers=headers)
                            brdata1 = br1.json()
                            #print(brdata1)
                            if len(brdata1['results']['bindings']) !=0:
                                brdata1bindings=brdata1['results']['bindings']
                                for brbind in brdata1bindings:
                             #       print('BROADER')
                                    broader='E2:'+brbind['label']['value']
                              #      print(broader)
                                    row.append(broader)
                               #     print(row)
                    
                    except:
                        print('something happened')
                                    
            writer.writerow(row)    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        