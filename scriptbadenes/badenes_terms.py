#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:11:48 2020

@author: pmchozas
"""
import spacy
import pytextrank
import os
#import it_core_news_sm
from langdetect import detect


#spacy.load("en")


def get_language(text):
  try:
    lang = detect(text)
    return lang
  except:
    return "en"

def get_keywords(text):
  # load a spaCy model, depending on language, scale, etc.
  lang = get_language(text)
  os.system('python3 -m spacy download '+lang)
  nlp = spacy.load(lang)
  nlp.max_length = 29204346
  # add PyTextRank to the spaCy pipeline
  tr = pytextrank.TextRank()
  nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
  doc = nlp(text)
  # examine the top-ranked phrases in the document
  key_words=[]
  for p in doc._.phrases:
      #print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
      key_words.append(p.text)
  return key_words



if __name__ == "__main__":
  file = open("smallcorpus.txt", "r")
  text=file.read()

  #print(len(text))
  
  f = open('results.txt','a')
  test=get_keywords(text)
  #print(test)
  f.write(str(test) + '\n')
  f.close()
