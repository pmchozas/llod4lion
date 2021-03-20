#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:18:23 2021

@author: pmchozas
"""

import requests
#import Term
from modules_api import Term
from modules_api import postprocess
from modules_api import TBXTools 



def test_extract(myterm):
    url='https://termitup.oeg.fi.upm.es/extract_terminology?'
    params={'lang_in': myterm.lang_in, 'corpus': myterm.context}
    


def test_postproc(terms, lang, tasks):

    url='https://termitup.oeg.fi.upm.es/postprocess_terminology?'
    params={'terms': terms, 'tasks': tasks, 'source_language':lang}
    
    response = requests.post(url,params=params)
    value=response.json()
    return value

terms="pepino, treinta, cincuenta, 5 de febrero"
tasks="numbers, timeEx"
lang="es"

print(test_postproc(terms, lang, tasks))
