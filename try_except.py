
# ============================================================
# MANEJO DE ERRORES Y EXCEPCIONES EN PYTHON
# ARCHIVO: try_except.py
# ============================================================

# Una excepción es un evento que interrumpe el flujo normal
# de un programa cuando ocurre un error.
#
# Python permite manejar excepciones utilizando:
#
# try     -> Intenta ejecutar un bloque de código.
# except  -> Captura una excepción.
# else    -> Se ejecuta si no ocurre una excepción en try.
# finally -> Se ejecuta al finalizar el bloque.
# raise   -> Permite lanzar excepciones manualmente.
#
# OBJETIVO:
# Aprender a controlar errores sin que el programa
# termine inesperadamente.


# ============================================================
# NIVEL 1 - ERRORES SIN TRY EXCEPT
# ============================================================

# EJEMPLO 1: DIVISIÓN ENTRE CERO

# resultado = 10 / 0
# print(resultado)

# Si ejecutamos el código anterior, Python genera:
#
# ZeroDivisionError: division by zero
#
# Dejamos este ejemplo comentado para que el programa
# pueda continuar ejecutando los siguientes ejercicios.


print("=" * 50)


# ============================================================
# NIVEL 2 - PRIMER TRY EXCEPT
# ============================================================

# EJEMPLO 2: CAPTURAR UNA DIVISIÓN ENTRE CERO

try:
    resultado = 10 / 0

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# EXPLICACIÓN:
#
# 1. Python entra al bloque try.
# 2. Intenta calcular 10 / 0.
# 3. Se genera ZeroDivisionError.
# 4. Python ejecuta el bloque except correspondiente.
# 5. El programa continúa.
#
# RESULTADO:
# Error: No se puede dividir entre cero.


print("=" * 50)


# ============================================================
# NIVEL 3 - TRY EXCEPT SIN ERRORES
# ============================================================

# EJEMPLO 3: DIVISIÓN CORRECTA

try:
    resultado2 = 10 / 2

    print("Resultado:", resultado2)

except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# RESULTADO:
# Resultado: 5.0
#
# Como no ocurrió ningún error,
# el bloque except no se ejecuta.


print("=" * 50)


# ============================================================
# NIVEL 4 - UTILIZAR ELSE
# ============================================================

# EJEMPLO 4: ELSE CUANDO OCURRE UN ERROR

try:
    resultado3 = 10 / 0

except ZeroDivisionError:
    print("No se puede dividir por cero.")

else:
    print("La división se realizó correctamente:", resultado3)

# RESULTADO:
# No se puede dividir por cero.
#
# IMPORTANTE:
# El bloque else NO se ejecuta cuando ocurre una excepción
# dentro del bloque try.


# ------------------------------------------------------------
# EJEMPLO 5: ELSE CUANDO NO OCURRE UN ERROR
# ------------------------------------------------------------

try:
    resultado4 = 10 / 2

except ZeroDivisionError:
    print("No se puede dividir por cero.")

else:
    print("La división se realizó correctamente:", resultado4)

# RESULTADO:
# La división se realizó correctamente: 5.0
#
# APUNTE:
# else se utiliza para ejecutar instrucciones
# cuando el bloque try termina sin excepciones.


print("=" * 50)


# ============================================================
# NIVEL 5 - MANEJAR VALUEERROR
# ============================================================

# EJEMPLO 6: CONVERTIR TEXTO EN NÚMERO

try:
    numero = int("Python")

    print("Número:", numero)

except ValueError:
    print("Error: No se puede convertir ese texto en entero.")

# RESULTADO:
# Error: No se puede convertir ese texto en entero.
#
# int() intenta convertir un valor en número entero.
#
# Si el texto no representa un número válido,
# Python genera ValueError.


# ------------------------------------------------------------
# EJEMPLO 7: CONVERSIÓN CORRECTA
# ------------------------------------------------------------

try:
    numero = int("25")

except ValueError:
    print("Error al convertir.")

else:
    print("Número convertido:", numero)

# RESULTADO:
# Número convertido: 25


print("=" * 50)


# ============================================================
# NIVEL 6 - MÚLTIPLES EXCEPCIONES
# ============================================================

# EJEMPLO 8: VALUEERROR Y ZERODIVISIONERROR

# Este ejemplo corresponde a tu código original.
#
# Vamos a utilizar input() para solicitar información.

# Para ejecutarlo, elimina los símbolos # de estas líneas:

# try:
#     valor = int(input("Ingresa un número entero: "))
#     resultado5 = 10 / valor
#
# except ValueError:
#     print("Error: Debes ingresar un número entero válido.")
#
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.")
#
# else:
#     print("El resultado de la división es:", resultado5)


# APUNTE:
#
# Si escribes "hola", se genera ValueError.
#
# Si escribes 0, se genera ZeroDivisionError.
#
# Si escribes 2, el resultado será 5.0.


# ------------------------------------------------------------
# EJEMPLO 9: MÚLTIPLES EXCEPCIONES SIN INPUT
# ------------------------------------------------------------

valores = ["5", "0", "Python", "2"]

for valor in valores:

    print("\nValor recibido:", valor)

    try:
        numero = int(valor)

        resultado = 10 / numero

    except ValueError:
        print("Error: El valor no es un número entero.")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    else:
        print("Resultado:", resultado)

# RESULTADOS:
#
# Valor 5      -> 2.0
# Valor 0      -> Error de división.
# Valor Python -> Error de conversión.
# Valor 2      -> 5.0
#
# RECOMENDACIÓN:
# Utiliza excepciones específicas para saber
# qué tipo de error ocurrió.


print("=" * 50)


# ============================================================
# NIVEL 7 - CAPTURAR EL MENSAJE DEL ERROR
# ============================================================

# EJEMPLO 10: EXCEPTION AS E

try:
    resultado6 = 10 / 0

except Exception as e:
    print("Ocurrió un error:", e)

# RESULTADO:
# Ocurrió un error: division by zero
#
# EXPLICACIÓN:
#
# Exception es la clase base de muchas excepciones comunes.
#
# as e guarda el objeto de la excepción
# en una variable llamada e.
#
# Así podemos consultar el mensaje del error.
#
# IMPORTANTE:
# Exception no captura absolutamente todos los tipos
# de excepciones de Python.
#
# En programas reales es preferible capturar
# las excepciones específicas que sabemos manejar.


# ------------------------------------------------------------
# EJEMPLO 11: CAPTURAR EXCEPCIÓN CON INPUT
# ------------------------------------------------------------

# Este ejemplo también está basado en tu script original.
#
# Puedes activarlo quitando los comentarios.

# try:
#     valor = int(input("Ingresa un número entero nuevo: "))
#
#     resultado = 10 / valor
#
# except Exception as e:
#     print("Ocurrió un error:", e)
#
# else:
#     print("El resultado de la división es:", resultado)


print("=" * 50)


# ============================================================
# NIVEL 8 - UTILIZAR FINALLY
# ============================================================

# EJEMPLO 12: FINALLY CON ERROR

try:
    resultado = 10 / 0

except ZeroDivisionError:
    print("Se produjo una división entre cero.")

finally:
    print("Finalizó el intento de división.")

# RESULTADO:
#
# Se produjo una división entre cero.
# Finalizó el intento de división.
#
# finally se ejecuta aunque ocurra una excepción.


# ------------------------------------------------------------
# EJEMPLO 13: FINALLY SIN ERROR
# ------------------------------------------------------------

try:
    resultado = 20 / 4

except ZeroDivisionError:
    print("No se puede dividir.")

else:
    print("Resultado correcto:", resultado)

finally:
    print("Operación terminada.")

# RESULTADO:
#
# Resultado correcto: 5.0
# Operación terminada.


print("=" * 50)


# ============================================================
# NIVEL 9 - LANZAR EXCEPCIONES MANUALMENTE
# ============================================================

# EJEMPLO 14: UTILIZAR RAISE

def verificar_edad(edad):

    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    elif edad < 18:
        raise ValueError("Debes ser mayor de edad.")

    else:
        return "Edad válida."


# PROBAMOS DISTINTOS VALORES.

edades = [-5, 15, 18, 25]

for edad in edades:

    try:
        mensaje = verificar_edad(edad)

    except ValueError as e:
        print("Error:", e)

    else:
        print("Edad:", edad, "-", mensaje)

# RESULTADOS:
#
# -5 -> Error: La edad no puede ser negativa.
# 15 -> Error: Debes ser mayor de edad.
# 18 -> Edad válida.
# 25 -> Edad válida.
#
# CORRECCIÓN IMPORTANTE:
#
# En tu ejemplo original aparecía:
#
# elif edad > 18:
#     raise ValueError("Debes ser mayor de edad.")
#
# Esa condición estaba invertida.
#
# Para validar mayoría de edad en este ejercicio
# debemos comprobar edad < 18.
#
# raise genera manualmente una excepción.


# ------------------------------------------------------------
# EJEMPLO 15: VERIFICAR EDAD CON INPUT
# ------------------------------------------------------------

# Puedes activar este ejemplo cuando quieras:

# try:
#     edad_usuario = int(input("Ingresa tu edad: "))
#
#     mensaje = verificar_edad(edad_usuario)
#
#     print(mensaje)
#
# except ValueError as e:
#     print("Error:", e)


print("=" * 50)


# ============================================================
# NIVEL 10 - EXCEPCIONES EN LISTAS
# ============================================================

# EJEMPLO 16: INDEXERROR

frutas = ["Manzana", "Naranja", "Pera"]

try:
    print(frutas[5])

except IndexError:
    print("Error: Esa posición no existe en la lista.")

# RESULTADO:
# Error: Esa posición no existe en la lista.
#
# IndexError ocurre cuando intentamos acceder
# a una posición que no existe.


# ============================================================
# NIVEL 11 - EXCEPCIONES EN DICCIONARIOS
# ============================================================

# EJEMPLO 17: KEYERROR

estudiante = {
    "nombre": "Daniel",
    "edad": 25
}

try:
    print(estudiante["curso"])

except KeyError:
    print("Error: La clave no existe en el diccionario.")

# RESULTADO:
# Error: La clave no existe en el diccionario.
#
# También podemos evitar el error utilizando get().

print("Curso:", estudiante.get("curso", "No registrado"))


print("=" * 50)


# ============================================================
# NIVEL 12 - EXCEPCIONES EN ARCHIVOS
# ============================================================

# EJEMPLO 18: FILENOTFOUNDERROR

try:
    with open("archivo_inexistente_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()

except FileNotFoundError:
    print("Error: No se encontró el archivo solicitado.")

# APUNTE:
#
# FileNotFoundError ocurre cuando intentamos abrir
# un archivo que no existe en la ruta indicada.
#
# with permite administrar correctamente el cierre
# de un archivo cuando se sale de su bloque.


print("=" * 50)


# ============================================================
# NIVEL 13 - FUNCIONES CON MANEJO DE ERRORES
# ============================================================

# EJEMPLO 19: DIVISIÓN SEGURA

def division_segura(a, b):

    try:
        resultado = a / b

    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

    except TypeError:
        return "Error: Los valores deben ser numéricos."

    else:
        return resultado


print("División:", division_segura(10, 2))
print("División:", division_segura(10, 0))
print("División:", division_segura(10, "hola"))

# RESULTADOS:
#
# 5.0
# Error: No se puede dividir entre cero.
# Error: Los valores deben ser numéricos.


print("=" * 50)


# ============================================================
# NIVEL 14 - CALCULADORA CON EXCEPCIONES
# ============================================================

# EJEMPLO 20: CALCULADORA MÁS SEGURA

def calculadora_segura(a, b, operacion):

    try:

        if operacion == "sumar":
            return a + b

        elif operacion == "restar":
            return a - b

        elif operacion == "multiplicar":
            return a * b

        elif operacion == "dividir":
            return a / b

        else:
            raise ValueError("Operación no válida.")

    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."

    except TypeError:
        return "Error: Tipos de datos incompatibles."

    except ValueError as e:
        return f"Error: {e}"


print("Suma:", calculadora_segura(10, 5, "sumar"))

print("Resta:", calculadora_segura(10, 5, "restar"))

print("Multiplicación:",
      calculadora_segura(10, 5, "multiplicar"))

print("División:",
      calculadora_segura(10, 0, "dividir"))

print("Operación incorrecta:",
      calculadora_segura(10, 5, "potencia"))

# APUNTE:
# Podemos combinar funciones, condiciones y excepciones
# para construir programas más resistentes a errores.


# ============================================================
# NIVEL 15 - EJERCICIO PRÁCTICO: INVENTARIO
# ============================================================

# EJEMPLO 21: VALIDAR CANTIDADES

def registrar_producto(nombre, precio, cantidad):

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }


# PROBAMOS EL REGISTRO.

try:
    producto = registrar_producto("Tornillo", 1500, 20)

except ValueError as e:
    print("Error al registrar producto:", e)

else:
    print("Producto registrado:", producto)


# PROBAMOS UN PRODUCTO INVÁLIDO.

try:
    producto = registrar_producto("Tuerca", -500, 10)

except ValueError as e:
    print("Error al registrar producto:", e)

# RESULTADO:
# Error al registrar producto: El precio no puede ser negativo.


print("=" * 50)


# ============================================================
# APUNTES Y RECOMENDACIONES FINALES
# ============================================================

# TIPOS DE EXCEPCIONES:
#
# ZeroDivisionError:
# División entre cero.
#
# ValueError:
# Valor incorrecto para una operación o conversión.
#
# TypeError:
# Tipo de dato incompatible.
#
# IndexError:
# Índice inexistente en una secuencia.
#
# KeyError:
# Clave inexistente en un diccionario.
#
# FileNotFoundError:
# Archivo no encontrado.
#
# Exception:
# Clase base de muchas excepciones habituales.


# ESTRUCTURA COMPLETA:
#
# try:
#     codigo_que_puede_fallar
#
# except TipoDeError:
#     instrucciones_si_ocurre_error
#
# else:
#     instrucciones_si_no_ocurre_error
#
# finally:
#     instrucciones_al_final


# RECOMENDACIONES:
#
# 1. Captura solamente los errores que puedas manejar.
# 2. Prefiere excepciones específicas.
# 3. Evita utilizar except: sin indicar el tipo.
# 4. Utiliza else cuando el código depende del éxito de try.
# 5. Utiliza finally para realizar tareas de limpieza.
# 6. Utiliza raise para validar reglas de tu programa.
# 7. No ocultes errores importantes sin analizarlos.
# 8. Recuerda que un error no siempre requiere try/except:
#    a veces es mejor corregir directamente el código.


print("\nFin de los ejercicios de manejo de excepciones.")
