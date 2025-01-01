# Este código te dice cuanta edad tienes en dias teniendo una logica general, que corresponde a mi decimo proyecto personal

#Se le pide al usuario que ingrese su edad en años
edad = int(input("¿Cuántos años tienes?: "))

#Dias en 1 año sin considerar si es bisiesto o no
dias_año = 365

#Calculo de la edad del usuario en dias
edad_dias = edad * dias_año;

#Se imprime en pantalla la edad en dias
print(f"Tienes actualmente '{edad}' años de edad, lo que equivale aproximadamente a '{edad_dias}' dias.")