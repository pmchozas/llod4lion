#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:58:07 2020

@author: pmchozas
"""

import requests
#import stanza
import json


#r = requests.get("https://ixasrl.linkeddata.es/pos?txt=Ella%20come%20patatas")



#ixa_srl = "https://ixasrl.linkeddata.es/srl?"
#ixa_pos = "https://ixasrl.linkeddata.es/pos?"

import requests
#import stanza
import json

termlist=["derecho laboral", "independientemente", "después", "pepino", "contratos vendrán"]
#termlist=["labour law", "now", "later", "contracts will come", "would"]
del_list=[]
lang='es'
for term in termlist:
    pos_list=[]

    params = {'txt':term, 'lang':lang}
    rpos= requests.get("https://ixasrl.linkeddata.es/pos?", params=params)
    rjson=json.loads(rpos.text)
    for token in rjson['annotations']:
        print(token)
        tag=token['pos']
        print(tag)
        if(tag[0] == 'V' and tag[1]=='A'):
            pos_list.append('aux')
        if(tag[0] == 'V' and tag[1]=='M'):
            pos_list.append('verb')
        if(tag[0] == 'N'):
            pos_list.append('noun')
        if(tag[0] == 'P'):
            pos_list.append('pron')
        if(tag[0] == 'R'):
            pos_list.append('adv')
        if(tag[0] == 'T'):
            pos_list.append('art')
        if(tag[0] == 'D'):
            pos_list.append('det')
        if(tag[0] == 'C'):
            pos_list.append('conj')
        if(tag[0] == 'M'):
            pos_list.append('num')
        if(tag[0] == 'A'):
            pos_list.append('adj')
        if(tag[0] == 'I'):
            pos_list.append('int')
        if(tag[0] == 'S'):
            pos_list.append('prep')
        if(tag[0] == 'F'):
            pos_list.append('punt')
        if(tag[0] == 'Y'):
            pos_list.append('abr')
            
    print(pos_list)
    print(len(pos_list))
    
    if len(pos_list) == 1:
        for pos in pos_list:
            if pos=='pron':
                del_list.append(term)
            if pos=='aux':
                del_list.append(term)
            if pos=='adv':
                del_list.append(term)
            if pos=='art':
                del_list.append(term)
            if pos=='det':
                del_list.append(term)
            if pos=='conj':
                del_list.append(term)
            if pos=='num':
                del_list.append(term)
            if pos=='int':
                del_list.append(term)
            if pos=='prep':
                del_list.append(term)
            if pos=='punt':
                del_list.append(term)
            if pos=='abr':
                del_list.append(term)
                
    if len(pos_list)==2:
        if (pos_list[0] == 'aux' and pos_list[1] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'verb' and pos_list[1] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'verb' and pos_list[1] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'aux' and pos_list[1] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'adv' and pos_list[1] == 'adj'):
            del_list.append(term)
        if (pos_list[0] == 'adj' and pos_list[1] == 'adv'):
            del_list.append(term)
        if (pos_list[0] == 'adv' and pos_list[1] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'aux' and pos_list[1] == 'adv'):
            del_list.append(term)    
        if (pos_list[0] == 'aux' and pos_list[1] == 'adj'):
            del_list.append(term)
        if (pos_list[0] == 'adj' and pos_list[1] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'adv' and pos_list[1] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'verb' and pos_list[1] == 'adv'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'adv'):
            del_list.append(term)
        if (pos_list[0] == 'adv' and pos_list[1] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'verb' and pos_list[1] == 'noun'):
            del_list.append(term)
    
    if len(pos_list)==3:
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb' and pos_list[2] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'aux' and pos_list[2] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'aux' and pos_list[2] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb' and pos_list[2] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb' and pos_list[2] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'aux' and pos_list[2] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'verb' and pos_list[1] == 'noun' and pos_list[2] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'noun' and pos_list[2] == 'verb'):
            del_list.append(term)
        if (pos_list[0] == 'aux' and pos_list[1] == 'noun' and pos_list[2] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'noun' and pos_list[2] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'aux' and pos_list[1] == 'verb' and pos_list[2] == 'noun'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb' and pos_list[2] == 'aux'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'verb' and pos_list[2] == 'adj'):
            del_list.append(term)
        if (pos_list[0] == 'noun' and pos_list[1] == 'adj' and pos_list[2] == 'verb'):
            del_list.append(term)
    
print(del_list)
            
        
#print(rpos.url)
'''

def delete_patterns(anotador):
    anotador=["derecho laboral"]
    for term in anotador:
        params = {'txt':term}
        rpos= requests.get("https://ixasrl.linkeddata.es/pos?", params=params)
        rjson=json.loads(rpos.text)
        for token in rjson['annotations']:
            tag=token['pos']
            if(tag[0] == 'V' and tag[1]=='A'):
                list_pos.append('aux--'+str(lem))
						if(len(spl)==1):
							ind=anotador.index(str(i))
							anotador[ind]=str(lem)
					if(t[1] ==  'NNP'):
						list_pos.append('noun-'+str(t[0]))
					if(t[1][:2] ==  'VB'):
						cont_inf=cont_inf+1
						doc=nlp(t[0])
						for tok in doc:
							l=tok.lemma_
							if(l!=t[0]):
								cont_post=cont_post+1
						lemlist=[tok.lemma_ for tok in doc]
						lem=''.join(lemlist)
						lemmas_list.append(lem)
						if(lem==i):
							lem=t[0]
						list_pos.append('verb-'+str(lem))
						if(len(spl)==1):
							ind=anotador.index(str(i))
							anotador[ind]=str(lem)
					if(t[1] ==  'RB'):
						list_pos.append('adv--'+str(t[0]))
					if(t[1] ==  'JJ'):
						list_pos.append('adj--'+str(t[0]))
					if(t[1] ==  'CC'):
						list_pos.append('sconj'+str(t[0]))
				
				spl_i=joini.split(' ')
				
				if(len(list_pos)==1):
					pos1=list_pos[0]
					if(pos1[0:4]=='adv-' ):
						term=pos1[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1

				elif(len(list_pos)==2 and len(spl_i)==2):
					pos1=list_pos[0]
					pos2=list_pos[1]
					term=''
					if(pos1[0:4]=='aux-' and pos2[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adv-' and pos2[0:4]=='adj-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adj-' and pos2[0:4]=='adv-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adv-' and pos2[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='aux-' and pos2[0:4]=='adv-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adv-' and pos2[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='adv-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adv-' and pos2[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='adv-'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='aux-' and pos2[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adj-' and pos2[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1

				elif(len(list_pos)==3 and len(spl_i)==3):
					#print(list_pos, spl_i,'-', len(list_pos), len(spl_i))
					pos1=list_pos[0]
					pos2=list_pos[1]
					pos3=list_pos[2]
					term=''
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb' and pos3[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='aux-' and pos3[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='aux-' and pos3[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb' and pos3[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb' and pos3[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='aux-' and pos3[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='noun' and pos3[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='noun' and pos3[0:4]=='verb'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='aux-' and pos2[0:4]=='noun' and pos3[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='noun' and pos3[0:4]=='aux-'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='aux-' and pos2[0:4]=='verb' and pos3[0:4]=='noun'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb' and pos3[0:4]=='adj-'):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='verb' and pos3[0:4]=='noun' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='noun' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='aux-' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='adv-' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adj-' and pos2[0:4]=='adv-' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='noun' and pos2[0:4]=='adv-' and pos3[0:4]=='scon' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adj-' and pos2[0:4]=='scon' and pos3[0:4]=='adv-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='aux-' and pos2[0:4]=='noun' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='verb' and pos2[0:4]=='verb' and pos3[0:4]=='verb' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1
					if(pos1[0:4]=='adj-' and pos2[0:4]=='noun' and pos3[0:4]=='adj-' and joini in anotador):
						term=pos1[5:]+' '+pos2[5:]+' '+pos3[5:]
						deletes.append(joini)
						ind=anotador.index(joini)
						#anotador.pop(ind)
						cont=cont+1

	for i in deletes:
		if(i in anotador):
			ind=anotador.index(i)
			anotador.pop(ind)
			
	
	#elapsed_time=time()-start_time
	#txt='PATRONES, DELETE'+' ('+str(cont)+') NEW LIST SIZE: ('+str(len(anotador))+') TIME: ('+str(elapsed_time)+')'
	joind=', '.join(deletes)
	#print('PATRONES DELETE', cont, len(anotador), elapsed_time)
	#conts_log.information(txt, 'TERMS REMOVED: '+joind)
	return(anotador)
'''

