# -*- coding: utf-8 -*-
class Ruta:

    def __init__(self, nombre, ida, vuelta):
        self.nombre = nombre
        self.ida = ida
        self.vuelta = vuelta

    #convierte un objeto de tipo Futbolista en un diccionario/documento
    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "ida":self.ida,
            "vuelta": self.vuelta        
        }

    def __str__(self):
        return "Nombre: %s - Ida: %s - Vuelta: %s" \
               %(self.nombre, self.ida, self.vuelta)
