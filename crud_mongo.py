# -*- coding: utf-8 -*-
from pymongo import MongoClient
from iniciar_db import fill_db
#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db AsistenteRutas
db = mongoClient.AsistenteRutas

# Obtenemos una coleccion para trabajar con ella
collection = db.RutasPereira

# colección donde estan los puntos sin repetir
#collection = db.NoRepeat

# "READ" -> Leemos todos los documentos de la base de datos
#cursor = collection.find()

#TODO agregar la busqueda en array vuelta
def buscar_ruta(punto):
    result = []
    print ("\n\n*** Buqueda de los rutas***")
    cursor = collection.find({"ida":{"$in":[punto]}})
    cursor2 = collection.find({"vuelta":{"$in":[punto]}})
    for rut in cursor:
      if rut['nombre'] not in result: #si la ruta no esta, entonces incluyala
        result.append(rut['nombre']) #porque dentro de una ruta se puede encontrar un mismo punto

    for rut in cursor2:
      if rut['nombre'] not in result: #si la ruta no esta, entonces incluyala
        result.append(rut['nombre'])
    return result  

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
  #return [coincidir_ida,coincidir_vuelta] #retorna los dos diccionarios
  return lista_coincidir
  
  #print(coincidir_ida.values())
  #print(coincidir_vuelta.keys())
  

#solo necesito retorna las lista de ida y vuelta que contengan los 2 puntos
def ida_vuelta_list(punto1):
    ida_list= []
    #print ("\n\n*** Buqueda ruta/s que conecte/n 2 puntos***")
    rutas_punto1 = buscar_ruta(punto1)
    #print(rutas_punto1)
    #verificar que 
    for r in rutas_punto1: #r = nombre ruta
      rut= collection.find({"nombre": r}) #busca la ruta donde coincida el nombre
      for r2 in rut:

        #if #punto2 se encuentra junto con punto1, añadir a la lista
        ida_list.append(r2['ida']) #añado a la lista la ida, pueden haber varios lista de ida 
      #ida_list= r2['ida']
        #vuelta_list = r2['vuelta']
    print(ida_list)
    return ida_list

def indice_punto(punto, lista):
    for i in range(len(lista)):
      for j in range(len(lista[i])):
        if lista[i][j] == punto:
          print("indice p: "+str(j))
          #return j #retorna el indice donde lo encuentra

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
    
    return mensaje
      
    #print("indice punto 1: "+str(indice_punto1[1]))
    #print("indice punto 2: "+str(indice_punto2[1]))
    #if indice_punto1 < indice_punto2: #si el indice es menor es porque hay una conexión logica 
    #  return True 
    #por cada ruta tengo que verificar en ida y vuelta, si punto1 esta antes de punto 2

#función para borrar espacios en los campos de la lista ida y vuelta
#en proceso
def update_espacios():
  cursor = collection.find()
  for i in cursor:
    if i['nombre'] == 'ruta 1':
      ida_list= i['ida']
      print(ida_list)
  #coleccion.update({"ida":})

#update_espacios()

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

#en proceso
def no_repeat():
  cursor = collection.find()
  for i in cursor:
    ida_list= i['ida']
    for j in ida_list:
      pass
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
#TODO averiguar cuando utilizar el mongoClient.close()
#collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)

"""
def buscar_ruta(punto):
    print ("\n\n*** Buqueda de los rutas***")
    cursor = collection.find({"ida":{"$in":[punto]}})
    for rut in cursor:
        print ("%s - %s" \
          %(rut['nombre'], rut['ida']))

def indice_punto(punto, lista):
    for i in range(len(lista)):
        if lista[i] == punto:
          return i #retorna el indice donde lo encuentra
"""
