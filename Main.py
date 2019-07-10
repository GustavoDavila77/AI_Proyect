# -*- coding: utf-8 -*-
from crud_mongo import buscar_ruta, two_points
from audio_txt import Listening
from PLN import clasification
from text_to_audio import reproducir

if __name__ == "__main__":
    # text_from_audio = Listening()
    # puntos = clasification(text_from_audio.lower())
    # print(puntos)
    puntos = ['frailes','montelibano']
    if len(puntos) == 1: #si solo encontro un punto, busque las rutas 
        try:
            for indice in range(len(puntos)):
                print (str(indice+1) + "."+ str(buscar_ruta(puntos[indice])))
        except:
            print('No se encontro ningun resultado')

    elif len(puntos) == 2: #si hay dos puntos, busque una conexión logica
        respuesta = two_points(puntos[0],puntos[1])
        #print(respuesta)
        reproducir(respuesta)


#buscar_ruta("victoria")
#TODO   4, 6, governacion, 18, 1, 24, 36, virginia
#29, 25A, 17
