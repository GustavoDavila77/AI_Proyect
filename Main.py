# -*- coding: utf-8 -*-
from crud_mongo import buscar_ruta
from audio_txt import Listening
from PLN import clasification

if __name__ == "__main__":
    text_from_audio = Listening()
    puntos = clasification(text_from_audio.lower())
    print(puntos)
    try:
        if puntos: #si la lista no esta vacia
            for indice in range(len(puntos)):
                print (str(indice+1) + "."+ str(buscar_ruta(puntos[indice])))
    except:
        print('No se encontro ningun resultado')

#buscar_ruta("victoria")
