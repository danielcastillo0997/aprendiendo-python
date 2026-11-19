
# ============================================================
# HISTORIAL DE PEDIDOS
# Archivo: historial.py
# ============================================================

# NIVEL 1 - CREAR UNA LISTA PARA GUARDAR PEDIDOS

historial_pedidos = []

# APUNTE:
# La lista comienza vacía.
# Cada nuevo pedido se agregará con append().


# ============================================================
# NIVEL 2 - REGISTRAR UN PEDIDO
# ============================================================

def registrar_pedido(cafe):

    # Creamos un diccionario con los datos del pedido.
    pedido = {
        "numero": len(historial_pedidos) + 1,
        "cafe": cafe
    }

    # Agregamos el pedido a la lista.
    historial_pedidos.append(pedido)

    print("Pedido registrado correctamente.")

# EXPLICACIÓN:
#
# len() cuenta los pedidos existentes.
# + 1 asigna el siguiente número de pedido.
# append() agrega el diccionario a la lista.


# ============================================================
# NIVEL 3 - MOSTRAR EL HISTORIAL
# ============================================================

def mostrar_historial():

    print("\n========== HISTORIAL DE PEDIDOS ==========")

    # Comprobamos si no hay pedidos registrados.
    if not historial_pedidos:

        print("Todavía no tienes pedidos registrados.")
        return

    # Recorremos todos los pedidos.
    for pedido in historial_pedidos:

        print(
            "Pedido N°", pedido["numero"],
            "-", pedido["cafe"]
        )

    print("==========================================")

# APUNTES:
#
# if not historial_pedidos:
# Comprueba si la lista está vacía.
#
# return:
# Termina la función.
#
# for pedido in historial_pedidos:
# Recorre cada diccionario guardado en la lista.


# ============================================================
# NIVEL 4 - CONTAR PEDIDOS
# ============================================================

def contar_pedidos():
    return len(historial_pedidos)


# Esta función devuelve la cantidad de pedidos realizados.
