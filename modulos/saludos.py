
# ============================================================
# MÓDULO DE SALUDOS
# Archivo: saludos.py
# ============================================================

# Este módulo contiene funciones relacionadas con mensajes.


# ============================================================
# NIVEL 1 - FUNCIÓN SIN PARÁMETROS
# ============================================================

def bienvenida():
    return "Bienvenido a mi proyecto de Python"


# ============================================================
# NIVEL 2 - FUNCIÓN CON UN PARÁMETRO
# ============================================================

def saludar(nombre):
    return f"Hola {nombre}, bienvenido a Python"


# ============================================================
# NIVEL 3 - FUNCIÓN CON DOS PARÁMETROS
# ============================================================

def presentacion(nombre, edad):
    return f"Mi nombre es {nombre} y tengo {edad} años"


# ============================================================
# NIVEL 4 - FUNCIÓN CON CONDICIONES
# ============================================================

def clasificar_edad(edad):

    if edad < 0:
        return "Edad no válida"

    elif edad < 18:
        return "Menor de edad"

    else:
        return "Mayor de edad"


# ============================================================
# NIVEL 5 - PARÁMETROS PREDETERMINADOS
# ============================================================

def despedida(nombre="Estudiante"):
    return f"Hasta pronto, {nombre}"


# APUNTES:
#
# f"..." permite insertar variables en un texto.
#
# return devuelve el texto para utilizarlo
# desde cualquier otro archivo.
