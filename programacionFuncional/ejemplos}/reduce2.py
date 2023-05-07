from functools import reduce  # Importamos la función reduce desde el módulo functools

personas = [  # Creamos una lista de diccionarios que representan a tres personas
    {'Nombre': 'Alicia', 'Edad': 22},
    {'Nombre': 'Bob', 'Edad': 29},
    {'Nombre': 'Charlie', 'Edad': 33}
]

suma_edad = reduce(lambda total, p: total + p['Edad'], personas, 0)  # Usamos la función reduce para sumar las edades de las personas
# La función lambda toma dos argumentos (total y p) y devuelve la suma del total acumulado hasta ese momento (total) y la edad de la persona actual (p['Edad']).
# En cada iteración, reduce() toma el resultado acumulado hasta ese momento (total) y el siguiente elemento de la lista (p)
# y aplica la función lambda para obtener el nuevo valor acumulado.

# En este caso, se proporciona un valor inicial de 0 para el acumulador, ya que no hay edades en la lista al principio.

promedio_edad = suma_edad / len(personas)  # Calculamos el promedio de edad dividiendo la suma total de edades entre el número de personas

print(promedio_edad)  # Imprimimos el resultado del promedio de edad en la consola
