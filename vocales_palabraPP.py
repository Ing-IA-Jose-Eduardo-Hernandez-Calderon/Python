# Este código cuenta las vocales que haya en una palabra, que corresponde a mi noveno proyecto personal

#Se le pide al usuario que ingrese la palabra a la cual se le contaran las vocales
palabra = str(input("Ingresa la palabra para contar cuantas vocales tiene: "))

#Se convierte la palabra a minusculas para que el programa funcione correctamente
palabra_min = palabra.lower()

#Se inicializa una lista que contiene todas las vocales
vocales = ["a","e","i","o","u"]

#Se inicia el contador en 0 de las vocales
contador_vocal = 0

#Cada letra que aparezca en la lista vocales la encontrará en la palabra y contará cuantas veces aparece
for letra in vocales:
    contador = palabra_min.count(letra)
    print(f"La letra '{letra}' aparece '{contador}' veces en la palabra {palabra_min}.")
    #El contador se actualiza en cada iteracion
    contador_vocal += contador

#Se imprime en pantalla cuantas vocales contiene en total
print(f"\nLa palabra '{palabra_min}' contiene '{contador_vocal}' vocales.")