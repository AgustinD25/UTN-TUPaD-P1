# Trabajo Practico Datos Complejos

def punto_1_2_3():
    # 1) Crear y añadir frutas
    precios_frutas = {
        'Banana': 1200,
        'Anana': 2500,
        'Melón': 3000,
        'Uva': 1450
    }
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera']    = 2300

    # 2) Actualizar precios
    precios_frutas['Banana']  = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón']   = 2800

    # 3) Lista de frutas (solo claves)
    lista_frutas = list(precios_frutas.keys())

    print("\n1–3) Diccionario precios_frutas:")
    print(precios_frutas)
    print("Lista de frutas:", lista_frutas)


def punto_4():
    # 4) Agenda telefónica
    contactos = {}
    print("\n4) Carga 5 contactos (nombre y teléfono):")
    for i in range(5):
        nombre = input(f"  Nombre #{i+1}: ").strip()
        tel    = input(f"  Teléfono de {nombre}: ").strip()
        contactos[nombre] = tel

    consulta = input("Consulta nombre: ").strip()
    if consulta in contactos:
        print(f"  → {consulta}: {contactos[consulta]}")
    else:
        print("  → No existe ese contacto.")


def punto_5():
    # 5) Palabras únicas y recuento
    frase = input("\n5) Ingresa una frase: ").strip().lower()
    palabras = frase.split()
    unicas   = set(palabras)
    recuento = {p: palabras.count(p) for p in unicas}

    print("  Palabras únicas:", unicas)
    print("  Recuento:", recuento)


def punto_6():
    # 6) Promedio de notas
    alumnos = {}
    print("\n6) Ingresa 3 alumnos y sus 3 notas:")
    for i in range(3):
        nombre = input(f"  Nombre del alumno #{i+1}: ").strip()
        notas  = []
        for j in range(3):
            n = float(input(f"    Nota #{j+1} de {nombre}: "))
            notas.append(n)
        alumnos[nombre] = tuple(notas)

    print("\n  Promedios:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"    {nombre}: {promedio:.2f}")


def punto_7():
    # 7) Conjuntos de aprobados
    print("\n7) Ingrese nombres que aprobaron Parcial 1 (separados por comas):")
    p1 = set(input("  ").replace(",", " ").split())
    print("   Parcial 2:")
    p2 = set(input("  ").replace(",", " ").split())

    ambos      = p1 & p2
    solo_uno   = p1 ^ p2
    al_menos_uno = p1 | p2

    print("  Aprobados en ambos parciales:", ambos)
    print("  Aprobados solo en uno de los dos:", solo_uno)
    print("  Aprobados al menos en uno:", al_menos_uno)


def punto_8():
    # 8) Stock de productos
    stock = {}
    print("\n8) Sistema de stock. Comandos: consultar / agregar / salir")
    while True:
        cmd = input("  Acción: ").strip().lower()
        if cmd == 'salir':
            break
        if cmd == 'consultar':
            prod = input("    Producto: ").strip()
            valor = stock.get(prod)
            if valor is None:
                print("    No existe ese producto.")
            else:
                print(f"    Stock de {prod}: {valor}")
        elif cmd == 'agregar':
            prod = input("    Producto: ").strip()
            cant = int(input("    Cantidad a agregar: "))
            stock[prod] = stock.get(prod, 0) + cant
            print(f"    Nuevo stock de {prod}: {stock[prod]}")
        else:
            print("    Comando no reconocido.")


def punto_9():
    # 9) Agenda de eventos
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }
    print("\n9) Consulta agenda (ingresa día y hora):")
    dia  = input("  Día: ").strip().lower()
    hora = input("  Hora (HH:MM): ").strip()
    evento = agenda.get((dia, hora))
    if evento:
        print(f"  → {evento}")
    else:
        print("  → No hay actividad agendada.")


def punto_10():
    # 10) Invertir diccionario países–capitales
    original = {}
    print("\n10) Ingresa país y capital (vacío para terminar):")
    while True:
        pais    = input("  País: ").strip()
        if not pais:
            break
        capital = input("  Capital de " + pais + ": ").strip()
        original[pais] = capital

    invertido = {cap: pais for pais, cap in original.items()}
    print("  Original:", original)
    print("  Invertido:", invertido)


def main():
    print("=== Práctico 6: Estructuras de Datos Complejas ===")
    punto_1_2_3()
    punto_4()
    punto_5()
    punto_6()
    punto_7()
    punto_8()
    punto_9()
    punto_10()
    print("\nFin del práctico. ¡Éxitos!")


if __name__ == "__main__":
    main()
