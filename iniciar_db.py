# -*- coding: utf-8 -*-
from pymongo import MongoClient
from Ruta import Ruta

# Creo una lista de objetos Ruta a insertar en la BD
rutas = [
    Ruta('ruta 1',
        ['frailes', 'santiago londoño','camilo mejia', 'naranjales', 'los rosales','las violetas','los lagos','la pradera',
        'carrera 21','av santa monica','carrera 19 a', 'calle 12', 'carrera 21', 'calle 13', 'carrera 17', 'calle 8', 'la popa',
        'interseccion viaducto', 'puente mosquera', 'av del rio', 'inteseccion turín', 'av 30 de agosto', 'calle 50', 'maraya',
        ' inem', 'parte baja jardin 1', 'av. las americas', 'home center', 'av. de las americas', 'av. el dorado', 'panorama 2',
        'antonio jose valencia', 'bella sardi', 'naranjito', 'altos de las mercedes los critales', '2500 lotes', 'calle 75',
        'carrera 44', 'calle 76', 'carrera 43', 'alejandria', 'navarra', 'montelibano'],
        ['montelibano', 'navarra', 'alejandría', 'carrera 43', 'calle 76','carrera 44', 'calle 75', '2500 lotes', 'los cristales',
        'altos de las mercedes', 'naranjito', 'bella sardi', 'antonio josé valencia', 'panorama 2', 'avda. el dorado',
        'avda. de las américas', 'parte baja jardín 1', 'inem', 'intersección turín', 'av. del rio', 'puente mosquera', 'popa',
        'avda. valher', 'santa mónica', 'carrera 21', 'la pradera', 'los lagos', 'las violetas', 'los rosales', 'camilo mejía', 
        'santiago londoño', 'frailes']),
    Ruta('ruta 2',
        ['remanso', 'tokio', 'las brisas', 'danubio', 'intermedio', 'calle 18 bis este', 'carrera 23',
        'el otoño', 'las margaritas', 'monserrate', 'el pizamo', 'avda. santander', 'cra 11', 'calle 4',
        'cra 12', 'la rebeca', 'avda. circunvalar', 'invico', 'calle 14', 'calle 13', 'carrera 5a ', 'calle 10',
        'carrera 4a', 'puente mosquera', 'la popa', 'la macarena', 'postobón', 'diagonal 26', 'diagonal 25 a',
        'santa isabel transversal 7', 'carrera 7', 'calle 32','av. ferrocarril', 'glorieta postobón',
        'avda. ferrocarril hacia el norte de dosquebradas', 'playa rica'],
        ['playa rica', 'av. ferrocarril', 'calle 32', 'transversal 7', 'santa isabel', 'diagonal 27a', 'transversal 8',
        'diagonal 26','postobón', 'la macarena', 'puente mosquera', 'cra 4', 'calle 14', 'invico', 'avda. circunvalar',
        'parque la rebeca', 'calle 3', 'cra 10', 'avda. santander', 'kennedy', 'pízamo', 'monserrate', 'las margaritas',
        'el otoño', 'carrera 23', 'calle 18 bis este', 'intermedio', 'danubio', 'las brisas', 'tokio', 'el remanso']),
    Ruta('ruta 3a',
        ['variante romelia el pollo', 'guaduales', 'campestre c', 'campestre b', 'limonar', 
        'la macarena', 'avda. el ferrocarril','la popa', 'puente mosquera', 'carrera 4', 'calle 14', 'avda. ferrocarril', 
        'cra 12', 'calle 27', 'avda. belalcazar', 'calle 14', 'terminal de transportes', 'avda. de las américas', 
        'los cedros', 'barrio la playa', 'puente gamma', 'barrio alfa', 'barrio gamma', 'los corales', 
        'avda. de las américas', 'glorieta variante condina', 'urbanización salamanca'],
        ['urbanización salamanca', 'variante condina', 'nuevo sol', 'san marcos', 'san joaquín', 'glorieta corales',
        'av. américas','calle 81', 'carrera 25', 'gamma', 'barrio san fernando', 'la playa', 'avda. de las américas', 
        'los cedros', 'la dulcera', 'vuelta al centro comercial la 14', 'terminal de transportes', 'calle 17', 'invico', 'calle 14',
        'calle 13', 'cra 5a', 'calle 10', 'puente mosquera', 'la popa', 'avda. el ferrocarril'])
    ]


#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db AsistenteRutas
db = mongoClient.AsistenteRutas

# Obtenemos una coleccion para trabajar con ella
collection = db.RutasPereira

# ingresamos los objetos rutas (o documentos en Mongo) en la coleccion RutasPereira
def fill_db():
    for ruta in rutas:
        #convierte el objeto en colección
        collection.insert_one(ruta.toDBCollection())
    

# PASO FINAL: Cerrar la conexion
mongoClient.close()

# TODO Hacer un try catch
"""
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
# 4 parametros
#actualiza la edad de los jugadores mayores de 30, incrementa la edad en 100,
#upsert --> si el campo edad no existe, lo crea
#multi --> para que actualice todos los jugadores mayores de 30 
#collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)



# PASO 4.4: "DELETE" -> Borramos todos las rutas que contengan utp
#collection.remove({"ida": {"$in":["utp"]}})
"""