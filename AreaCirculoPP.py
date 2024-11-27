# Este código calcula el area de un circulo pidiendo al usuario el radio, que corresponde a mi tercer proyecto personal

# Se le pide al usuario ingresar el radio del circulo y se hace la conversión del radio a tipo float para poder trabajar con el mismo tipo de dato
radio = float(input("Ingresa el radio del circulo: "))
PI = 3.1416
# Para elevar al cuadrado, se utiliza la función pow
Area = PI * pow(radio,2)
print(f"El area del circulo es: {Area}")