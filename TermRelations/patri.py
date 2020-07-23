import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

textpatri = 'siempre que convivan con el empresario , el cónyuge , los descendientes , ascendientes y demás parientes por consanguinidad o afinidad , hasta el segundo grado inclusive y , en su caso , por adopción.f ) La actividad de las personas que intervengan en operaciones mercantiles por cuenta de uno o más empresarios , siempre que queden personalmente obligados a responder del buen fin de la operación asumiendo el riesgo y ventura de la misma.g ) En general , todo trabajo que se efectúe en desarrollo de relación distinta de la que define el apartado 1.A tales efectos se entenderá excluida del ámbito laboral la actividad de las personas prestadoras del servicio de transporte al amparo de autorizaciones administrativas de las que sean titulares , realizada , mediante el correspondiente precio , con vehículos comerciales de servicio público cuya propiedad o poder directo de disposición ostenten , aun cuando dichos servicios se realicen de forma continuada para un mismo cargador o comercializador. cargador o comercializador'
pos_tagger = CoreNLPParser('http://localhost:9003', tagtype='pos')
pattern = list()
postaglist = list()
wordlist = list()
tag = pos_tagger.tag(textpatri.split(' '))
file=open('postaglist.txt', 'r', encoding='utf-8')
document=file.readlines()
file1=open('wordlist.txt', 'r', encoding='utf-8')
document1=file1.readlines()
for t in range(len(document)):
	#pattern.append(t)
	postaglist.append(document[t][:-1])
	wordlist.append(document1[t][:-1])

#noun verb noun
for i in range(len(postaglist)):
    if('NOUN' == postaglist[i]):
        posnoun=i
        newword=wordlist[posnoun]
        #print( '->',newword)
        if(posnoun+3<len(postaglist)):
            verbrange=postaglist[posnoun:posnoun+5]
            #
            #print('verbrange',verbrange)
            for pos in range(len(verbrange)):
	            if('VERB' ==verbrange[pos]):
	                posverb=posnoun+pos
	                newword+=' '+wordlist[posverb]
	                #print('-->',newword)
	                nounrange=postaglist[posverb:posverb+5]
	                #print('nounrange-',nounrange)
	                for pos1 in range(len(nounrange)):
	                	if('NOUN' ==nounrange[pos1]):
	                		posnoun2=posverb+pos1
	                		newword+=' '+wordlist[posnoun2]
	                		print('--->',newword)

	               

