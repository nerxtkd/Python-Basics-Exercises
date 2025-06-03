# Ejercicio 1.
# Definir una variable que se llama “prueba”, asignarle el valor “23” e imprimirla por pantalla. Tras la impresión asígnale el valor “24” y volver a imprimirlo.
prueba = 23
print(prueba)

# cambiamos el valor: 
prueba = 24
print(prueba)


# Ejercicio 2.
# Definir una variable que se llama “PRUEBA_CONSTANTE”, asignarle el valor “25” e imprimirla por pantalla.
PRUEBA_CONSTANTE = 25
print(PRUEBA_CONSTANTE)


# Ejercicio 3. 
# Definir un array de 5 elementos que contengan los números 1, 2, 3, 4 y 5, e imprimirlo por pantalla.
numeros = [1,2,3,4,5]
print(numeros)


# Ejercicio 4. 
# Define una variable llamada “numero”, y asígnale un valor. A continuación, utilizando un if-else, imprime por pantalla si el número introducido es par o impar.
numero = 9

if numero == 0:
    print("Este número es el cero.")
elif numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")



# Ejercicio 5.
# Crear un programa que imprima los números del 1 al 5 utilizando un bucle while y una variable llamada “contador”, que se tendrá que incrementar una unidad en cada interacción del bucle.
contador=1
while contador <= 5:
    print(contador)
    contador += 1


# Ejercicio 6. 
# Crear un programa que imprima los números del 1 al 5 usando un bucle for.
for numero in range(1, 6):
    print(numero)