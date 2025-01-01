# Este código suma numeros del 1 hasta N, que corresponde a mi undecimo proyecto personal

#Se le pide al usuario que ingrese hasta que numero quiere sumar
n = int(input("Ingresa el numero hasta el cual quieres que se sume: "))

#Se inicializa la variable donde se almacenará el resultado
resultado = 0

#Se inicia el ciclo que sumará los numeros
for i in range(1,n+1):
    resultado += i

#Se imprime en pantalla el resultado
print(f"La suma desde '1' hasta '{n}' es de: {resultado}")