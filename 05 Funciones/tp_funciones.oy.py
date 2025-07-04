#Trabajo Practico Funciones

import math

def imprimir_hola_mundo():
    """1. Imprime 'Hola Mundo!'."""
    print("Hola Mundo!")


def saludar_usuario(nombre):
    """2. Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    """3. Imprime información personal formateada."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    """4a. Calcula y devuelve el área de un círculo de radio dado."""
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    """4b. Calcula y devuelve el perímetro de un círculo de radio dado."""
    return 2 * math.pi * radio


def segundos_a_horas(segundos):
    """5. Convierte segundos a horas (puede ser fracción)."""
    return segundos / 3600


def tabla_multiplicar(numero):
    """6. Imprime la tabla de multiplicar del 1 al 10 para el número dado."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a, b):
    """
7. Devuelve una tupla con (suma, resta, multiplicación, división).
   Si b es cero, la división retorna None.
    """
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else None
    return suma, resta, producto, division


def calcular_imc(peso, altura):
    """8. Calcula y devuelve el Índice de Masa Corporal con dos decimales."""
    imc = peso / (altura ** 2)
    return round(imc, 2)


def celsius_a_fahrenheit(celsius):
    """9. Convierte Celsius a Fahrenheit."""
    return celsius * 9 / 5 + 32


def calcular_promedio(a, b, c):
    """10. Calcula y devuelve el promedio de tres números."""
    return (a + b + c) / 3


def main():
    # 1.
    imprimir_hola_mundo()
    print()

    # 2.
    nombre = input("2) Ingresá tu nombre: ")
    print(saludar_usuario(nombre))
    print()

    # 3.
    apellido = input("3) Ingresá tu apellido: ")
    edad = int(input("   Ingresá tu edad: "))
    residencia = input("   Ingresá tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()

    # 4.
    radio = float(input("4) Ingresá el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"   Área: {area:.2f}")
    print(f"   Perímetro: {perimetro:.2f}")
    print()

    # 5.
    segundos = int(input("5) Ingresá segundos a convertir: "))
    horas = segundos_a_horas(segundos)
    print(f"   Equivalen a {horas:.4f} horas")
    print()

    # 6.
    num_tabla = int(input("6) Ingresá un número para la tabla de multiplicar: "))
    print(f"   Tabla de multiplicar de {num_tabla}:")
    tabla_multiplicar(num_tabla)
    print()

    # 7.
    a = float(input("7) Ingresá el primer número: "))
    b = float(input("   Ingresá el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print("   Resultados:")
    print(f"     Suma: {resultados[0]}")
    print(f"     Resta: {resultados[1]}")
    print(f"     Multiplicación: {resultados[2]}")
    div = resultados[3]
    print(f"     División: {div if div is not None else 'No definida (división por cero)'}")
    print()

    # 8.
    peso = float(input("8) Ingresá tu peso (kg): "))
    altura = float(input("   Ingresá tu altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"   Tu IMC es: {imc}")
    print()

    # 9.
    celsius = float(input("9) Ingresá temperatura en °C: "))
    fahr = celsius_a_fahrenheit(celsius)
    print(f"   Equivalente en °F: {fahr:.2f}")
    print()

    # 10.
    n1 = float(input("10) Ingresá primer número: "))
    n2 = float(input("    Ingresá segundo número: "))
    n3 = float(input("    Ingresá tercer número: "))
    promedio = calcular_promedio(n1, n2, n3)
    print(f"   Promedio: {promedio:.2f}")


if __name__ == "__main__":
    main()
