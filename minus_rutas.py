#dado un texto, retorna una lista en minuscula y separado por comas, y sin espacios
def minus(text):
    text_minus= text.lower()
    result= text_minus.split(', ')
    return result

#TODO hacer scrapping a la pagina area metropolitana
#TODO hacer limpieza de el texto
if __name__ == "__main__":
    print(minus('Urbanización Salamanca, Variante Condina, Nuevo Sol, San Marcos, San Joaquín, &nbsp;Glorieta Corales, Av. Américas,&nbsp; Calle 81, Carrera 25, Gamma, Barrio San Fernando, la Playa, Avda. De las Américas, Los Cedros, La Dulcera, Vuelta al centro comercial la 14, Terminal de Transportes, Calle 17, INVICO, Calle 14, calle 13, Cra 5a, Calle 10, Puente Mosquera, La Popa, Avda. El Ferrocarril'))
