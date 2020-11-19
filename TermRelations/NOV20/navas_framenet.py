from pprint import pprint
from nltk.corpus import framenet as fn
#print('Number of Frames:', len(fn.frames()))
#print('Number of Lexical Units:', len(fn.lus()))
#print('Number of annotated documents:', len(fn.docs()))


#print('getting frames whose name matches the (case insensitive) regex: "(?i)Committing_crime"')
#medframes = fn.frames(r'(?i)Committing_crime')
#print('Found {0} Frames whose name matches "(?i)Committing_crime":'.format(len(medframes)))
#print([(f.name, f.ID) for f in medframes])



#print((m_frame.lexUnit))
rels = fn.frame_relations(frame='Committing_crime')
childrels = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels):
        childrels.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels):
        childrels.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels):
        childrels.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels):
        childrels.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels):
        childrels.append(f2.Earlier)
#print(childrels)
print('\ncomitting crime')
# Coger hijos recursivamente
for f in childrels:
    #print(f)
    aux = f.name
    print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels):
            childrels.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels):
            childrels.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels):
            childrels.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels):
            childrels.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels):
            childrels.append(f2.Earlier)
print([(f.name) for f in childrels])


unique = childrels






rels = fn.frame_relations(frame='Crime_scenario')
childrels2 = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels2):
        childrels2.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
        childrels2.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
        childrels2.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
        childrels2.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
        childrels2.append(f2.Earlier)

#print(childrels)
print('\nCrime_scenario')
# Coger hijos recursivamente
for f in childrels2:
    #print(f)
    aux = f.name
    #print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels2):
            childrels2.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
            childrels2.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
            childrels2.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
            childrels2.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
            childrels2.append(f2.Earlier)
print([(f.name) for f in childrels2])


unique = unique + childrels2












rels = fn.frame_relations(frame='Law')
childrels2 = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels2):
        childrels2.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
        childrels2.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
        childrels2.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
        childrels2.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
        childrels2.append(f2.Earlier)

#print(childrels)
print('\nLaw')
# Coger hijos recursivamente
for f in childrels2:
    #print(f)
    aux = f.name
    #print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels2):
            childrels2.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
            childrels2.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
            childrels2.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
            childrels2.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
            childrels2.append(f2.Earlier)
print([(f.name) for f in childrels2])


unique = unique + childrels2




rels = fn.frame_relations(frame='Obligation_scenario')
childrels2 = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels2):
        childrels2.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
        childrels2.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
        childrels2.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
        childrels2.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
        childrels2.append(f2.Earlier)

#print(childrels)
print('\nObligation_scenario')
# Coger hijos recursivamente
for f in childrels2:
    #print(f)
    aux = f.name
    #print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels2):
            childrels2.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
            childrels2.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
            childrels2.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
            childrels2.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
            childrels2.append(f2.Earlier)
print([(f.name) for f in childrels2])


unique = unique + childrels2










rels = fn.frame_relations(frame='Misdeed')
childrels2 = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels2):
        childrels2.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
        childrels2.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
        childrels2.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
        childrels2.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
        childrels2.append(f2.Earlier)

#print(childrels)
print('\nMisdeed')
# Coger hijos recursivamente
for f in childrels2:
    #print(f)
    aux = f.name
    #print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels2):
            childrels2.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
            childrels2.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
            childrels2.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
            childrels2.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
            childrels2.append(f2.Earlier)
print([(f.name) for f in childrels2])


unique = unique + childrels2







rels = fn.frame_relations(frame='Law')
childrels2 = []
for f2 in rels:
    #print(f2.keys())
    if ("Child" in f2.keys()) and (f2.Child not in childrels2):
        childrels2.append(f2.Child)
    elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
        childrels2.append(f2.Target)
    elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
        childrels2.append(f2.Component)
    elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
        childrels2.append(f2.Later)
    elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
        childrels2.append(f2.Earlier)

#print(childrels)
print('\nLaw')
# Coger hijos recursivamente
for f in childrels2:
    #print(f)
    aux = f.name
    #print(aux)
    rels2 = fn.frame_relations(frame=aux)

    for f2 in rels2:
        if ("Child" in f2.keys()) and (f2.Child not in childrels2):
            childrels2.append(f2.Child)
        elif ("Target" in f2.keys()) and (f2.Target not in childrels2):
            childrels2.append(f2.Target)
        elif ("Component" in f2.keys()) and (f2.Component not in childrels2):
            childrels2.append(f2.Component)
        elif ("Later" in f2.keys()) and (f2.Later not in childrels2):
            childrels2.append(f2.Later)
        elif ("Earlier" in f2.keys()) and (f2.Earlier not in childrels2):
            childrels2.append(f2.Earlier)
print([(f.name) for f in childrels2])


unique = unique + childrels2
new_list = []
[new_list.append(x) for x in unique if x not in new_list]




print([(f.name) for f in new_list])
lexunits = [(f.lexUnit) for f in new_list]
print(lexunits)

for f in new_list:
    l = f.lexUnit
    print(f.name , "|" , l.keys())
