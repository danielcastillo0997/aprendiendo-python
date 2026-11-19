
# ============================================================
# PEDIDOS DE CAFÉ
# Archivo: pedidos.py
# ============================================================

def pedir_cafe():

    print("\nElige el café que prefieras:")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Opción: ")

    # Diccionario de cafés disponibles.
    cafes = {
        "1": "Espresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    # Consultamos el café elegido.
    cafe = cafes.get(opcion)

    # Si la opción no existe, devolvemos None.
    if cafe is None:

        print("Opción de café no válida.")
        return None

    print("Has pedido un", cafe)

    # Devolvemos el nombre del café.
    return cafe


# APUNTES:
#
# get() obtiene un valor del diccionario.
#
# Si la clave no existe, devuelve None.
#
# return cafe permite utilizar el resultado
# desde el archivo main.py.
