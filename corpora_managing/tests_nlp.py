#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:55:24 2021

@author: pmchozas
"""

import stanfordnlp

stanfordnlp.download('es')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("inevitablemente, pepino, algo más")
doc.sentences[0].print_dependencies