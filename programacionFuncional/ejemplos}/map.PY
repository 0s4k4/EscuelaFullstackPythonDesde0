
##creamos una lista iterable
lista  = [1,2,3,4,5]


###una funcion donde pasamos el parametro que se va a multiplicar x por dos
def por_dos(x):
    return x *2;


##le pasamos a map la funcion y la lista, y hace el trabajo como si fuera un bucle 
##map toma dos entradas, una lista o iterable que sera modificado
##una funcion que sera aplicada por cada elemento de la lista anterior
##la sintaxis, map(funcion,lista/entrada iterable)
listaPorDos = map(por_dos,lista)


###imprime un valor iterable, transforma el objeto map a una lista
print(list(listaPorDos))


