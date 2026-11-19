# ============================================================
# BUCLES FOR EN PYTHON - DE LO SIMPLE A LO AVANZADO
# Archivo: for.py
# ============================================================

# 1. PRIMER EJERCICIO: FRUTAS Y ADJETIVOS (FOR ANIDADOS)
# Un bucle anidado es un for dentro de otro for.
# Empezamos con este ejemplo sencillo:

adjetivos = ["Rica", "Saludable"]
frutas = ["manzana", "naranja", "kiwi"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

# RESULTADO:
# manzana Rica
# manzana Saludable
# naranja Rica
# naranja Saludable
# kiwi Rica
# kiwi Saludable
# APUNTES:
# - El for externo elige una fruta.
# - El for interno recorre todos los adjetivos de esa fruta.
# - Hay 3 frutas * 2 adjetivos = 6 combinaciones.
# - La indentacion (4 espacios por nivel) es esencial.

print("\n" + "-" * 40)

# AHORA AMPLIAMOS CON MAS EJEMPLOS DE FOR
# ============================================================

# 2. RECORRER UNA PALABRA
print("\nLetras de la palabra 'Python':")
palabra = "Python"

for letra in palabra:
    print(letra)
# Cada letra aparece en una linea diferente.

# 3. RECORRER UNA LISTA
meses = ["Enero", "Febrero", "Marzo", "Abril"]
print("\nMeses del año:")
for mes in meses:
    print(mes)
# El bucle recorre los elementos de la lista en orden.

# 4. BREAK: DETENER UN BUCLE ANTES DE TERMINAR
print("\nLetras hasta la letra 'h':")
for letra in palabra:
    if letra == "h":
        break
    print(letra)
# Se imprimen P, y, t; el bucle se detiene al encontrar h.

# 5. CONTINUE: SALTAR UNA ITERACION
print("\nLetras excepto la letra 'o':")
for letra in palabra:
    if letra == "o":
        continue
    print(letra)
# Se muestran todas las letras, excepto o.

print("\n" + "-" * 40)

# 6. RANGE(): GENERAR SECUENCIAS DE NUMEROS
print("\nNumeros del 0 al 10:")
for numero in range(11):
    print(numero)
# range(11) produce los numeros del 0 al 10.

print("\nNumeros del 5 al 15:")
for numero in range(5, 16):
    print(numero)
# El limite superior (16) no se incluye.

print("\nNumeros pares del 0 al 20:")
for numero in range(0, 21, 2):
    print(numero)
# El tercer argumento (2) es el paso.

print("\nNumeros impares del 1 al 19:")
for numero in range(1, 20, 2):
    print(numero)

# 7. BREAK CON RANGE()
print("\nNumeros del 0 al 5, deteniendose antes del 6:")
for numero in range(11):
    if numero == 6:
        break
    print(numero)

# 8. CONTINUE CON RANGE()
print("\nNumeros del 0 al 10, excepto el 5:")
for numero in range(11):
    if numero == 5:
        continue
    print(numero)

print("\n" + "-" * 40)

# 9. BUCLES FOR ANIDADOS: TABLAS DE MULTIPLICAR
print("\nTablas de multiplicar del 1 al 5:")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Linea en blanco para separar las tablas.
# El for externo cambia la tabla; el interno multiplica del 1 al 10.

# 10. BUCLES FOR ANIDADOS: COLORES Y TAMANOS
print("Combinaciones de colores y tamaños:")
colores = ["Rojo", "Verde", "Azul"]
tamanos = ["Pequeño", "Mediano", "Grande"]

for color in colores:
    for tamano in tamanos:
        print(f"{color} - {tamano}")
# 3 colores x 3 tamaños = 9 combinaciones.

print("\n" + "-" * 40)

# 11. FOR ... ELSE
print("\nLetras de la palabra 'Python' con else:")
for letra in palabra:
    print(letra)
else:
    print("Fin del bucle for.")
# El else se ejecuta si el for termina sin un break.

# 12. PASS: INSTRUCCION QUE NO HACE NADA
print("\nLetras de 'Python' con pass:")
for letra in palabra:
    if letra == "h":
        pass  # No hace nada; NO salta por si mismo la iteracion.
    else:
        print(letra)
# La h no se imprime porque print esta dentro del else.
# pass por si solo no equivale a continue.

print("\n" + "-" * 40)
print("Fin de los ejemplos de bucles for en Python.\n")

# ============================================================
# RECOMENDACIONES PARA ESTUDIAR
# 1. Ejecuta cada ejercicio y revisa lo que imprime.
# 2. Cambia frutas, adjetivos y numeros para practicar.
# 3. Recuerda: break detiene; continue salta; pass no hace nada.
# 4. range(inicio, fin, paso) no incluye el valor de fin.
# 5. En for anidados, el bucle interno termina sus vueltas
#    antes de que el externo pase al siguiente elemento.
# 6. Utiliza 4 espacios para cada nivel de indentacion.
# ============================================================
