# Este código representa una calculadora simple (operaciones basicas), que corresponde a mi quinto proyecto personal

#Se le pregunta al usuario los dos valores a manejar
numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

#Se le pregunta al usuario que operación desea realizar
operacion = input("Suma: '+'\nResta: '-'\nMultiplicación: '*'\nDivision: '/'\n¿Qué operación deseas realizar?: ")

#Se inicializa una variable resultado donde se almacenará el reusltado de la operacion que desea realizar el usuario
resultado = None
operacion_valida = True

#Condicionales dependiendo de la opción elegida por el usuario, manejando un mensaje de error de operador si es que se ingresa alguno que no sea válido.
if operacion == '+':
    resultado = numero1 + numero2
elif operacion == '-':
    resultado = numero1 - numero2
elif operacion == '*':
    resultado = numero1 * numero2
elif operacion == '/':
    resultado = numero1 / numero2
else:
    print("Intentalo de nuevo, ese no es un operador válido.")
    operacion_valida = False

#Se utiliza una sola impresión en pantalla para evitar repeticiones innecesarias
if operacion_valida ==  True:
    print(f"El resultado es: {resultado}")