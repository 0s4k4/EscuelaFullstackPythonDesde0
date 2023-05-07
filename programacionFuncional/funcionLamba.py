##funciones lambda

##lambda argumento:funcion


##definimos una funcion

def calculo(b,h):
    return b*h/2


#asignamos alamba dos bariables, y ejecutamos la funcion que hace la tarea de sacar la area del triangulo usando dos parametros, que es el b y  h
area_triangulo = lambda b,h:calculo(b,h)



##se imprime la area del tiangulo, mandando a llamar area de triangulo y pasando el parametro de b y h
print(area_triangulo(10,5))





