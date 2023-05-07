##funcionesmap NOS PERMITE TRANFORMAR UN CONJUNTO DE VALORES A OTRO CONJUNTO DE VALORES DEL NISMO TAMAÑO AFECTANDO CADA ELEMENTO 

##funcion

al_cuadrado = lambda X:X*X

#Creamos la lista 

L = [1,2,3,4,5,6,8,9,10]


L_resultado = list(map(al_cuadrado,L))
print(L_resultado)
