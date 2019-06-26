#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from spacy.lang.es.examples import sentences
from spacy_lookup import Entity

nlp = spacy.load('es_core_news_sm')
entity = Entity(keywords_list=['invico', 'victoria', 'montelibano','luis','nicolas','utp','dosquebradas'])
nlp.add_pipe(entity, last=True) # add this entity al pipeline

doc = nlp('ruta que me lleve de la utp a dosquebradas')
#doc = nlp('ruta entre san nicolas y san luis')
#print(doc.text)

#nouns = dict() #diccionario para almecenar los sustantivos
recorrido = dict()
for token in doc:
    print("categorizacion: {} {} {}".format(token.text, token.pos_, token.dep_))# 
    #print(token.is_stop) #para saber si el token es de parada ( words que se repiten mucho )
    if token._.is_entity:
        recorrido[token.text] = token.pos_

print(recorrido)
#print(recorrido.keys())
#print(recorrido.values())

#print([(token.text, token._.canonical) for token in doc if token._.is_entity]) imprime las palabras que estan dentro de la entidad

#print(token.text, token.pos_, token.dep_)


############ TODO Para hacer #############
# 1. identificacion de barrios, calles, puntos de la ruta
# 2. numerar el orden en que entraron, esto me va a servir luego para saber si hay una ruta logica
# 3. crear un identificador de sinonimos, para rutas -- podria servir el lematizador(pasar a la palabra originaria)


###### Problems ###########
"""
* el programa tiene problemas cuando hay recorridos que se componen 
por una misma palabra eje: san luis, san nicolas
"""