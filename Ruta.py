# -*- coding: utf-8 -*-
class Ruta:

    def __init__(self, nombre, ida):
        self.nombre = nombre
        self.ida = ida

    #convierte un objeto de tipo Futbolista en un diccionario/documento
    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "ida":self.ida,        
        }

    def __str__(self):
        return "Nombre: %s - Ida: %s" \
               %(self.nombre, self.ida)
