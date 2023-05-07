##sumar todos los productos de una lista

from functools import reduce


lista_numero = [1,2,3,4,5]


suma_total = reduce(lambda x,y: x+y, lista_numero)


print('La suma total:   ',suma_total)




##multiplicamos todos los productos de la lista



lista2_numero = [1,2,3,4,5]

multiplicacion_total   =    reduce(lambda x,y: x*y,lista_numero)

print('la total de la lista de la multiplicacion',multiplicacion_total)



#### encontrar el numero mayor en una lista usando lamnbda y reduce

lista_numeros3 = [1,7,3,5,9,2]
maximo_valor = reduce(lambda x,y: x if x > y else y,lista_numeros3)
print('el numero mayor es de ',maximo_valor)


##concatenar todos los caracteres
lista_cadenas = ['hola','   ','Mundo','!']
cadena_completa = reduce(lambda x,y: x + y,lista_cadenas)
print('la cadena concatenada    ',cadena_completa)