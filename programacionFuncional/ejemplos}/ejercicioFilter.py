# Dada una lista de palabras, escribe un programa que cree una nueva lista que contenga solo las palabras que
# tienen más de 5 caracteres. Utiliza la función filter() y una función lambda para crear esta nueva lista.

palabras = ['hola', 'adios', 'python', 'programacion', 'lenguaje']

cantidadCaracteres = 5;



palabrasDe5 = list(filter(lambda palabra5: len(palabra5) > 5,palabras)) 


print(palabrasDe5)
# palabra = len('hola');


# numero = 4;


# if(palabra == numero):
#     print('valores indicados')
# else:
#     print('valores de menos')


