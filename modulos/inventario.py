
# ============================================================
# MÓDULO DE INVENTARIO
# Archivo: inventario.py
# ============================================================

# Este módulo permite trabajar con un inventario básico.
#
# CONCEPTOS:
# - Diccionarios.
# - Funciones.
# - Bucles for.
# - Condicionales if.
# - Acumuladores.


# ============================================================
# NIVEL 1 - INVENTARIO INICIAL
# ============================================================

productos = {
    "P001": {
        "nombre": "Tornillo",
        "precio": 1500,
        "cantidad": 20
    },
    "P002": {
        "nombre": "Tuerca",
        "precio": 800,
        "cantidad": 50
    },
    "P003": {
        "nombre": "Arandela",
        "precio": 500,
        "cantidad": 100
    }
}


# ============================================================
# NIVEL 2 - CONSULTAR UN PRODUCTO
# ============================================================

def buscar_producto(codigo):
    return productos.get(codigo, "Producto no encontrado")


# ============================================================
# NIVEL 3 - CALCULAR EL VALOR DE UN PRODUCTO
# ============================================================

def valor_producto(codigo):

    producto = productos.get(codigo)

    if producto is None:
        return "Producto no encontrado"

    return producto["precio"] * producto["cantidad"]


# ============================================================
# NIVEL 4 - CALCULAR EL INVENTARIO TOTAL
# ============================================================

def valor_inventario():

    total = 0

    for producto in productos.values():

        subtotal = producto["precio"] * producto["cantidad"]

        total += subtotal

    return total


# ============================================================
# NIVEL 5 - IDENTIFICAR PRODUCTOS CON POCO INVENTARIO
# ============================================================

def productos_bajos(limite=30):

    resultado = []

    for codigo, producto in productos.items():

        if producto["cantidad"] < limite:

            resultado.append({
                "codigo": codigo,
                "nombre": producto["nombre"],
                "cantidad": producto["cantidad"]
            })

    return resultado


# ============================================================
# NIVEL 6 - AGREGAR NUEVOS PRODUCTOS
# ============================================================

def agregar_producto(codigo, nombre, precio, cantidad):

    if codigo in productos:
        return "El código ya existe"

    if precio < 0 or cantidad < 0:
        return "Precio y cantidad no pueden ser negativos"

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    return "Producto agregado correctamente"


# APUNTES:
#
# El diccionario productos está definido
# dentro del módulo inventario.py.
#
# Cuando importamos las funciones, podemos utilizarlas
# para consultar y modificar ese diccionario.
#
# Los cambios realizados en memoria duran mientras
# el programa se está ejecutando.
#
# No se guardan automáticamente en un archivo.
