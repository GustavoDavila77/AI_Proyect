# -*- coding: utf-8 -*-
from crud_mongo import buscar_ruta, two_points
from audio_txt import Listening
from PLN import clasification
from text_to_audio import reproducir

if __name__ == "__main__":
    text_from_audio = Listening()
    puntos = clasification(text_from_audio.lower())
    print(puntos)
    #puntos = ['calle 13','la popa']
    if len(puntos) == 1: #si solo encontro un punto, busque las rutas 
        buscar = buscar_ruta(puntos[0])
        reproducir(buscar)

    elif len(puntos) == 2: #si hay dos puntos, busque una conexión logica
        respuesta = two_points(puntos[0],puntos[1])
        #print(respuesta)
        reproducir(respuesta)


#TODO   4, 6, 
#29, 25A, 17
