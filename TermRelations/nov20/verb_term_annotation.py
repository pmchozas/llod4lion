#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:02:35 2020

@author: pmchozas
"""

f = open('estatuto.txt', 'r')

estatuto = f.read()

t = open('term_es.txt', 'r')

te=t.read()

terms=te.split('\n')


v = open('legal_verbs.txt', 'r')
ve=v.read()
verbs=ve.split('\n')

print(len(estatuto))