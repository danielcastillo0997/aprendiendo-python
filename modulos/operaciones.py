
# ============================================================
# MÓDULO: OPERACIONES MATEMÁTICAS
# Archivo: operaciones.py
# ============================================================

# Un módulo es un archivo .py que contiene código reutilizable.
#
# Podemos importar sus funciones desde otros archivos.
#
# CONCEPTOS:
# def    -> Define una función.
# return -> Devuelve un resultado.
# import -> Permite utilizar código de otro módulo.


# ============================================================
# NIVEL 1 - OPERACIONES BÁSICAS
# ============================================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"


# ============================================================
# NIVEL 2 - OPERACIONES ADICIONALES
# ============================================================

def potencia(base, exponente):
    return base ** exponente


def cuadrado(numero):
    return numero ** 2


def cubo(numero):
    return numero ** 3


def promedio(a, b, c):
    return (a + b + c) / 3


def es_par(numero):
    return numero % 2 == 0


# ============================================================
# NIVEL 3 - FUNCIONES CON VALORES PREDETERMINADOS
# ============================================================

def calcular_total(precio, cantidad=1):
    return precio * cantidad


# Si no proporcionamos cantidad, Python utiliza 1.


# ============================================================
# NIVEL 4 - FUNCIÓN QUE UTILIZA OTRAS FUNCIONES
# ============================================================

def calcular_operacion(a, b, operacion):

    if operacion == "sumar":
        return sumar(a, b)

    elif operacion == "restar":
        return restar(a, b)

    elif operacion == "multiplicar":
        return multiplicar(a, b)

    elif operacion == "dividir":
        return dividir(a, b)

    elif operacion == "potencia":
        return potencia(a, b)

    else:
        return "Operación no válida"


# APUNTES:
#
# Este módulo contiene funciones que pueden ser
# llamadas desde otros archivos.
#
# RECOMENDACIÓN:
# Utiliza nombres descriptivos y una función
# para cada tarea específica.
