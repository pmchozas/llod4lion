# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:45:08 2019
 @author: Sina Ahmadi - Patricia Martín Chozas  .

"""
import requests
from random import randint
import os
import requests
import json
import time

# header for Wikidata queries
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# =========================================
# SKOS template
# =========================================
prefixes_templates = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix iso639: <http://lexvo.org/id/iso639-1/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.
@prefix : <#> .
"""
concept_template = """
    <http://lkg.lynx-project.eu/kos/labourlaw_terms/SCTMID> a skos:Concept ;
        skos:closeMatch <https://www.wikidata.org/wiki/WDTMID> ;
        skos:prefLabel "CONCAT"@LANG ;"""

desc_template = """
        skos:description CONCAT1;
"""

alt_template = """
        skos:altLabel "CONCAT2"@LANG ;
"""

br_template = """        skos:broader WDBRTMID ; 
"""

naTerm_template = """        skos:narrower WDNRTMID ;
"""
re_template = """
        skos:related <https://www.wikidata.org/wiki/WDRLTMID>; 
"""

brconcept_temp = """
    <http://lkg.lynx-project.eu/kos/labourlaw/LTBRTMID> a skos:Concept .
    skos:exactMatch <https://www.wikidata.org/wiki/WDBRTMID> .
"""

brconceptlab_temp = """
        skos:prefLabel CONCAT3 ;
"""

nrconcept_temp = """
    <http://lkg.lynx-project.eu/kos/labourlaw/LTNRTMID> a skos:Concept .
        skos:exactMatch <https://www.wikidata.org/wiki/WDNRTMID> .
"""
nrconceptlab_temp = """
        skos:prefLabel CONCAT4 ;
"""

reconcept_temp = """
    <http://lkg.lynx-project.eu/kos/labourlaw/LTRLTMID> a skos:Concept .
        skos:exactMatch <https://www.wikidata.org/wiki/WDRLTMID> .
"""
reconceptlab_temp = """
        skos:prefLabel CONCAT5 ;
"""
# =========================================
# Clean text by removing noisy characters
# =========================================
def clean_text(text):
    return text.replace("\n", "")
# =========================================
# Creation of numeric ID for source terms
# =========================================
def sctmid_creator():
    numb = randint(1000000, 9999999)

    SCTMID = "LT" + str(numb)
    return SCTMID
# =========================================
# 
# =========================================
def get_conceptNet_synonyms(term, lang="en"):
    # Given a term, get the synonyms from ConcetpNet of the same language
    # Note that all words are in lower case on ConceptNet, unlike Wikidata
    # Start and end edges should be taken into account
    synonyms = list()
    query_url_pattern = "http://api.conceptnet.io/query?EDGEDIRECTION=/c/LANG/TERM&rel=/r/Synonym&limit=1000"
    
    edge_directions = {"start":"end", "end":"start"}
    for direction in edge_directions.keys():
        query_url = query_url_pattern.replace("EDGEDIRECTION", direction).replace("LANG", lang).replace("TERM", term)
        # print(query_url)
        obj = requests.get(query_url).json()
        for edge_index in range(len(obj['edges'])):
            syn_lang = obj['edges'][edge_index][edge_directions[direction]]["language"]
            if syn_lang == lang:
                synonyms.append(obj['edges'][edge_index][edge_directions[direction]]["label"])
    return list(set(synonyms))

def inducer(T, A, S):
    # Gets T, the list of preferred labels and A, the list of alternative labels
    # Using synonyms of T, S, it induces the semantic relationship that exists between T and A. 
    # S is a dictionary of word as term and dictionary {lang: synonyms} as values.
    semantic_relationship = None
    
    if len(A) and len(T):
        invalid = False


        if " ".join(A).lower() == " ".join(T).lower():
            # They are identical. No semantic relationship should be induced. 
            pass
        
        elif len(T) == len(A):
            case_check = list()
            for t in T:
                if t in A:
                    case_check.append(True)
                else:
                    # check if the language exists
                    if len(S[t]):
                        if True in [True for s_t in S[t] if s_t in A]:
                            case_check.append(True)
                        else:
                            case_check.append(False)
                    else:
                        invalid = True

            if case_check.count(True) < len(T):
                semantic_relationship = "related"
            if not invalid and False not in case_check: 
                semantic_relationship = "synonymy"

        elif len(T) < len(A):
            case_check = list()
            for t in T:
                if t in A:
                    case_check.append(True)
                else:
                    # check if the language exists
                    if len(S[t]):
                        if True in [True for s_t in S[t] if s_t in A]:
                            case_check.append(True)
                        else:
                            case_check.append(False)
                    else:
                        case_check.append(False)

            # print(case_check)
            if False not in case_check:
                semantic_relationship = "narrower"

        elif len(T) > len(A):
            case_check = True
            for a in A:
                # Find all the synonyms of the existing terms
                syns = list()
                for term_syn in S.values():
                    if len(term_syn):
                        syns = syns + term_syn
                    else:
                        pass

                syns = list(set(syns))
                if len(syns):
                    if not (a in T or True in [True for s_t in syns if a in s_t]):
                        case_check = False
                else:
                    invalid = True

            if not invalid and case_check:
                semantic_relationship = "broader"

        else:
            pass

    return semantic_relationship
# =========================================
# Extract multiLabel
# =========================================
def extract_multiLabel(labels, key):
    # Given a list of dictionaries where similar keys may exist, 
    # converge all those values belonging to the same key to a list and
    # create a new dictionary where the keys are unique and multiple values exist as a list {article_URL:[altLabel, ...]}
    # altLabel or naTerm
    multiLabels = dict()
    for item in labels['results']['bindings']:
        article = item['article']['value']
        if key in item.keys():
            label = item[key]['value']
        else:
            label = ""
        if article not in multiLabels:
            multiLabels[article] = [label]
        else:
            multiLabels[article].append(label)
    return multiLabels
# =========================================
# Retrieving from Wikidata
# =========================================
def wikidata_retriever(term, subjects, lang):
    url = 'https://query.wikidata.org/sparql'
    retrieve_query = """
      SELECT * {
       ?item rdfs:label "TERM"@LANG.
      }
    """

    class_checker = """
      ask {
        wd:WDTMID (wdt:P361|wdt:P279|wdt:P31)+ wd:SUBJECT .
      }
    """

    original_query = """
    SELECT DISTINCT ?article ?lang ?name ?desc WHERE {
      ?article schema:about wd:WDTMID;
               schema:inLanguage ?lang;
               schema:name ?name.
      FILTER(?lang in ('es', 'de', 'nl', 'en'))  
      OPTIONAL {
        wd:WDTMID schema:description ?desc.
        FILTER (lang(?name) = lang(?desc))
      }
    }ORDER BY ?lang
    """

    altLabel_query = """
    SELECT DISTINCT ?article ?altLabel WHERE {
      ?article schema:about wd:WDTMID;
               schema:inLanguage ?lang;
               schema:name ?name.
      FILTER(?lang in ('es', 'de', 'nl', 'en'))  
      OPTIONAL {
        wd:WDTMID skos:altLabel ?altLabel.
        FILTER (lang(?name) = lang(?altLabel))
      }
    }ORDER BY ?lang
    """

    narrower_concept_query = """
    SELECT DISTINCT ?naTerm WHERE {
        ?naTerm wdt:P279 wd:WDTMID .
      }
    """

    broader_concept_query = """
    SELECT DISTINCT ?brTerm WHERE {
        wd:WDTMID wdt:P279 ?brTerm .   
    }
    """

    term_query = """
    SELECT DISTINCT ?lang ?name WHERE {
      ?article schema:about wd:WDTMID;
               schema:inLanguage ?lang;
               schema:name ?name.
      FILTER(?lang in ('es', 'de', 'nl', 'en'))  
    }ORDER BY ?lang
    """

    Wikidata_dataset = dict()
    
    print(term)
    query = retrieve_query.replace("TERM", term).replace("LANG", lang)
    SRCTERM = "\"" + term + "\"" + "@" + lang
    #print(SRCTERM) We have to save this in the skos as well
    r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
    data = r.json()

    if len(data['results']['bindings']) != 0:
        item_id = data['results']['bindings'][0]['item']['value'].split("/")[-1]

        retrieved_subject = ""
        for subject in subjects:
            query = class_checker.replace("WDTMID", item_id).replace("SUBJECT", subjects[subject])
            r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
            data = r.json()
            if data['boolean'] == True:
                retrieved_subject = subject
                # Quit the loop if a subject found (better performance)
                break

        if len(retrieved_subject):
            query = original_query.replace("WDTMID", item_id)
            r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
            data = r.json()
            # print(data)

            # Alternative labels
            query = altLabel_query.replace("WDTMID", item_id)
            r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
            altLabel_response = r.json()
            altLabel_dict = extract_multiLabel(altLabel_response, "altLabel")

            # Retrieve narrower and broader concepts
            relation_type = ["narrower", "broader"]
            relations_retrieved = dict()
            for relation in relation_type:
                if relation == "narrower":
                    concept_query = narrower_concept_query
                    relation_id = "naTerm"
                else:
                    concept_query = broader_concept_query
                    relation_id = "brTerm"

                query = concept_query.replace("WDTMID", item_id)
                r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
                concept_response = r.json()
                # extract concepts and get its id (the URL is returned by default)
                concepts_list = [item[relation_id]["value"].split("/")[-1] if len(item[relation_id]["value"]) else None for item in concept_response["results"]["bindings"]]
                
                # Retrieve terms of the concepts
                concepts_dict = dict()
                if len(concepts_list):
                    for concept in concepts_list:
                        concept_terms = dict()
                        query = term_query.replace("WDTMID", concept)
                        r = requests.get(url, params={'format': 'json', 'query': query}, headers=headers)
                        for item in r.json()["results"]["bindings"]:
                            concept_terms[item["lang"]["value"]] = item["name"]["value"]
                        concepts_dict[concept] = concept_terms
                else:
                    concepts_dict = {}

                relations_retrieved[relation] = concepts_dict

            # Extract data
            retrieved = list()
            for item in data['results']['bindings']:
                # ignore articles describing a category 
                article = item['article']['value']
                if article.count(":") == 1:
                    lang = item['lang']['value']
                    name = item['name']['value']
                    altL, naTeL, brTeL = "", "", ""
                    if "desc" in item.keys():
                        desc = item['desc']['value']
                    else:
                        desc = ""
                    if article in altLabel_dict.keys():
                        altL = altLabel_dict[article]

                    retrieved.append({"article": article, "lang": lang, "name": name, "desc": desc, "altLabel": altL})

            subj = {"value": retrieved_subject, "id": subjects[retrieved_subject]}
            retrieved_data = {"Term": term, "WDTMID": item_id, "SBJCT": subj, "naTerm": relations_retrieved["narrower"], "brTerm": relations_retrieved["broader"], "translations": retrieved}
        else:
            retrieved_data = {}
    else:
        retrieved_data = {}

    return retrieved_data
# =========================================
# Creation of SKOS model with the collected Wikidata_dataset
# he quitado el zip. no faltaría un return?  naTerm_lang
# =========================================
def skos_converter_Wiki(entry, wiki_data):
    name_lang, desc_lang, altLabel_lang, narrower_terms, broader_terms = list(), list(), list(), list(), list()
    translations = wiki_data["translations"]
    for i in translations:
        name_lang.append( "\"" + i["name"] + "\"" + "@" + i["lang"] )
        if i["desc"]:
            dl = "\"" + i["desc"] + "\"" + "@" + i["lang"]
            if dl not in desc_lang:
                desc_lang.append(dl)

        if i["altLabel"]:
            for lbl in i["altLabel"]:
                if len(lbl):
                    ll = "\"" + lbl + "\"" + "@" + i["lang"]
                    if ll not in altLabel_lang:
                        altLabel_lang.append(ll)

        if i["naTerm"]:
            for ntrm in i["naTerm"]:
                ntrm = "<" + ntrm + ">"
                if len(ntrm) and ntrm not in narrower_terms:
                        narrower_terms.append(ntrm)

        if i["brTerm"]:
            for btrm in i["brTerm"]:
                btrm = "<" + btrm + ">"
                if len(btrm) and btrm not in broader_terms:
                        broader_terms.append(btrm)

    header = concept_template.replace("CONCAT", ", ".join(name_lang)).replace("WDTMID", 
        wiki_data["WDTMID"]).replace("SCTMID", TERM_ID_MAP[entry])

    if ", ".join(desc_lang):
        body = desc_template.replace("CONCAT1", ", ".join(desc_lang))
    else:
        body = ""

    if ", ".join(altLabel_lang):
        alternative_labels = alt_template.replace("CONCAT2", ", ".join(altLabel_lang))
    else:
        alternative_labels = ""

    # remove empty elements (NEXT STEP)
    if ", ".join(narrower_terms):
        narrower_concepts = naTerm_template.replace("WDNRTMID", ", ".join(narrower_terms))
    else:
        narrower_concepts = ""

    if ", ".join(broader_terms):
        broader_concepts = br_template.replace("WDBRTMID", ", ".join(broader_terms))
    else:
        broader_concepts = ""

    return str(header + body + alternative_labels + narrower_concepts + broader_concepts)[:-3] + "."

# Conversion of the goldstandard file
def skos_converter(entry):
    SKOS_triples = ""
    if entry["T"] not in TERM_ID_MAP:
        TERM_ID_MAP[entry["T"]] = sctmid_creator()
    SKOS_triples += concept_template.replace("SCTMID", TERM_ID_MAP[entry["T"]]).replace("CONCAT", entry["T"])

    alt_labels, broader_labels, narrower_labels = list(), list(), list()
    for k in entry["S"]:
        alt_labels = alt_labels + entry["S"][k]

    for k in entry["A"]:
        if entry["A"][k] == "related":
            alt_labels.append(k)
        elif entry["A"][k] == "narrower":
            narrower_labels.append(k)
        elif entry["A"][k] == "broader":
            broader_labels.append(k)

    alt_labels = "\"" +  "\", \"".join( list(set(alt_labels)) ) + "\""
    narrower_labels = "\"" + "\", \"".join( list(set(narrower_labels)) ) + "\""
    broader_labels = "\"" + "\", \"".join( list(set(broader_labels)) ) + "\""
    
    SKOS_triples += alt_template.replace("CONCAT2", alt_labels)
    SKOS_triples += naTerm_template.replace("WDNRTMID", narrower_labels)
    SKOS_triples += br_template.replace("WDBRTMID", broader_labels)
    return SKOS_triples.replace("LANG", entry["lang"]).replace("        skos:broader \"\" ; ", "")

# =========================================
# main
# =========================================
# Read the configuration file
print("============ Reading the configuration file")
with open("configuration.json", 'r') as f:
    configuration = json.load(f)

term_id_file_dir = 'IDs/scterm_dict_%s.csv'%configuration["run_id"]
wikidata_output_file_name = "Wikidata/%s.json"%configuration["run_id"]
not_found_file_name = "Log/not_found_%s.txt"%configuration["run_id"]
induction_dir = "Induction/%s.json"%configuration["run_id"]
filtered_output_dir = "Output/%s.json"%configuration["run_id"]
evaluation_results_dir = "Evaluation/%s.txt"%configuration["run_id"]

source_file = open(configuration["source_file_dir"], "r")
terms = [t for t in source_file.read().split("\n")]
# print(terms)

TERM_ID_MAP = dict()
# Check if ID-term file exists
if os.path.isfile(term_id_file_dir):
    id_term = open(term_id_file_dir,'r').read().split("\n")
    TERM_ID_MAP = {t.split(", ")[0]: t.split(", ")[1] if len(t) else None for t in id_term}
# otherwise create a new one
else:
    a = open(term_id_file_dir,'w+')
    for t in terms:
        TERM_ID_MAP[t] = sctmid_creator()
        a.write(t+ ', '+ TERM_ID_MAP[t] + '\n')
    a.close()
# ================
if configuration["retrieve_wikidata"]:
    print("====== Retrieving data from Wikidata:")
    # Read subjects JSON file
    with open(configuration["gold_concepts_dir"], 'r') as f:
        subjects = json.load(f)

    not_found = list()
    save_as_json = True
    save_as_triples = False

    if save_as_triples:
        # Creating the output file and writing the prefixes
        with open(wikidata_output_file_name, "a") as output_file:
            output_file.write(prefixes_templates)
            output_file.write("\n\n")

        for entry in terms:
            retrieved_data = wikidata_retriever(entry, subjects, lang=configuration["source_language"][0:2])
            if len(retrieved_data):
                skos_text = skos_converter(entry, retrieved_data)
                with open(wikidata_output_file_name, "a") as output_file:
                  output_file.write(skos_text)
                  output_file.write("\n\n")
            else:
                not_found.append(entry)

    if save_as_json:
        retrieved_data = list()
        for entry in terms:
            entry_retrieved_data = wikidata_retriever(entry, subjects, lang=configuration["source_language"][0:2])
            if len(entry_retrieved_data):
                retrieved_data.append(entry_retrieved_data)
            else:
                not_found.append(entry)

        # print(json.dumps(retrieved_data, indent=4, sort_keys=True))

        with open(wikidata_output_file_name, 'w') as f:
            json.dump(retrieved_data, f)

    # # Writing those words which could not be found
    with open(not_found_file_name, "w") as output_file:
        output_file.write("\n".join(not_found))
# ================
if configuration["retrieve_ConceptNet"]:
    print("====== Retrieving data from ConceptNet:")
    with open(wikidata_output_file_name, 'r') as f:
        retrieved_wikidata = json.load(f)

    all_inductions = list()
    for item in retrieved_wikidata:
        induced_relationships = list()
        for trans in item["translations"]:
            altLabel_induction = dict()
            print(trans["name"].lower())
            T = trans["name"].lower().split()
            lang = trans["lang"]
            S = dict()
            for t in T:
                if t not in S:
                    S[t] = get_conceptNet_synonyms(t, lang)
            # S = get_conceptNet_synonyms(T.replace(" ", "_"), lang)
            # print("T:", T, "lang:", lang, "S:", S)
            if len(S):
                for altLabel in trans["altLabel"]:
                    A = altLabel.lower().split()
                    if len(A):
                        # Go for axiom induction
                        T_A_relationship = inducer(T, A, S)
                        altLabel_induction[" ".join(A)] = T_A_relationship
                        # print("A:", A, "SR:", T_A_relationship)
            else:
                # No synonyms found on ConceptNet"
                altLabel_induction = {}
            
            induced_relationships.append({"T":" ".join(T), "lang": lang, "S": S, "A": altLabel_induction})
            # Not to get timeout from ConceptNet API
            time.sleep(2)
        all_inductions.append(induced_relationships)
    
    print("==== Saving induced data.")
    with open(induction_dir, "w") as f:
        json.dump(all_inductions, f)
    # print(json.dumps(all_inductions, indent=4, sort_keys=True))
    # for trans in example["translations"]:
    #     for key, value in trans.items():
    #         print(key, value)
    # print(example.keys())
    # synonyms = get_conceptNet_synonyms("en", "discrimination")
    # print(synonyms)

# Analysis
if configuration["analysis"]:
    print("====== Analysing valid outputs")
    with open(induction_dir, 'r') as f:
        retrieved_wikidata = json.load(f)

    item_empty = 0
    all_trans, all_valids, A_empty, S_all_empty = 0, 0, 0, 0
    valid_items = list()
    for item in retrieved_wikidata:
        item_valid = True

        if not len(item):
            item_empty += 1
            item_valid = False
        else:
            for trans in item:
                all_trans += 1
                if not len(trans["A"]):
                    item_valid = False
                    A_empty += 1
                
                S_is_empty = True
                for s in list(trans["S"].values()):
                    if len(s):
                        S_is_empty = False
                if S_is_empty:
                    item_valid = False
                    S_all_empty += 1

        if item_valid:
            all_valids += len(item)
            valid_items.append(item)

    print("All translations", all_trans)
    print("Empty items:", item_empty)
    print("Empty A:", A_empty)
    print("Empty S:", S_all_empty)
    print("All valids:", all_valids)

    with open(filtered_output_dir, "w") as f:
        json.dump(valid_items, f)


# Comparison of the gold-standard with the output of the script
# and also I'd like to know which of the "wrong" matches (A) contain a token that is not present within the list of synonyms (S)

if configuration["evaluate"]:
    print("====== Evaluating the performance")
    with open(filtered_output_dir, 'r') as f:
        retrieved_wikidata = json.load(f)
    with open(configuration["gold_concepts_dir"], 'r') as f:
        goldstandard = json.load(f)

    correct_predictions = dict()
    all_pred = dict()
    missing_synonym = dict()

    results = "T \t A \t Prediction \t Gold-standard"
    for item_ind in range(len(retrieved_wikidata)):
        for trans_ind in range(len(retrieved_wikidata[item_ind])):
            A_re = retrieved_wikidata[item_ind][trans_ind]["A"]
            A_gold = goldstandard[item_ind][trans_ind]["A"]
            T = retrieved_wikidata[item_ind][trans_ind]["T"]
            lang = retrieved_wikidata[item_ind][trans_ind]["lang"]
            for a in A_re:
                if lang not in all_pred:
                    all_pred[lang] = 1
                else:
                    all_pred[lang] += 1
                if A_re[a] == A_gold[a]:
                    if lang not in correct_predictions:
                        correct_predictions[lang] = 1
                    else:
                        correct_predictions[lang] += 1
                    # correct_predictions += 1
                    results = results + "\n" + T + "\t" +  a + "\t" + str(A_re[a])
                else:
                    # count "wrong" matches (A) containing a token that is not present within the list of synonyms (S)
                    S = retrieved_wikidata[item_ind][trans_ind]["S"]
                    S_values = list()
                    for s in S.values():
                        for ss in s:
                            S_values.append(ss)

                    for token in a.split():
                        if token not in S_values:
                            if lang not in missing_synonym:
                                missing_synonym[lang] = 1
                            else:
                                missing_synonym[lang] += 1
                            break

                results = results + "\n" + T + "\t" + a + "\t" + str(A_re[a]) + "\t" + str(A_gold[a])

    accuracy = dict()
    for lang in all_pred:
        accuracy[lang] = correct_predictions[lang]*100 / all_pred[lang]
    sum_acc = 0
    for acc in accuracy.values():
        sum_acc += acc
    accuracy["all"] = sum_acc / 4

    results += "\n" + "-"*50
    results += "\n All: " + json.dumps(all_pred)
    results += "\n Correct: " + json.dumps(correct_predictions)
    results += "\n Missing: " + json.dumps(missing_synonym)
    results += "\n Accuracy: " + json.dumps(accuracy)

    print("=== Saving evaluation results.")
    with open(evaluation_results_dir, "w") as f:
        f.write(results)



print("============ Finished.")
# Induction test
# lang = "en"
# T = "employment agreement".split()


# print("T:", T, "S: ", S)
# T = "bank holiday".split()
# A = "bank holiday".split()
# S = {}
# # print("A:", A)
# print(inducer(T, A, S))

# A = "rental contract".split()
# print("A:", A)
# print(inducer(T, A, S))

# A = "temporary work contract".split()
# print("A:", A)
# print(inducer(T, A, S))

# A = "contract".split()
# print("A:", A)
# print(inducer(T, A, S))

# ================
# Ignore category
# Remove duplicates




