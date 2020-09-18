import os
import json
import csv

def read_terms(file):
    new=open('termimos_json.txt', 'w')
    valuelist=[]
    lang_list=[]
    with open(file) as f:
        file = json.load(f)
    item=file[0]['@graph']
    for i in range(len(item)):
        ide=item[i]['@id']
        item2=item[i]
        
        if('http://www.w3.org/2004/02/skos/core#prefLabel' in item2.keys()):
            w3pref=item2['http://www.w3.org/2004/02/skos/core#prefLabel']
            for j in range(len(w3pref)):
                value=w3pref[j]['@value']
                language=w3pref[j]['@language']
                if(language=='es'):
                    valuelist.append(value)
                #print('pref')
        if('http://www.w3.org/2004/02/skos/core#altLabel' in item2.keys() ):
            w3alt=item2['http://www.w3.org/2004/02/skos/core#altLabel']
            for j in range(len(w3alt)):
                value=w3alt[j]['@value']
                language=w3alt[j]['@language']
                if(language=='es'):
                    valuelist.append(value)
                #print('alt')
    


    valuelist2=sorted(list(set(valuelist)))
    valuelist_all=[]
    valuelist_largos=[]
    valuelist_cortos=[]
    for i in valuelist2:
        spl=i.split(' ')
        if(len(spl)>1):
            valuelist_largos.append(i)
            valuelist_all.append(i)
        else:
            valuelist_cortos.append(i)

    singular=[]
    plural=[]
    
    for i in valuelist_cortos:
        if('es' not in i[-2:] or 's' not in i[-1:] ):
            singular.append(i)
            if('a' in i[-1:] or 'e' in i[-1:] or 'o' in i[-1:]):
                plu=i+'s'
                plural.append(plu)
                valuelist_all.append(plu)
                
            elif('ón' in i[-2:] or 'l' in i[-1:] or 'y' in i[-1:] or 'd' in i[-1:] or 'r' in i[-1:]):
                plu=i+'es'
                #print(plu)
                plural.append(plu)
                valuelist_all.append(plu)
            elif('z' in i[-1:]):
                plu=i[:-1]+'ces'
                #print(plu)
                plural.append(plu)
                valuelist_all.append(plu)
        else:
            plural.append(i)
            if('es' in i[-2:]):
                sing=i[:-2]
                #print(sing)
                singular.append(sing)
                valuelist_all.append(sing)
            elif('s' in i[-1:] ):
                sing=i[:-1]
                singular.append(sing)
                valuelist_all.append(sing)
            
            elif('ces' in i[-1:]):
                sing=i[:-3]+'z'
                #print(sing)
                singular.append(sing)
                valuelist_all.append(sing)
                

    
    #print(plural)
    #print(singular)

    
    return(valuelist, valuelist_largos, plural, singular, valuelist_all)

def labelled(valuelist):
    file=open('estatuto_es.txt', 'r', encoding='utf-8')
    read=file.readlines()
    new=open('estatuto_es_span.txt', 'w')
    newc=open('listTerms_conts.csv', 'w')
    conts = csv.writer(newc)
    
    
    ready=[]
    
    
    for i in read:
        cont=0
        for j in valuelist[1]:
            low=i.lower()
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3='<span>'+find2+'</span>'
                i=i.replace(find2, find3)
        for j in valuelist[2]:
            low=i.lower()
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3=' <span>'+find2+'</span> '
                i=i.replace(' '+find2+' ', find3)
        for j in valuelist[3]:
            low=i.lower()
            find=low.find(j)
            if(find>0):
                tam=len(j)+find
                find2=i[find:tam]
                find3=' <span>'+find2+'</span> '
                i=i.replace(' '+find2+' ', find3)
            
            
        new.write(i)


    
    new.close()

def cont(valuelist):
    file=open('estatuto_es.txt', 'r', encoding='utf-8')
    read=file.readlines()
    newc=open('listTerms_conts.csv', 'w')
    conts = csv.writer(newc)
    termino=''
    for i in valuelist[4]:
        #print(i)
        cont=0
        for j in read:
            if(' '+i+' ' in j.lower()):
                cont=cont+1
                termino=i

        #print(termino, cont)
        if(cont>0):
            conts.writerow([termino, cont])



file='terminos_cuatrecasas.json'
uno=read_terms(file)
labelled(uno) 
cont(uno)

