
# Trabajo Practico Listas


def actividad1():
    # 1) Números del 1 al 100 múltiplos de 4
    multiplos_de_4 = list(range(4, 101, 4))
    print("1) Múltiplos de 4:", multiplos_de_4)

def actividad2():
    # 2) Lista con 5 elementos y mostrar penúltimo usando índice negativo
    favoritos = ["pizza", "python", "play", "música", "cine"]
    print("2) Penúltimo elemento:", favoritos[-2])

def actividad3():
    # 3) Lista vacía, agregar tres palabras con append e imprimir
    lista_vacia = []
    lista_vacia.append("hola")
    lista_vacia.append("mundo")
    lista_vacia.append("UTN")
    print("3) Lista resultante:", lista_vacia)

def actividad4():
    # 4) Reemplazar segundo y último valor de 'animales'
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"     # segundo elemento
    animales[-1] = "oso"     # último elemento
    print("4) Animales modificados:", animales)

def actividad5():
    # 5) Explicar: remove(max(numeros))
    numeros = [8, 15, 3, 22, 7]
    # Elimina el valor máximo de la lista
    numeros.remove(max(numeros))
    print("5) Lista tras eliminar el máximo:", numeros)

def actividad6():
    # 6) Lista de 10 a 30 con saltos de 5, mostrar dos primeros
    lista = list(range(10, 31, 5))
    print("6) Dos primeros:", lista[:2])

def actividad7():
    # 7) Reemplazar valores centrales de 'autos'
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["4x4", "camioneta"]  # índices 1 y 2
    print("7) Autos modificados:", autos)

def actividad8():
    # 8) Lista 'dobles' con el doble de 5, 10 y 15
    dobles = []
    dobles.append(2 * 5)
    dobles.append(2 * 10)
    dobles.append(2 * 15)
    print("8) Dobles:", dobles)

def actividad9():
    # 9) Operaciones sobre lista de compras
    compras = [
        ["pan", "leche"],
        ["arroz", "fideos", "salsa"],
        ["agua"]
    ]
    # a) Agregar "jugo" al tercer cliente
    compras[2].append("jugo")
    # b) Reemplazar "fideos" por "tallarines"
    idx = compras[1].index("fideos")
    compras[1][idx] = "tallarines"
    # c) Eliminar "pan" del primer cliente
    compras[0].remove("pan")
    print("9) Compras actualizadas:", compras)

def actividad10():
    # 10) Crear lista anidada con los valores pedidos
    lista_anidada = [
        15,
        True,
        [25.5, 57.9, 30.6],
        False
    ]
    print("10) Lista anidada:", lista_anidada)

if __name__ == "__main__":
    actividad1()
    actividad2()
    actividad3()
    actividad4()
    actividad5()
    actividad6()
    actividad7()
    actividad8()
    actividad9()
    actividad10()
