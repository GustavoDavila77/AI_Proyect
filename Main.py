# -*- coding: utf-8 -*-
from crud_mongo import buscar_ruta, two_points #hace las consultas en la base de datos
from audio_txt import Listening #libreria para pasar de audio a texto
from PLN import clasification #libreria para que permite obtener los barrios,direcciones
from text_to_audio import reproducir #libreria para pasar de texto a audio

if __name__ == "__main__":
    text_from_audio = Listening()
    puntos = clasification(text_from_audio.lower())
    print(puntos)
    #puntos = ['calle 13','la popa']
    if len(puntos) == 1: #si solo encontro un punto, busque las rutas para ese punto
        buscar = buscar_ruta(puntos[0])
        reproducir(buscar)

    elif len(puntos) == 2: #si hay dos puntos, busque una conexión logica
        respuesta = two_points(puntos[0],puntos[1])
        #print(respuesta)
        reproducir(respuesta)


#TODO add rutas 4, 6, 
#29, 25A, 17
