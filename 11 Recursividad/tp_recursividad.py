#Trabajo Practico Recursividad 

def factorial(n):
    """Ejercicio 1: Calcula el factorial de n de forma recursiva."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    """Muestra factoriales de 1 hasta 'hasta'."""
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

def fibonacci_recursivo(pos):
    """Ejercicio 2: Devuelve el término 'pos' de la serie de Fibonacci recursivamente."""
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def mostrar_fibonacci(hasta):
    """Muestra la serie de Fibonacci desde la posición 0 hasta 'hasta'."""
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")

def potencia_recursiva(base, exp):
    """Ejercicio 3: Calcula base^exp recursivamente."""
    if exp == 0:
        return 1
    return base * potencia_recursiva(base, exp - 1)

def decimal_a_binario(n):
    """Ejercicio 4: Convierte un entero positivo a cadena binaria recursivamente."""
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    """Ejercicio 5: Devuelve True si 'palabra' es palíndromo (sin reversed ni [::-1])."""
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    """Ejercicio 6: Suma recursiva de los dígitos de n."""
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    """Ejercicio 7: Cuenta el total de bloques de una pirámide de base n."""
    if n <= 1:
        return n
    return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    """Ejercicio 8: Cuenta cuántas veces aparece 'digito' en 'numero' recursivamente."""
    if numero == 0:
        return 0
    cuenta = 1 if (numero % 10) == digito else 0
    return cuenta + contar_digito(numero // 10, digito)

def main():
    # Ejercicio 1
    hasta = int(input("1) Mostrar factoriales hasta (entero >=1): "))
    mostrar_factoriales(hasta)
    print()

    # Ejercicio 2
    pos = int(input("2) Posición máxima de Fibonacci a mostrar: "))
    mostrar_fibonacci(pos)
    print()

    # Ejercicio 3
    base = int(input("3) Base para potencia recursiva: "))
    exp = int(input("   Exponente: "))
    print(f"   Resultado: {potencia_recursiva(base, exp)}")
    print()

    # Ejercicio 4
    dec = int(input("4) Número decimal a convertir a binario: "))
    print(f"   Binario: {decimal_a_binario(dec)}")
    print()

    # Ejercicio 5
    pal = input("5) Palabra para verificar palíndromo: ").lower()
    print(f"   Es palíndromo: {es_palindromo(pal)}")
    print()

    # Ejercicio 6
    n6 = int(input("6) Número para sumar sus dígitos: "))
    print(f"   Suma de dígitos: {suma_digitos(n6)}")
    print()

    # Ejercicio 7
    n7 = int(input("7) Bloques en el nivel más bajo de la pirámide: "))
    print(f"   Total de bloques: {contar_bloques(n7)}")
    print()

    # Ejercicio 8
    num8 = int(input("8) Número entero en el que contar dígitos: "))
    dig = int(input("   Dígito a contar (0–9): "))
    print(f"   Aparece {contar_digito(num8, dig)} veces")

if __name__ == "__main__":
    main()
