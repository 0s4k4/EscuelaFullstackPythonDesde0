from functools import reduce  # Importamos la función reduce desde el módulo functools

lista = [1, 2, 3, 4, 5]  # Creamos una lista de números

suma_total = reduce(lambda x, y: x + y, lista)  # Usamos la función reduce para sumar los números de la lista
# La función lambda toma dos argumentos (x e y) y devuelve su suma (x + y).
# En cada iteración, reduce() toma el resultado acumulado hasta ese momento (x) y el siguiente elemento de la lista (y)
# y aplica la función lambda para obtener el nuevo valor acumulado.

print(suma_total)  # Imprimimos el resultado de la suma total en la consola
