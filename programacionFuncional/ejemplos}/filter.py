lista = [7,4,16,3,8]
##creamos una lista con elementos


##se crea una funcion que nos verifica si el recidio de x entre dos es igual a un par 
def es_par(x):
    return x % 2 == 0


##creamos filter, es una funcion que nos crea una nueva lista solo si el resultado de la funcion es igual a true
pares = filter(es_par,lista)


##imprime la lista de todos los trues que se han hecho en la funcion
print(list(pares))