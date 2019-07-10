# -*- coding: utf-8 -*-
from pymongo import MongoClient
from Ruta import Ruta

# Creo una lista de objetos Ruta a insertar en la BD
rutas = [
    Ruta('ruta 1',
        ['frailes', 'santiago londoño','camilo mejia', 'naranjales', 'los rosales','las violetas','los lagos','la pradera',
        'carrera 21','av santa monica','carrera 19 a', 'calle 12', 'carrera 21', 'calle 13', 'carrera 17', 'calle 8', 'la popa',
        'interseccion viaducto', 'puente mosquera', 'av del rio', 'inteseccion turín', 'av 30 de agosto', 'calle 50', 'maraya',
        'inem', 'parte baja jardin 1', 'av. las americas', 'home center', 'av. las americas', 'av. el dorado', 'panorama 2',
        'antonio jose valencia', 'bella sardi', 'naranjito', 'altos de las mercedes','los cristales', '2500 lotes', 'calle 75',
        'carrera 44', 'calle 76', 'carrera 43', 'alejandria', 'navarra', 'montelibano'],
        ['montelibano', 'navarra', 'alejandría', 'carrera 43', 'calle 76','carrera 44', 'calle 75', '2500 lotes', 'los cristales',
        'altos de las mercedes', 'naranjito', 'bella sardi', 'antonio josé valencia', 'panorama 2', 'avda. el dorado',
        'av. las americas', 'parte baja jardín 1', 'inem', 'intersección turín', 'av. del rio', 'puente mosquera', 'la popa',
        'avda. valher', 'santa mónica', 'carrera 21', 'la pradera', 'los lagos', 'las violetas', 'los rosales', 'camilo mejía', 
        'santiago londoño', 'frailes']),
    Ruta('ruta 2',
        ['remanso', 'tokio', 'las brisas', 'danubio', 'intermedio', 'calle 18 bis este', 'carrera 23',
        'el otoño', 'las margaritas', 'monserrate', 'el pizamo', 'avda. santander', 'cra 11', 'calle 4',
        'cra 12', 'la rebeca', 'avda. circunvalar', 'invico', 'calle 14', 'calle 13', 'carrera 5a', 'calle 10',
        'carrera 4a', 'puente mosquera', 'la popa', 'la macarena', 'postobón', 'diagonal 26', 'diagonal 25 a',
        'santa isabel transversal 7', 'carrera 7', 'calle 32','av. ferrocarril', 'glorieta postobón',
        'av. ferrocarril hacia el norte de dosquebradas', 'playa rica'],
        ['playa rica', 'av. ferrocarril', 'calle 32', 'transversal 7', 'santa isabel', 'diagonal 27a', 'transversal 8',
        'diagonal 26','postobón', 'la macarena', 'puente mosquera', 'cra 4', 'calle 14', 'invico', 'avda. circunvalar',
        'parque la rebeca', 'calle 3', 'cra 10', 'avda. santander', 'kennedy', 'pízamo', 'monserrate', 'las margaritas',
        'el otoño', 'carrera 23', 'calle 18 bis este', 'intermedio', 'danubio', 'las brisas', 'tokio', 'el remanso']),
    Ruta('ruta 3a',
        ['variante romelia el pollo', 'guaduales', 'campestre c', 'campestre b', 'limonar', 
        'la macarena', 'av. ferrocarril','la popa', 'puente mosquera', 'carrera 4', 'calle 14', 'av. ferrocarril', 
        'cra 12', 'calle 27', 'avda. belalcazar', 'calle 14', 'terminal de transportes', 'av. las americas', 
        'los cedros', 'barrio la playa', 'puente gamma', 'barrio alfa', 'barrio gamma', 'los corales', 
        'av. las americas', 'glorieta variante condina', 'urbanizacion salamanca'],
        ['urbanización salamanca', 'variante condina', 'nuevo sol', 'san marcos', 'san joaquin', 'glorieta corales',
        'av. américas','calle 81', 'carrera 25', 'barrio gamma', 'barrio san fernando', 'la playa', 'av. las americas', 
        'los cedros', 'la dulcera', 'vuelta al centro comercial la 14', 'terminal de transportes', 'calle 17', 'invico', 'calle 14',
        'calle 13', 'cra 5a', 'calle 10', 'puente mosquera', 'la popa', 'av. ferrocarril'])
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


