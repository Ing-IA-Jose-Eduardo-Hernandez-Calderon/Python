# Este código calcula el area y perimetro de un rectangulo conociendo su base y altura, que corresponde a mi sexto proyecto personal

#Se le pide al usuario ingresar la base y altura del rectangulo
base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))

#Se calcula el area y el perimetro del rectangulo
area = base * altura
print(f"El area del rectangulo de base: '{base}' y altura: '{altura}' es: {area}")

perimetro = (2*base) + (2*altura)
print(f"El perimetro del rectangulo de base: '{base}' y altura: '{altura}' es: {perimetro}")