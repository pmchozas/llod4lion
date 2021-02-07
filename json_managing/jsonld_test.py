#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:51:54 2021

@author: pmchozas
"""
from rdflib import Graph, Literal
from SPARQLWrapper import SPARQLWrapper


g = Graph()
g.load("input.jsonld", format="jsonld")
with open("output.nt", "w") as fp:
    fp.write(g.serialize(format="nt", indent=4))