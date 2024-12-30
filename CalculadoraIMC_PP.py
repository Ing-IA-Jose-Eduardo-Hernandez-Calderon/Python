# Este código calcula el IMC (indice de masa corporal), que corresponde a mi octavo proyecto personal

#Se le pide al usuario que ingresa su peso en KG y su altura en metros

peso = float(input("Ingresa tu peso en KG: "))
altura = float(input("Ingresa tu altura en metros (m): "))

#Se calcula el IMC y se redondea a 1 decimal utilizando round
IMC = peso / pow(altura,2)
IMC = round(IMC,1)

#Se verifican las condiciones
if IMC < 18.5:
    print(f"Tu indice de masa corporal es de '{IMC}'. Tu nivel de peso es: Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print(f"Tu indice de masa corporal es de '{IMC}'. Tu nivel de peso es: Peso saludable")
elif IMC >= 25.0 and IMC <= 29.9:
    print(f"Tu indice de masa corporal es de '{IMC}'. Tu nivel de peso es: Sobrepeso")
else:
    print(f"Tu indice de masa corporal es de '{IMC}'. Tu nivel de peso es: Obesidad")
