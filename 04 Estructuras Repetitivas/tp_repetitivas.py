#TRABAJO PRACTICO ESTRUCTURAS REPETITIVAS

import random


def ejercicio_1():
    """1) Imprimir todos los enteros de 0 a 100."""
    for n in range(0, 101):
        print(n)


def ejercicio_2():
    """2) Contar dígitos de un número entero."""
    num = int(input("2) Ingrese un número entero: "))
    digitos = len(str(abs(num)))
    print(f"Cantidad de dígitos: {digitos}")


def ejercicio_3():
    """3) Sumar enteros entre dos valores (excluyéndolos)."""
    a = int(input("3) Valor inicial: "))
    b = int(input("   Valor final: "))
    inicio, fin = min(a, b) + 1, max(a, b)
    suma = 0
    for n in range(inicio, fin):
        suma += n
    print(f"Suma de valores entre {a} y {b} (sin incluirlos): {suma}")


def ejercicio_4():
    """4) Sumatoria hasta ingresar 0."""
    total = 0
    while True:
        n = int(input("4) Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        total += n
    print(f"Total acumulado: {total}")


def ejercicio_5():
    """5) Adivinar un número aleatorio (0–9)."""
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("5) Adivina el número (0–9): "))
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")
            break
        else:
            print("Incorrecto, intenta de nuevo.")


def ejercicio_6():
    """6) Imprimir pares entre 0 y 100 en orden decreciente."""
    for par in range(100, -1, -2):
        print(par)


def ejercicio_7():
    """7) Sumar enteros de 0 a un valor dado."""
    m = int(input("7) Ingrese un entero positivo: "))
    suma = 0
    for n in range(0, m + 1):
        suma += n
    print(f"Suma de 0 a {m}: {suma}")


def ejercicio_8():
    """8) Clasificar 100 números (pares, impares, negativos, positivos)."""
    N = 100
    pares = impares = positivos = negativos = 0
    for i in range(1, N + 1):
        n = int(input(f"8) Número {i}/{N}: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")


def ejercicio_9():
    """9) Calcular la media de 100 números."""
    N = 100
    suma = 0.0
    for i in range(1, N + 1):
        n = float(input(f"9) Número {i}/{N}: "))
        suma += n
    media = suma / N if N > 0 else 0
    print(f"Media de los {N} valores: {media}")


def ejercicio_10():
    """10) Invertir dígitos de un número."""
    entrada = input("10) Ingrese un número: ")
    signo = "-" if entrada.startswith('-') else ""
    digitos = entrada.lstrip('-')
    invertido = digitos[::-1]
    print(f"Número invertido: {signo}{invertido}")


def main():
    opciones = {
        '1': ejercicio_1,
        '2': ejercicio_2,
        '3': ejercicio_3,
        '4': ejercicio_4,
        '5': ejercicio_5,
        '6': ejercicio_6,
        '7': ejercicio_7,
        '8': ejercicio_8,
        '9': ejercicio_9,
        '10': ejercicio_10,
        '0': exit
    }
    while True:
        print("\nPráctico 4 – Elige ejercicio (1–10) o 0 para salir:")
        elec = input("> ")
        accion = opciones.get(elec)
        if accion:
            accion()
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
    