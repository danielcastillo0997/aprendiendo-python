# bucle for en Python
print("\nLetras de la palabra 'Python':")

palabra = "Python"

for letra in palabra:
    print(letra)
# Este código imprimirá cada letra de la palabra "Python" en una línea separada.


# También podemos usar un bucle for para iterar sobre una lista
meses = ["Enero", "Febrero", "Marzo", "Abril"]

print("\nMeses del año:")
for mes in meses:
    print(mes)
# Este código imprimirá cada mes de la lista en una línea separada.


# También podemos usar un bucle for con la función break para salir del bucle antes de que termine
print("\nLetras hasta la letra 'h':")

for letra in palabra:
    if letra == 'h':
        break
    print(letra)
# Este código imprimirá las letras de "Python" hasta llegar a la letra 'h'.


# Finalmente, podemos usar un bucle for con la función continue para saltar una iteración
print("\nLetras excepto la letra 'o':")

for letra in palabra:
    if letra == 'o':
        continue
    print(letra)
else:
    print("Fin del bucle for.")
# Este código imprimirá las letras de "Python", excepto la letra 'o'.


print("\n ----------------------------- \n")


# bucle for con range en Python
print("Números del 0 al 10:")

# Comenzando desde 0 hasta 10
for numero in range(11):
    print(numero)
# Este código imprimirá los números del 0 al 10, cada uno en una línea separada.


print("\nNúmeros del 5 al 15:")

# Comenzando desde 5 hasta 15
for numero in range(5, 16):
    print(numero)
# Este código imprimirá los números del 5 al 15, cada uno en una línea separada.


print("\nNúmeros pares del 0 al 20:")

# Comenzando desde 0 hasta 20, con un paso de 2 en 2
for numero in range(0, 21, 2):
    print(numero)
# Este código imprimirá los números pares del 0 al 20, cada uno en una línea separada.


print("\nNúmeros impares del 1 al 19:")

# Comenzando desde 1 hasta 19, con un paso de 2
for numero in range(1, 20, 2):
    print(numero)
# Este código imprimirá los números impares del 1 al 19, cada uno en una línea separada.


# break
# Podemos usar break para salir del bucle antes de que termine
print("\nNúmeros del 0 al 10, pero deteniéndose en el 6:")

for numero in range(11):
    if numero == 6:
        break
    print(numero)
# Este código imprimirá los números del 0 al 5, deteniéndose antes de imprimir el 6.


# continue
# Podemos usar continue para saltar una iteración
print("\nNúmeros del 0 al 10, excepto el 5:")

for numero in range(11):
    if numero == 5:
        continue
    print(numero)
# Este código imprimirá los números del 0 al 10, excepto el 5.


print("\n ----------------------------- \n")


# bucle for anidado en Python
print("Tabla de multiplicar del 1 al 5:")

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Línea en blanco para separar las tablas de multiplicar

# Este código imprimirá las tablas de multiplicar del 1 al 5,
# cada una separada por una línea en blanco.


print("Combinaciones de colores y tamaños:")

colores = ["Rojo", "Verde", "Azul"]
tamaños = ["Pequeño", "Mediano", "Grande"]

for color in colores:
    for tamaño in tamaños:
        print(f"{color} - {tamaño}")

# Este código imprimirá todas las combinaciones posibles de colores y tamaños.


print("\n ----------------------------- \n")


# bucle for con else en Python
print("Letras de la palabra 'Python' con else:")

palabra = "Python"

for letra in palabra:
    print(letra)
else:
    print("Fin del bucle for.")

# Este código imprimirá cada letra de la palabra "Python"
# y luego imprimirá "Fin del bucle for." al finalizar el bucle.


# También podemos usar un bucle for con pass en Python
print("\nLetras de la palabra 'Python' con pass:")

for letra in palabra:
    if letra == 'h':
        pass  # No hacer nada cuando la letra es 'h'
    else:
        print(letra)

# Este código imprimirá cada letra de la palabra "Python",
# pero no hará nada cuando la letra sea 'h'.


print("\n ----------------------------- \n")
print("Fin de los ejemplos de bucles for en Python.\n")