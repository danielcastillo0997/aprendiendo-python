
# ============================================================
# HISTORIAL PERMANENTE DE PEDIDOS
# Archivo: historial.py
# ============================================================

from pathlib import Path

# Guardaremos pedidos.txt junto a historial.py.
ARCHIVO_PEDIDOS = Path(__file__).resolve().parent / "pedidos.txt"


# ============================================================
# NIVEL 1 - REGISTRAR UN PEDIDO
# ============================================================

def registrar_pedido(cafe):

    # "a" agrega información sin borrar pedidos anteriores.
    with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
        archivo.write(cafe + "\n")

    print("Pedido registrado correctamente.")

# APUNTES:
# "a" -> Append: agrega al final.
# write() -> Escribe el nombre del café.
# "\n" -> Cada pedido se guarda en una línea.
# with -> Cierra automáticamente el archivo.


# ============================================================
# NIVEL 2 - VER EL HISTORIAL
# ============================================================

def mostrar_historial():

    print("\n========== HISTORIAL DE PEDIDOS ==========")

    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()

        if not pedidos:
            print("Todavía no hay pedidos registrados.")
            return

        # enumerate permite numerar los pedidos.
        for numero, pedido in enumerate(pedidos, start=1):
            print(f"Pedido N° {numero} - {pedido.strip()}")

    except FileNotFoundError:
        print("Todavía no existe un historial de pedidos.")

    print("==========================================")


# ============================================================
# NIVEL 3 - CONTAR LOS PEDIDOS
# ============================================================

def contar_pedidos():

    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            return sum(1 for linea in archivo if linea.strip())

    except FileNotFoundError:
        return 0

# APUNTE:
# Cada línea no vacía representa un pedido.
# sum() cuenta esas líneas.
# Si no existe el archivo, devolvemos 0.
