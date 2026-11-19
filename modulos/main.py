
# ============================================================
# PROGRAMA PRINCIPAL
# Archivo: main.py
# ============================================================

# Este archivo importa funciones de otros módulos.
#
# IMPORTANTE:
# Los cuatro archivos .py deben estar dentro
# de la misma carpeta modulos.


# ============================================================
# NIVEL 1 - IMPORTAR FUNCIONES ESPECÍFICAS
# ============================================================

from operaciones import sumar, restar, multiplicar, dividir

print("OPERACIONES BÁSICAS")

print("Suma:", sumar(2, 3))
print("Resta:", restar(2, 3))
print("Multiplicación:", multiplicar(2, 3))
print("División:", dividir(10, 5))


# ============================================================
# NIVEL 2 - IMPORTAR UN MÓDULO COMPLETO
# ============================================================

import operaciones

print("\nOPERACIONES ADICIONALES")

print("Potencia:", operaciones.potencia(2, 3))
print("Cuadrado:", operaciones.cuadrado(5))
print("Cubo:", operaciones.cubo(3))
print("Promedio:", operaciones.promedio(4, 5, 3))
print("¿10 es par?:", operaciones.es_par(10))

# APUNTE:
#
# import operaciones
#
# Importa el módulo completo.
# Para acceder a sus funciones utilizamos:
#
# operaciones.nombre_funcion()


# ============================================================
# NIVEL 3 - IMPORTAR CON UN ALIAS
# ============================================================

import operaciones as op

print("\nUTILIZANDO UN ALIAS")

print("Suma:", op.sumar(10, 20))
print("Multiplicación:", op.multiplicar(5, 8))

# APUNTE:
#
# as permite crear un alias.
#
# operaciones -> op
#
# El alias nos permite escribir menos código.


# ============================================================
# NIVEL 4 - IMPORTAR FUNCIONES DE SALUDOS
# ============================================================

from saludos import bienvenida, saludar, presentacion

print("\nMÓDULO DE SALUDOS")

print(bienvenida())
print(saludar("Daniel"))
print(presentacion("Ana", 25))


# ============================================================
# NIVEL 5 - IMPORTAR FUNCIONES CON OTRO NOMBRE
# ============================================================

from saludos import clasificar_edad as verificar_edad

print("\nCLASIFICACIÓN DE EDAD")

print(verificar_edad(15))
print(verificar_edad(20))

# APUNTE:
#
# Podemos cambiar el nombre con el que utilizamos
# una función importada mediante as.


# ============================================================
# NIVEL 6 - IMPORTAR EL MÓDULO DE INVENTARIO
# ============================================================

import inventario

print("\nCONSULTA DE PRODUCTOS")

print(inventario.buscar_producto("P001"))
print(inventario.buscar_producto("P002"))


# ============================================================
# NIVEL 7 - CALCULAR VALORES DEL INVENTARIO
# ============================================================

print("\nVALORES DEL INVENTARIO")

print("Valor P001:", inventario.valor_producto("P001"))

print("Valor total del inventario:",
      inventario.valor_inventario())

# RESULTADO INICIAL:
# 120000


# ============================================================
# NIVEL 8 - CONSULTAR PRODUCTOS BAJOS
# ============================================================

print("\nPRODUCTOS CON POCAS UNIDADES")

productos_bajos = inventario.productos_bajos(30)

for producto in productos_bajos:
    print(producto["nombre"], producto["cantidad"])

# RESULTADO:
# Tornillo 20


# ============================================================
# NIVEL 9 - AGREGAR UN PRODUCTO DESDE MAIN
# ============================================================

resultado = inventario.agregar_producto(
    "P004",
    "Destornillador",
    12000,
    10
)

print("\n", resultado)

print("Nuevo valor del inventario:",
      inventario.valor_inventario())

# El inventario inicial vale 120000.
#
# Agregamos 10 destornilladores a 12000.
#
# 12000 * 10 = 120000
#
# Nuevo total: 240000


# ============================================================
# NIVEL 10 - COMBINAR MÓDULOS
# ============================================================

print("\nRESUMEN DEL PROYECTO")

print(saludar("Daniel"))

total = inventario.valor_inventario()

print("Inventario total:", total)

print("Inventario con el doble del valor:",
      operaciones.multiplicar(total, 2))


# ============================================================
# APUNTES FINALES
# ============================================================

# FORMAS DE IMPORTAR:
#
# 1. import modulo
#    Importa el módulo completo.
#
# 2. from modulo import funcion
#    Importa una función específica.
#
# 3. import modulo as alias
#    Importa un módulo con otro nombre.
#
# 4. from modulo import funcion as alias
#    Importa una función utilizando otro nombre.
#
# RECOMENDACIONES:
#
# - Organiza las funciones según su responsabilidad.
# - Evita copiar la misma función en diferentes archivos.
# - Utiliza main.py para coordinar el programa.
# - Conserva nombres descriptivos.
# - Utiliza comentarios para documentar lo aprendido.
#
# NOTA:
# Evita utilizar from modulo import * en proyectos reales,
# porque puede dificultar identificar de dónde viene
# cada función y generar conflictos de nombres.


print("\nFin de los ejercicios de módulos.")
