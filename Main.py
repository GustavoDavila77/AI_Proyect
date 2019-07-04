# -*- coding: utf-8 -*-
from pymongo import MongoClient
from Ruta import Ruta

# Creo una lista de objetos futbolista a insertar en la BD
rutas = [
    Ruta('ruta1',['victoria', 'libertad','luis', 'jardin', 'utp']),
    Ruta('ruta2',['nicolas', 'terminal','jardin', 'utp'])
]


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.AsistenteRutas

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db.RutasPereira


# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista
for ruta in rutas:
    #convierte el objeto en colección
    collection.insert_one(ruta.toDBCollection()) 

# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()

for rut in cursor:
    print ("%s - %s" \
          %(rut['nombre'], rut['ida']))

# PASO 4.2.2: "READ" -> Hacemos una Query con condiciones y lo pasamos a un objeto Futbolista
print ("\n\n*** Buqueda de los rutas que contengan terminal ***")
cursor = collection.find({"ida":{"$in":["terminal"]}})
for fut in cursor:
    print ("%s - %s" \
          %(fut['nombre'], fut['ida']))

# PASO 4.3: "UPDATE" -> Actualizamos la edad de los jugadores.
#collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)



# PASO 4.4: "DELETE" -> Borramos todos las rutas que contengan utp
#collection.remove({"ida": {"$in":["utp"]}})


# PASO FINAL: Cerrar la conexion
mongoClient.close()
