#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:58:07 2020

@author: pmchozas
"""

import requests


r = requests.get("https://ixasrl.linkeddata.es/pos?txt=Ella%20come%20patatas")

text="Esto es una prueba"

params = {'txt':text}
rsrl= requests.get("https://ixasrl.linkeddata.es/srl?", params=params)

ixa_pos = "https://ixasrl.linkeddata.es/pos?"

ixa_srl = "https://ixasrl.linkeddata.es/srl?"


#request.get 


print(rsrl.text)

print(rsrl.url)