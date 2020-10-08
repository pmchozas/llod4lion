# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:59:53 2020

@author: Pablo
"""



class Term:
    
    string = ''
    lang = ''
    score=0
    corpus=''
    synonyms=[]
    
    iateURL=''
    
    
    translations = {} 
  
   
    
    def __init__(self, term, code):
        self.string = term
        self.lang = code

    def get_data(self):
        print(self.string+' '+self.lang+' Synonyms: '+''.join(self.synonyms))
        print(self.translations)
    
    def getJson(self):
        
        return { 'lang':self.lang}




termino1 = Term('trabajador','es')
termino2 = Term('worker', 'en')





termino1.get_data()
termino2.get_data()

'''

lista=[]
lista.append(termino1)
lista.append(termino2)
print(lista)


 # Adding list as value 
termino1.translations["de"] = ['sdsssss'] 
termino1.translations["en"] = ["worker", "laborist"] 

print(termino1.translations.get('en'))

termino1.get_data()

termino1.synonyms.append('estatuto trabajadores')
termino1.get_data()


del termino1.synonyms[0]

termino1.getJson()

'''