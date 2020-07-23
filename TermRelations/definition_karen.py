import os
import argparse
import json
import csv
import re
import spacy
import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from time import time
nlp = spacy.load('es_core_news_sm')
from nltk.tokenize import sent_tokenize

def json_file():
	
	return()
def copula_funct(document):
	list_definitions=list()
	definiendums=list()
	
	jsonfile={}
	jsonfile={'palabras':[]}
	print(jsonfile)
	copulas=['es','son','considera', 'consideran', 'reputa','reputan','entiende', 'define','considerará', 'entenderá', 'definirá']
	pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
	sentence=sent_tokenize(document)
	both=list()
	file=open('definitions.txt', 'w')
	new=list()
	for i in range(len(sentence)):
		print('--------------------')
		pattern=list()
		postaglist=list()
		wordlist=list()
		#tokens = nltk.word_tokenize(sentence[i])
		doc=nlp(sentence[i])
		lemlist=[tok.lemma_ for tok in doc]
		tokens=[tok.text for tok in doc]

		#print(lemlist)
		if('considerar' in lemlist):
			cont=lemlist.count('considerar')
			if(cont>1):
				m=[i for i,x in enumerate(lemlist) if x=='considerar']
				poslem=m[0]
				#print(m)

			else:
				poslem=lemlist.index('considerar')
				copula=tokens[poslem]
			

			front=tokens[poslem+1:]
			#print(tokens[poslem],tokens[poslem+1:poslem+2], lemlist[poslem])
			tag=pos_tagger.tag(front)
			for t in tag:
				pattern.append(t)
				postaglist.append(t[1])
				wordlist.append(t[0])
			#print(pattern)
			#print(postaglist)
			#print(tokens)
			if(pattern[0][1]=='VERB' and pattern[1][1]=='DET' and pattern[2][1]=='NOUN' and pattern[3][1]=='PUNCT'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='NOUN' and pattern[1][1]=='ADP' and pattern[2][1]=='NOUN'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			
			elif(pattern[0][1]=='VERB' and pattern[1][1]=='ADP' and pattern[2][1]=='NOUN'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='ADP' and pattern[1][1]=='NOUN' and pattern[2][1]=='ADJ'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)

			elif(pattern[0][1]=='VERB' and pattern[1][1]=='NOUN'):
				definiendum=pattern[0][0]+' '+pattern[1][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='NOUN' and pattern[1][1]=='ADJ'):
				definiendum=pattern[0][0]+' '+pattern[1][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='ADJ' and pattern[1][0]=='la'):
				definiendum=pattern[0][0]+' '+pattern[1][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='ADJ' and pattern[1][1]=='NOUN'):
				definiendum=pattern[0][0]+' '+pattern[1][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='NOUN' and pattern[1][1]=='PUNCT'):
				definiendum=pattern[0][0]+''+pattern[1][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(tokens[0]=='Si'):
				definiendum='Definición condicional'
				definien=' '.join(tokens)
				#print(definiendum,'->', definien)
				jsonfile['palabras'].append({definiendum: definien})
				file.write(definiendum+'-->'+definien+'\n')
			elif('en todo caso' in sentence[i]):
				pos=tokens.index('caso')
				definiendum=' '.join(tokens[:pos-4])
				definien=' '.join(tokens)
				#print(definiendum,'->', definien)
				jsonfile['palabras'].append({definiendum: definien})
				file.write(definiendum+'-->'+definien+'\n')
			else:
				pass
				#print(pattern[0], pattern[1])
				#print(tokens[:pos])
				#print(front)
		elif('entender' in lemlist):
			cont=lemlist.count('entender')
			if(cont>1):
				m=[i for i,x in enumerate(lemlist) if x=='entender']
				poslem=m[0]
				#print(m)

			else:
				poslem=lemlist.index('entender')
				copula=tokens[poslem]
			

			#front=tokens[poslem+1:]
			nextword=tokens[poslem+1]
			if(nextword=='que'):
				#print(tokens[poslem],tokens[poslem+1:poslem+2], lemlist[poslem])
				front=tokens[poslem+2:]
				tag=pos_tagger.tag(front) #([palabra, pos])
				for t in tag:
					pattern.append(t)
					postaglist.append(t[1])
					wordlist.append(t[0])
				
				#print(postaglist)
				if('cuando' in front):
					#cuando |pos  = .split('|') --> cuando 0  pos 1
					#el #1 
					 #trabajo #
					  #es 
					  #nocturno 
					poscuando=front.index('cuando')#[0][0] , [0][1]
					posnoun=postaglist.index('NOUN')
					if(posnoun in [0, 1, 2] ):
						if(postaglist[posnoun+1]=='ADP' and postaglist[posnoun+2]=='DET' and postaglist[posnoun+3]=='NOUN'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]+' '+wordlist[posnoun+3]
							definien=' '.join(front[poscuando:])
							#print(definiendum,'-->', definien)
						elif(postaglist[posnoun+1]=='ADJ'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]
							definien=' '.join(front[poscuando:])
							#print(definiendum,'-->', definien)
						elif(postaglist[posnoun+1]=='AUX' and postaglist[posnoun+2]=='ADJ' ):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]
							definien=' '.join(front[poscuando:])
							#print(definiendum,'-->', definien)
					elif(posnoun in [4] ):
						if(postaglist[posnoun+1]=='ADJ' and postaglist[posnoun+2]=='ADP' and postaglist[posnoun+3]=='NOUN'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]+' '+wordlist[posnoun+3]
							definien=' '.join(front[poscuando:])
							#print(definiendum,'-->', definien)
						

				else:
					if('NOUN' in postaglist):
						posnoun=postaglist.index('NOUN')
						if(postaglist[posnoun+1]=='ADJ'):
								definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]
								definien=' '.join(front)
								#print(definiendum,'-->', definien)
			else:
				back=tokens[:poslem]
				front=tokens[poslem+1:]
				tag=pos_tagger.tag(front)
				for t in tag:
					pattern.append(t)
					postaglist.append(t[1])
					wordlist.append(t[0])

				if('cuando' in front):
					poscuando=front.index('cuando')
					posnoun=postaglist.index('NOUN')
					if(posnoun in [0, 1, 2] ):
						if(postaglist[posnoun+1]=='ADP' and postaglist[posnoun+2]=='DET' and postaglist[posnoun+3]=='NOUN'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]+' '+wordlist[posnoun+3]
							definien=' '.join(front[poscuando:])
							print(definiendum,'-->', definien)
						
						elif(postaglist[posnoun+1]=='AUX' and postaglist[posnoun+2]=='ADJ' ):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]
							definien=' '.join(front[poscuando:])
							print(definiendum,'-->', definien)
						elif(postaglist[posnoun+1]=='ADJ'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]
							definien=' '.join(front[poscuando:])
							print(definiendum,'-->', definien)
					elif(posnoun in [4] ):
						if(postaglist[posnoun+1]=='ADJ' and postaglist[posnoun+2]=='ADP' and postaglist[posnoun+3]=='NOUN'):
							definiendum=wordlist[posnoun]+' '+wordlist[posnoun+1]+' '+wordlist[posnoun+2]+' '+wordlist[posnoun+3]
							definien=' '.join(front[poscuando:])
							print(definiendum,'-->', definien)
					elif(posnoun in [3] ):
						if(postaglist[posnoun+1]=='ADJ' and postaglist[posnoun-3]=='ADV' and postaglist[posnoun-2]=='ADJ' and postaglist[posnoun-1]=='DET'):
							definiendum=wordlist[posnoun-3]+' '+wordlist[posnoun-2]+' '+wordlist[posnoun-1]+' '+wordlist[posnoun]+' '+wordlist[posnoun+1]
							definien=' '.join(front[poscuando:])
							print(definiendum,'-->', definien)
					else:
						print(pattern)
						print(tokens)
				else:
					pass
					#print(pattern)
					#print(tokens)
						
						
			'''if(pattern[0][1]=='SCONJ'):
				pattern.pop(0)
			if(pattern[0][1]=='DET'):
				pattern.pop(0)
			if(pattern[0][1]=='ADP'):
				pattern.pop(0)

			if(pattern[0][1]=='VERB' and pattern[1][1]=='ADP' and pattern[2][1]=='DET' and pattern[3][1]=='NOUN' and pattern[4][1]=='ADJ'):
				
				if(pattern[1][1]=='ADP' and pattern[2][1]=='DET' and pattern[2][0]=='el'):
					cong=pattern[1][0]+'l'
					definiendum=pattern[0][0]+' '+cong+' '+pattern[3][0]+' '+pattern[4][0]
				else:
					definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]+' '+pattern[3][0]+' '+pattern[4][0]
				#print(definiendum)
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='VERB' and pattern[1][1]=='ADP' and pattern[2][1]=='NOUN' and pattern[3][1]=='ADJ'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]+' '+pattern[3][0]
				ind=sentence[i].index(definiendum)
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					
					#print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)
			elif(pattern[0][1]=='NOUN' and pattern[1][1]=='ADP' and pattern[2][1]=='NOUN'):
				definiendum=pattern[0][0]+' '+pattern[1][0]+' '+pattern[2][0]
				ind=sentence[i].index(definiendum)
				if(pattern[3][0]=='se' and pattern[4][1]=='VERB' and 'cuando' in tokens):
					cuando=tokens.index('cuando')
					union=' '.join(tokens[ind+3:cuando])
					definiendum=definiendum+' '+union
				definien0=sentence[i][ind:]
				if('.' in tokens):
					pospunct=front.index('.')
					definien=' '.join(front[:pospunct])
					print(pattern)
					print(definiendum,'->', definien)
					new.append(definien0[pospunct+1:])
					jsonfile['palabras'].append({definiendum: definien})
					file.write(definiendum+'-->'+definien+'\n')
				else:
					print('---->', definien0)'''
				
				
	#print(jsonfile)


	
def pruebas():
	pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
	tag=pos_tagger.tag('tengo que ir Por el contrato de compra y venta uno de los contratantes se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto, en dinero o signo que lo represente'.split(' '))
	doc=nlp('considerará')
	lemlist=[tok.lemma_ for tok in doc]
	print(lemlist)

def pos_tagger_lemma(document, listterms):
	print('Definición por pos tagger y lemma, busqueda de 3,2 y 1 gram')
	text=str()
	definiendums=list()
	pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
	for i in document:
		if(len(i)>1):
			tag=pos_tagger.tag(i.split(' '))
			for t in tag:
				if(t[1]=='VERB'):
					doc=nlp(t[0])
					for tok in doc:
						l=tok.lemma_
						if(l=='ser'):
							text=i
							indverb=i.index(t[0])
							front=i[indverb:]
							back=i[:indverb+len(t[0])+1]
							tagfront=pos_tagger.tag(front.split(' '))
							tagback=pos_tagger.tag(back.split(' '))
							definiendum_definition(t[0], text, listterms)		
							



				elif(t[1]=='NOUN' and t[0]!='=RRB='):
					text=i
					if(len(t[0])>1):
						#definiendum_definition(t[0], text, listterms)
						pass




	return(text)

def punctuation_funct(document, listterms):
	print('Definición por punctuación [:, termino seguido de coma y acabando en coma verbo')
	text=str()
	definiendum=str()
	definiendums=list()
	for i in document:
		for j in listterms:
			term=j[:-1]
			if(len(i)>1):
				if(term+':' in i):
					ind=i.index(':')
					after=i[ind+1:]
					if(len(after)>1 and term not in definiendums):
						definiendum=term
						definition=after
						definiendums.append(definiendum)
						print(definiendum,'---->', definition)

				


				elif(term+',' in i):
					indterm=i.index(term)
					if(',' in i[indterm+len(term):indterm+len(term)+1]):
						#print('-')
						front=i[indterm:-1]
						pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
						tag=pos_tagger.tag(i.split(' '))
						for t in tag:
							if(t[1]=='VERB'):
								#print(front)
								if(t[0] in i):
									#print(t[0])
									indverb=i.index(t[0])
									if(i[indverb-2]==','):
										definiendum=term
										definition=i[indterm+len(term)+1:indverb]
										if(len(definiendum)>1 and len(definition)>1 and definiendum not in definiendums):
											definiendums.append(definiendum)
											print(definiendum,'---->', definition)
										#print( front[:indcoma] )

def definiendum_definition(verb, text, listterms):
	#print('---------------------',verb,'-',text)
	text=text.replace('\n','').replace(',','').replace('.','').replace(':','')
	definiendum=str()
	definition=str()
	definiendums=list()
	gram3=str()
	gram2=str()
	gram1=str()
	tokens=text.split(' ')
	ind=tokens.index(verb)
	gram3=' '.join(tokens[ind-3:ind])
	gram2=' '.join(tokens[ind-2:ind])
	gram1=' '.join(tokens[ind-1:ind])
	#print(verb)
	for i in listterms:
		term=i[:-1]
		if(gram3 == term and gram3 not in definiendums):
			definiendum=gram3
			definition=' '.join(tokens[ind:])
			if(len(tokens[ind:])>1):
				definiendums.append(definiendum)
				print(definiendum,'---->', definition)
		elif(gram2 == term and gram3 not in definiendums):
			definiendum=gram2
			definition=' '.join(tokens[ind:])
			if(len(tokens[ind:])>1):
				definiendums.append(definiendum)
				print(definiendum,'---->', definition)
		elif(gram1 == term and gram1 not in definiendums):
			definiendum=gram1
			definition=' '.join(tokens[ind:])
			if(len(tokens[ind:])>1):
				definiendums.append(definiendum)
				print(definiendum,'---->', definition)

def PVD(document):
	pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
	sentence=sent_tokenize(document)
	word='se'
	lemma='definir'
	for i in range(len(sentence)):
		#print('--------------------')
		pattern=list()
		postaglist=list()
		tokens = nltk.word_tokenize(sentence[i])
		tag=pos_tagger.tag(tokens)
		for t in tag:
			if('se' in tokens):
				pos=tokens.index('se')
				front=tokens[pos+1:pos+2]
				tag=pos_tagger.tag(front)
			
				doc=nlp(t[0])
				lemlist=[tok.lemma_ for tok in doc]
				#lem=''.join(lemlist)
				#lemmas_list.append(lem)
				#print(lemma, '-', lemlist)
				if('definir' in lemlist or 'entender' in lemlist or 'denominar' in lemlist):
					#print(sentence[i])
					front=tokens[pos+2:pos+5]
			if(t[1]=='PUNCT'):
				pos=tokens.index(t[0])
				print(t[0], pos, tag[pos+1])
				

			'''if(t[1]=='AUX'):
				pos1=tokens.index(t[0])
				wordnext=tokens[pos1+1]
				doc1=nlp(wordnext)
				lemlist1=[tok.lemma_ for tok in doc1]
				print(wordnext,'-', lemlist1)
				if('entender' in lemlist1):
					print(sentence[i])'''


					



parser=argparse.ArgumentParser()
parser.add_argument("--document", help="File name  ") #nombre de archivo a leer
parser.add_argument("--terms", help="Source list term to search")
parser.add_argument("--copula", help="Search by copula")
parser.add_argument("--posLemma", help="Search by pos and lemma")
parser.add_argument("--punctuation", help="Search by punctuation")


args=parser.parse_args()

namefile=args.document
fileterm=args.terms
copula=args.copula
posLemma=args.posLemma
punctuation=args.punctuation

#'../data/corpus/estatuto_es.txt'
#'../data/clean_terms_freq4.txt'
file=open(namefile, 'r', encoding='utf-8')
document=file.read()
file2=open(fileterm, 'r', encoding='utf-8')
listterms=file2.readlines()
#PVD(document)
if(copula=='yes'):
	json_file()
	copula_funct(document.replace('\n', ''))
	#pruebas()
if(posLemma=='yes'):
	pos_tagger_lemma(document,listterms)
if(punctuation=='yes'):
	punctuation_funct(document, listterms)

