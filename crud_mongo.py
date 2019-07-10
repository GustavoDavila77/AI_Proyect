# -*- coding: utf-8 -*-
from pymongo import MongoClient
from iniciar_db import fill_db
#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db AsistenteRutas
db = mongoClient.AsistenteRutas

# Obtenemos una coleccion para trabajar con ella
collection = db.RutasPereira

#TODO agregar la busqueda en array vuelta
def buscar_ruta(punto):
    mensaje = 'la ruta que le sirve es '
    result = []
    #print ("\n\n*** Buqueda de los rutas***")
    cursor = collection.find({"ida":{"$in":[punto]}})
    cursor2 = collection.find({"vuelta":{"$in":[punto]}})
    for rut in cursor:
      if rut['nombre'] not in result: #si la ruta no esta, entonces incluyala
        result.append(rut['nombre']) #porque dentro de una ruta se puede encontrar un mismo punto

    for rut in cursor2:
      if rut['nombre'] not in result: #si la ruta no esta, entonces incluyala
        result.append(rut['nombre'])

    if result:
      for i in result:
        mensaje = mensaje + i + ','
    else:
      mensaje = "no se encontró una ruta"
    print(mensaje)
    return mensaje  

#retorna una lista de diccionarios, donde los puntos coiciden
#tanto en ida como en vuelta
def buscar_dos_puntos(punto1,punto2):
  coincidir_ida = dict()
  coincidir_vuelta = dict()
  lista_coincidir = []
  cursor = collection.find({"ida":{"$all":[punto1,punto2]}})
  cursor2 = collection.find({"vuelta":{"$all":[punto1,punto2]}})
  for c in cursor:
    if not c['nombre'] in coincidir_ida: #para que no se vaya a repetir rutas
      coincidir = {}
      coincidir_ida[c['nombre']] = c['ida'] #se añade al diccionario
      coincidir[c['nombre']] = c['ida'] #se crea un diccionario aux
      lista_coincidir.append(coincidir)
  for c in cursor2:
    if not c['nombre'] in coincidir_vuelta: #para que no se vaya a repetir rutas
      coincidir= {}
      coincidir_vuelta[c['nombre']] = c['vuelta']
      coincidir[c['nombre']] = c['vuelta']
      #coincidir_vuelta[c['nombre']] = c['vuelta']
      lista_coincidir.append(coincidir)

  print(coincidir_ida.keys())
  print(coincidir_vuelta.keys())
  return lista_coincidir

def indice_punto_dict(punto, diccionario):
  llave_indice= []
  for clave,lista in diccionario.items():
    for j in range(len(lista)):
      if lista[j] == punto:
        llave_indice= [clave,j] #guardo la ruta y el indice
  return llave_indice
  

#devulve los indices 2 los 2 puntos en los diferentes listas de ida
def two_points(punto1, punto2):
    mensaje = 'la ruta que le sirve es'
    result = []
    lista_dicts = buscar_dos_puntos(punto1,punto2) #lista con diccionarios
    for diccionario in lista_dicts:
      indice_punto1 = indice_punto_dict(punto1,diccionario)
      indice_punto2 = indice_punto_dict(punto2,diccionario)
      
      if indice_punto1 and indice_punto2: #si encontro algo en los dos indices
        print('indice punto 1: '+ str(indice_punto1[1])+'\n'+
              'indice punto 2: '+ str(indice_punto2[1]))
        if indice_punto1[1] < indice_punto2[1]:
          result.append(indice_punto1[0])
        else:
          print('No se encontro una ruta')
      else:
        print("indice no encontrado")

    if result:
      for i in result:
        mensaje = mensaje + i + ','
    else:
      mensaje = "no se encontró una ruta"
    
    print(mensaje)
    return mensaje

def fit_base():
  try:
    fill_db()
    print('datos cargados a la colección')
  except:
    print('erro al cargar datos a la colección')

def delete_base():
  try:
    collection.delete_many({})
    print('Base de datos borrada')
  except:
    print('erro al borrar base')

###### Menu #######
#1. cargar datos
#fit_base()
#2. buscar ruta
#print(buscar_ruta("calle 13"))
#3. borrar base
#delete_base()
#4. two points
#two_points("la popa","calle 13")
#5. dos puntos juntos
#buscar_dos_puntos("calle 13","la popa")


#TODO hacer un menu para la configuración de la base de datos, iniciar base, borrar colección, insertar documento
#collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)
