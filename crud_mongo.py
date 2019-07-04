# -*- coding: utf-8 -*-
from pymongo import MongoClient

#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db AsistenteRutas
db = mongoClient.AsistenteRutas

# Obtenemos una coleccion para trabajar con ella
collection = db.RutasPereira

# "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()

def buscar_ruta(punto):
    print ("\n\n*** Buqueda de los rutas***")
    cursor = collection.find({"ida":{"$in":[punto]}})
    for rut in cursor:
        print ("%s - %s" \
          %(rut['nombre'], rut['ida']))