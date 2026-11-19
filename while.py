
# ============================================================
# PYTHON - BUCLES WHILE
# Tema: while, break, continue y else
# ============================================================

# ¿QUÉ ES UN BUCLE WHILE?
# while permite repetir un bloque de código mientras
# una condición sea verdadera (True).
#
# Sintaxis:
#
# while condicion:
#     instrucciones
#
# IMPORTANTE:
# La variable de control debe actualizarse para evitar
# que el bucle se ejecute infinitamente.


# ============================================================
# 1. BUCLE WHILE SIMPLE
# ============================================================

# Objetivo: imprimir los números del 1 al 10.

i = 1  # Inicializamos el contador

while i <= 10:
    print(i)
    i += 1  # Incrementamos el contador en 1

print("Bucle terminado.")

# APUNTES:
# i = 1       -> Valor inicial del contador.
# i <= 10     -> Condición para continuar el bucle.
# print(i)    -> Muestra el valor actual.
# i += 1      -> Equivale a i = i + 1.
#
# SALIDA:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Cada número aparece en una línea diferente.
#
# RECOMENDACIÓN:
# Nunca olvides incrementar el contador cuando
# la condición depende de su valor.
# De lo contrario, puedes crear un bucle infinito.


# ============================================================
# 2. BUCLE WHILE CON NÚMEROS PARES
# ============================================================

# Objetivo: imprimir los números pares del 2 al 20.

print("Bucle de números pares:")

i = 2

while i <= 20:
    print(i)
    i += 2

print("Bucle de números pares terminado.")

# APUNTES:
# Empezamos desde el número 2.
# Incrementamos de 2 en 2.
# Así obtenemos únicamente números pares.
#
# SALIDA:
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
#
# RECOMENDACIÓN:
# Si conocemos el incremento, podemos utilizar
# i += 2, i += 3, etc.
#
# También podemos comprobar si un número es par:
#
# numero % 2 == 0
#
# El operador % devuelve el residuo de una división.
# Si el residuo al dividir entre 2 es cero,
# el número es par.


# ============================================================
# 3. BUCLE WHILE CON BREAK
# ============================================================

# ¿QUÉ HACE BREAK?
# break termina inmediatamente el bucle,
# aunque la condición del while siga siendo verdadera.

print("Bucle con break:")

i = 1

while i <= 10:
    print(i)

    if i >= 5:
        break  # Termina el bucle al llegar a 5

    i += 1

print("Bucle terminado con break.")

# APUNTES:
# El bucle comienza en 1.
# Cuando i llega a 5, se cumple la condición.
# break detiene inmediatamente la ejecución del while.
#
# SALIDA:
# 1, 2, 3, 4, 5
#
# IMPORTANTE:
# break no termina todo el programa.
# Solo termina el bucle en el que se encuentra.
#
# RECOMENDACIÓN:
# Utiliza break cuando encuentres un resultado,
# se cumpla una condición de salida o necesites
# detener una búsqueda.


# ============================================================
# 4. BUCLE WHILE CON CONTINUE
# ============================================================

# ¿QUÉ HACE CONTINUE?
# continue salta las instrucciones restantes
# de la iteración actual y pasa a la siguiente.

print("Bucle con continue:")

i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue  # Omite los números pares

    print(i)

print("Bucle terminado con continue.")

# APUNTES:
# Primero incrementamos el contador.
# Después verificamos si el número es par.
# Si es par, continue omite el print(i).
# Si es impar, se muestra en pantalla.
#
# SALIDA:
# 1, 3, 5, 7, 9
#
# DIFERENCIA IMPORTANTE:
#
# break    -> Termina completamente el bucle.
# continue -> Omite una iteración y continúa el bucle.
#
# RECOMENDACIÓN:
# Actualiza el contador antes de continue
# cuando sea necesario.
#
# Si el contador no cambia, el bucle podría
# ejecutarse infinitamente.


# ============================================================
# 5. BUCLE WHILE CON ELSE
# ============================================================

# ¿QUÉ HACE ELSE EN WHILE?
# El bloque else se ejecuta cuando el bucle
# termina normalmente, sin utilizar break.

print("Bucle con else:")

i = 0

while i < 10:
    i += 1

    if i == 5:
        continue  # Omite el número 5

    print(i)

else:
    print("El bucle ha terminado normalmente.")

# APUNTES:
# El contador comienza en 0.
# Se incrementa hasta llegar a 10.
# Cuando i vale 5, se omite ese número.
# Como nunca utilizamos break, se ejecuta else.
#
# SALIDA:
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# El bucle ha terminado normalmente.
#
# IMPORTANTE:
# continue NO impide que se ejecute else.
# break SÍ impide que se ejecute else.
#
# RECOMENDACIÓN:
# Utiliza while...else cuando necesites saber
# si un proceso terminó normalmente.
#
# Ejemplo práctico:
# Buscar un elemento y mostrar un mensaje
# si se termina la búsqueda sin encontrarlo.


# ============================================================
# 6. BUCLE WHILE CON BREAK Y CONTINUE
# ============================================================

# Objetivo:
# Mostrar números impares y detener el bucle
# cuando el contador llegue a 5.

print("Bucle con break y continue:")

i = 0

while i < 10:
    i += 1

    if i == 5:
        break  # Detiene el bucle

    if i % 2 == 0:
        continue  # Omite números pares

    print(i)

print("Bucle terminado con break y continue.")

# APUNTES:
#
# i = 1 -> Imprime 1.
# i = 2 -> Es par, continue lo omite.
# i = 3 -> Imprime 3.
# i = 4 -> Es par, continue lo omite.
# i = 5 -> Se ejecuta break.
#
# SALIDA:
# 1
# 3
# Bucle terminado con break y continue.
#
# RECOMENDACIÓN:
# El orden de las condiciones es importante.
#
# Primero comprobamos si debemos detener
# el bucle y después si debemos omitir
# alguna iteración.


# ============================================================
# 7. EJEMPLO ADICIONAL: BÚSQUEDA CON WHILE Y ELSE
# ============================================================

# Objetivo: buscar un número dentro de una lista.

numeros = [10, 20, 30, 40, 50]
buscado = 35

indice = 0

while indice < len(numeros):

    if numeros[indice] == buscado:
        print("Número encontrado:", buscado)
        break

    indice += 1

else:
    print("El número no se encontró en la lista.")

# APUNTES:
# len(numeros) obtiene la cantidad de elementos.
# numeros[indice] accede a cada elemento.
# break se ejecuta si encontramos el número.
# else se ejecuta si terminamos sin encontrarlo.
#
# SALIDA:
# El número no se encontró en la lista.


# ============================================================
# FIN DE LOS APUNTES
# ============================================================
