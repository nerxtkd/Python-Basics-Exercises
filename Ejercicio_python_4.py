# Ejercicio 4. 
# Define una variable llamada “numero”, y asígnale un valor. A continuación, utilizando un if-else, imprime por pantalla si el número introducido es par o impar.
numero = 9

if numero == 0:
    print("Este número es el cero.")
elif numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
