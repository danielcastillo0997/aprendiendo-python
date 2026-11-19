
# ============================================================
# FUNCIONES EN PYTHON - CALCULADORA
# ============================================================

# Una función es un bloque de código reutilizable
# que realiza una tarea específica.
#
# CONCEPTOS:
#
# def    -> Define una función.
# a, b   -> Parámetros que recibe la función.
# return -> Devuelve un resultado.
# pass   -> No realiza ninguna acción; es un marcador vacío.
#
# VENTAJAS:
# 1. Evita repetir código.
# 2. Facilita organizar programas.
# 3. Permite reutilizar operaciones.
# 4. Facilita corregir errores.


# ============================================================
# NIVEL 1 - NUESTRA PRIMERA FUNCIÓN
# ============================================================

def saludar():
    print("Hola, estoy aprendiendo funciones en Python")


# Llamamos a la función.
saludar()

# APUNTE:
# Crear una función no significa ejecutarla.
# Debemos llamarla utilizando su nombre y paréntesis.


# ============================================================
# NIVEL 2 - FUNCIÓN CON PARÁMETROS
# ============================================================

def saludar_persona(nombre):
    print("Hola", nombre)


saludar_persona("Daniel")
saludar_persona("Ana")

# nombre es un parámetro.
# "Daniel" y "Ana" son argumentos.
#
# PARÁMETRO:
# Variable definida dentro de la declaración de la función.
#
# ARGUMENTO:
# Valor que enviamos cuando llamamos a la función.


# ============================================================
# NIVEL 3 - FUNCIÓN QUE DEVUELVE UN RESULTADO
# ============================================================

def sumar(a, b):
    return a + b


resultado_suma = sumar(5, 3)

print("Suma:", resultado_suma)

# EXPLICACIÓN:
#
# sumar(5, 3) llama a la función.
#
# a recibe 5.
# b recibe 3.
#
# return a + b devuelve 8.
#
# resultado_suma almacena ese resultado.
#
# IMPORTANTE:
# return devuelve un valor.
# print() solamente muestra información en pantalla.


# ============================================================
# NIVEL 4 - FUNCIÓN PARA RESTAR
# ============================================================

def restar(a, b):
    return a - b


resultado_resta = restar(10, 4)

print("Resta:", resultado_resta)

# RESULTADO:
# 6


# ============================================================
# NIVEL 5 - FUNCIÓN PARA MULTIPLICAR
# ============================================================

def multiplicar(a, b):
    return a * b


resultado_multiplicacion = multiplicar(6, 7)

print("Multiplicación:", resultado_multiplicacion)

# RESULTADO:
# 42


# ============================================================
# NIVEL 6 - FUNCIÓN PARA DIVIDIR
# ============================================================

def dividir(a, b):

    # Comprobamos que el divisor no sea cero.
    if b != 0:
        return a / b

    else:
        return "Error: División por cero"


resultado_division = dividir(20, 5)

print("División:", resultado_division)

# RESULTADO:
# 4.0

# APUNTE:
#
# != significa diferente de.
#
# if b != 0 comprueba que el divisor no sea cero.
#
# Una división entre cero genera ZeroDivisionError.
# Por eso utilizamos una condición.


# ============================================================
# NIVEL 7 - FUNCIÓN PARA POTENCIAS
# ============================================================

def potencia(a, b):
    return a ** b


resultado_potencia = potencia(2, 3)

print("Potencia:", resultado_potencia)

# RESULTADO:
# 8
#
# 2 ** 3 significa:
# 2 * 2 * 2 = 8


# ============================================================
# NIVEL 8 - FUNCIÓN VACÍA CON PASS
# ============================================================

def funcion():
    pass


funcion()

# pass permite dejar una función sin instrucciones.
#
# No imprime nada.
# No realiza ninguna operación.
#
# Se utiliza cuando todavía no hemos desarrollado
# el contenido de una función.


# ============================================================
# NIVEL 9 - PROBAR TODAS LAS OPERACIONES
# ============================================================

print("\nCALCULADORA BÁSICA")

print("Suma:", sumar(5, 3))
print("Resta:", restar(10, 4))
print("Multiplicación:", multiplicar(6, 7))
print("División:", dividir(20, 5))
print("Potencia:", potencia(2, 3))

# También podemos llamar directamente a una función
# dentro de print(), sin almacenar antes el resultado.


# ============================================================
# NIVEL 10 - PROBAR LA DIVISIÓN ENTRE CERO
# ============================================================

print("\nPRUEBA DE DIVISIÓN ENTRE CERO")

resultado = dividir(10, 0)

print(resultado)

# RESULTADO:
# Error: División por cero

# La condición impide intentar una división inválida.


# ============================================================
# NIVEL 11 - UTILIZAR VARIABLES COMO ARGUMENTOS
# ============================================================

numero1 = 15
numero2 = 5

print("\nOPERACIONES CON VARIABLES")

print("Suma:", sumar(numero1, numero2))
print("Resta:", restar(numero1, numero2))
print("Multiplicación:", multiplicar(numero1, numero2))
print("División:", dividir(numero1, numero2))
print("Potencia:", potencia(numero1, numero2))

# APUNTE:
# Podemos enviar variables a las funciones.
# No es obligatorio escribir números directamente.


# ============================================================
# NIVEL 12 - PARÁMETROS CON VALORES PREDETERMINADOS
# ============================================================

def calcular_precio(precio, impuesto=0.19):
    return precio * (1 + impuesto)


precio_final = calcular_precio(100000)

print("\nPrecio con impuesto:", precio_final)

# Si no enviamos el segundo argumento,
# Python utiliza el valor predeterminado de 0.19.

# También podemos enviar otro valor.

precio_final = calcular_precio(100000, 0.05)

print("Precio con impuesto del 5%:", precio_final)


# ============================================================
# NIVEL 13 - FUNCIÓN QUE DEVUELVE VARIOS RESULTADOS
# ============================================================

def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multiplicacion = a * b

    return suma, resta, multiplicacion


resultado = operaciones_basicas(10, 5)

print("\nResultados:", resultado)

# Python devuelve una tupla.
#
# RESULTADO:
# (15, 5, 50)


# Podemos desempaquetar los resultados.

suma, resta, multiplicacion = operaciones_basicas(10, 5)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)


# ============================================================
# NIVEL 14 - CALCULADORA CON OPCIONES
# ============================================================

def calculadora(a, b, operacion):

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


print("\nCALCULADORA CON OPCIONES")

print(calculadora(10, 5, "sumar"))
print(calculadora(10, 5, "restar"))
print(calculadora(10, 5, "multiplicar"))
print(calculadora(10, 5, "dividir"))
print(calculadora(2, 3, "potencia"))

# Esta función reutiliza las funciones anteriores.
#
# Así evitamos repetir las operaciones.


# ============================================================
# NIVEL 15 - CALCULADORA INTERACTIVA
# ============================================================

# Este ejemplo permite ingresar números por teclado.
#
# Se encuentra dentro de otra función para que
# puedas ejecutarlo solamente cuando quieras.


def calculadora_interactiva():

    print("\nCALCULADORA INTERACTIVA")

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")

    opcion = input("Selecciona una opción (1-5): ")

    # Comprobamos que la opción sea válida.
    if opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no válida")
        return

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

    except ValueError:
        print("Error: debes ingresar números válidos.")
        return

    if opcion == "1":
        resultado = sumar(a, b)

    elif opcion == "2":
        resultado = restar(a, b)

    elif opcion == "3":
        resultado = multiplicar(a, b)

    elif opcion == "4":
        resultado = dividir(a, b)

    else:
        resultado = potencia(a, b)

    print("Resultado:", resultado)


# Para probar la calculadora interactiva,
# elimina el símbolo # de la siguiente línea:

# calculadora_interactiva()


# ============================================================
# NIVEL 16 - EJERCICIOS PRÁCTICOS ADICIONALES
# ============================================================


# EJERCICIO A: CALCULAR EL CUADRADO DE UN NÚMERO

def cuadrado(numero):
    return numero ** 2


print("\nCuadrado de 5:", cuadrado(5))


# EJERCICIO B: CALCULAR EL PROMEDIO

def promedio(a, b, c):
    return (a + b + c) / 3


print("Promedio:", promedio(4, 5, 3))


# EJERCICIO C: COMPROBAR SI UN NÚMERO ES PAR

def es_par(numero):
    return numero % 2 == 0


print("¿10 es par?:", es_par(10))
print("¿7 es par?:", es_par(7))

# % calcula el residuo de una división.
# Si el residuo al dividir entre 2 es cero,
# el número es par.


# EJERCICIO D: CALCULAR EL TOTAL DE UNA COMPRA

def total_compra(precio, cantidad):
    return precio * cantidad


print("Total de la compra:", total_compra(1500, 20))


# ============================================================
# APUNTES FINALES
# ============================================================

# def:
# Define una función.
#
# Parámetros:
# Variables declaradas entre los paréntesis.
#
# Argumentos:
# Valores enviados al llamar una función.
#
# return:
# Devuelve un resultado y finaliza la función.
#
# print():
# Muestra información en la consola.
#
# pass:
# Marcador que permite dejar un bloque vacío.
#
# input():
# Solicita información al usuario.
#
# float():
# Convierte un dato numérico compatible a decimal.
#
# try / except:
# Permite manejar determinados errores.
#
# RECOMENDACIONES:
#
# 1. Utiliza nombres descriptivos para tus funciones.
# 2. Escribe una función para cada tarea específica.
# 3. Utiliza return cuando necesites reutilizar un resultado.
# 4. Respeta los cuatro espacios de indentación.
# 5. Evita repetir operaciones innecesariamente.
# 6. Comprueba posibles errores, como dividir entre cero.
# 7. Practica llamando funciones con distintos argumentos.
# 8. Reutiliza funciones para construir programas más grandes.


print("\nFin de los ejercicios de funciones.")
