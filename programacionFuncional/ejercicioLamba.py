##ejercico de lamba donde nos pide 
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Escribe aquí tu código utilizando filter() y lambda para crear una nueva lista 
# que contenga solo los números pares de la lista original.
#print(numeros_pares) # Debería imprimir [2, 4, 6, 8, 10]

def pares(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

es_par = filter(pares,numeros)


print(list(es_par))
    




