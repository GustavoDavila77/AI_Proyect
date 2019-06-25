#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from spacy.lang.es.examples import sentences
from spacy_lookup import Entity

nlp = spacy.load('es_core_news_sm')
entity = Entity(keywords_list=['invico', 'victoria', 'montelibano','san luis','san nicolas'])
nlp.add_pipe(entity, last=True) # add this entity al pipeline

#doc = nlp(sentences[0])
doc = nlp('ruta entre Montelibano y Invico')
#print(doc.text)

nouns = dict()

for token in doc:
    print("categorizacion: {} {} {}".format(token.text, token.pos_, token.dep_))# 
    #print(token.is_stop) #para saber si el token es de parada ( words que se repiten mucho )
    if token.pos_ == 'NOUN' or token._.is_entity:
        nouns[token.text] = token.pos_

#print([(token.text, token._.canonical) for token in doc if token._.is_entity]) imprime las palabras que estan dentro de la entidad

print(nouns.keys())
#print(nouns.values())
    #print(token.text, token.pos_, token.dep_)