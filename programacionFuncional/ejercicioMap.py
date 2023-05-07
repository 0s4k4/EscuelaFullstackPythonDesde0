# Dada una lista de temperaturas en grados Celsius, escribe un programa que cree una nueva lista 
# que contenga las mismas temperaturas, pero en grados Fahrenheit. Utiliza la función map() y 
# una función lambda para crear esta nueva lista.


#Recuerda que la fórmula para convertir grados Celsius a grados Fahrenheit es: F = C * 9/5 + 32.


celsius = [0,10,20,30,40,50]

celsiusToFahrenheit = lambda x: (9/5 * x)+32

conversionFarenhenti = list(map(celsiusToFahrenheit,celsius))

print(conversionFarenhenti);
