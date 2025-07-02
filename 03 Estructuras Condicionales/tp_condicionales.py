

# Trabajo Práctico N°3 - Estructuras Condicionales (Programación I)


import random
from statistics import mean, median, mode

# Ejercicio 1
edad = int(input("1️⃣ Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# Ejercicio 2
nota = float(input("\n2️⃣ Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("\n3️⃣ Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
edad2 = int(input("\n4️⃣ Ingrese su edad: "))
if edad2 < 12:
    print("Niño/a")
elif edad2 < 18:
    print("Adolescente")
elif edad2 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5
contrasena = input("\n5️⃣ Ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
numeros = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros)
mediana = median(numeros)
moda = mode(numeros)

print("\n6️⃣ Análisis de distribución aleatoria (50 valores):")
print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución indefinida")

# Ejercicio 7
texto = input("\n7️⃣ Ingrese una palabra o frase: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

# Ejercicio 8
nombre = input("\n8️⃣ Ingrese su nombre: ")
opcion = input("Elija una opción (1: MAY, 2: min, 3: Capitalizado): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

# Ejercicio 9
magnitud = float(input("\n9️⃣ Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Ejercicio 10
mes = int(input("\n🔟 Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día: "))
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()

if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido")
