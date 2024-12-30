# Este código verifica si un numero es par o impar, que corresponde a mi septimo proyecto personal

#Se le pide al usuario ingresar el numero a verificar
numero = int(input("Ingresa el numero que quieres que se verifique si es par o impar: "))

#Si al dividir el numero entre 2, el residuo es 0 entonces es par, de lo contrario es impar
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")