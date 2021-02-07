#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:58:07 2020

@author: pmchozas
"""

import requests


r = requests.get("https://ixasrl.linkeddata.es/pos?txt=Ella%20come%20patatas")


ixa_pos = "https://ixasrl.linkeddata.es/pos?"

ixa_srl = "https://ixasrl.linkeddata.es/srl?"

text="Esto es una prueba"

#request.get 


print(r.text)

print(r.url)