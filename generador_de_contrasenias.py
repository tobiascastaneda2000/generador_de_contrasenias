import string
import random

longitud = int(input("Ingrese el tamaño de su contraseña: "))

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
digitos = string.digits
puntuacion = string.punctuation 
todos_caracteres = minusculas + mayusculas + digitos + puntuacion

print(" 1. Todos los caracteres \n 2. Solo minusculas \n 3. Solo mayusculas \n 4. Solo digitos \n")
opccion = int(input("Por favor, ingresa una letra: "))

def funcion(opccion):
    if opccion == 1:
        return todos_caracteres
    elif opccion == 2:
        return minusculas
    elif opccion == 3:
        return mayusculas
    elif opccion == 4:
        return digitos
    
lista_de_caracteres = []
lista_de_caracteres = funcion(opccion)
contrasenia = "".join(random.choice(lista_de_caracteres) for i in range(longitud))

print("La contraseña generada es: " + contrasenia)