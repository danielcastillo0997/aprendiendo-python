# ============================================================
# CONJUNTOS (SET) EN PYTHON
# ============================================================

# Un conjunto (set) es una colección de elementos que:
# 1. No permite elementos duplicados.
# 2. No mantiene un orden definido.
# 3. No permite acceder a elementos mediante índices.
# 4. Permite agregar y eliminar elementos.
# 5. Sus elementos deben ser hashables:
#    Un objeto es hashable si Python puede calcular su hash,
#    un valor numérico utilizado para búsquedas eficientes.
#
#    REGLAS DEL HASH:
#    - Su hash debe permanecer estable durante su vida útil.
#    - Si dos objetos son iguales, tienen el mismo hash.
#    - Dos objetos diferentes pueden tener el mismo hash (colisión).
#
#    HASHABLES: str, int, float, bool y tuplas con elementos hashables.
#    NO HASHABLES: list, dict y set.
#
#    IMPORTANTE: Los conjuntos utilizan hashes y comparaciones
#    de igualdad para identificar y evitar duplicados.


# ============================================================
# 1. CREAR UN CONJUNTO
# ============================================================

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}

print("Conjunto de frutas:", frutas)
print("Tipo de dato:", type(frutas))
print("Cantidad de elementos:", len(frutas))

# APUNTE:
# Aunque escribimos "Naranja" dos veces,
# Python solamente conserva una.
# Los elementos pueden aparecer en diferente orden.


# ============================================================
# 2. COMPROBAR SI UN ELEMENTO EXISTE
# ============================================================

print("Manzana" in frutas)
print("Pera" not in frutas)

# in comprueba si un elemento existe.
# not in comprueba si no existe.
# Ambos devuelven True o False.


# ============================================================
# 3. AGREGAR UN ELEMENTO CON ADD()
# ============================================================

frutas.add("Pera")
print("Después de agregar Pera:", frutas)

# add() agrega un elemento.
# Si ya existe, no se duplica.


# ============================================================
# 4. AGREGAR VARIOS ELEMENTOS CON UPDATE()
# ============================================================

frutasTropicales = {"Piña", "Mango"}

frutas.update(frutasTropicales)
print("Después de update:", frutas)

# update() agrega varios elementos.
# Puede recibir conjuntos, listas, tuplas y otros iterables.


# ============================================================
# 5. ELIMINAR ELEMENTOS CON REMOVE()
# ============================================================

frutas.remove("Mango")
print("Después de eliminar Mango:", frutas)

# remove() elimina el elemento indicado.
# Si no existe, genera KeyError.


# ============================================================
# 6. ELIMINAR ELEMENTOS CON DISCARD()
# ============================================================

frutas.discard("Pera")
print("Después de eliminar Pera:", frutas)

# discard() elimina un elemento.
# Si no existe, NO genera error.


# ============================================================
# 7. ELIMINAR UN ELEMENTO CON POP()
# ============================================================

elemento_eliminado = frutas.pop()

print("Elemento eliminado:", elemento_eliminado)
print("Conjunto después de pop:", frutas)

# pop() elimina y devuelve un elemento arbitrario.
# No necesariamente elimina el último.


# ============================================================
# 8. VACIAR EL CONJUNTO CON CLEAR()
# ============================================================

frutas.clear()
print("Conjunto vacío:", frutas)

# clear() elimina todos los elementos.


print("-" * 40)


# ============================================================
# 9. UNIÓN DE CONJUNTOS
# ============================================================

a = {"a", "b", "c"}
b = {"c", "d", "e"}

c = a.union(b)

print("Conjunto A:", a)
print("Conjunto B:", b)
print("Unión:", c)

# union() crea un conjunto con los elementos de ambos.
# No repite elementos.

print("Unión con |:", a | b)


# ============================================================
# 10. INTERSECCIÓN DE CONJUNTOS
# ============================================================

interseccion = a.intersection(b)

print("Intersección:", interseccion)

# Devuelve los elementos comunes entre ambos conjuntos.

print("Intersección con &:", a & b)


# ============================================================
# 11. DIFERENCIA DE CONJUNTOS
# ============================================================

diferencia = a.difference(b)

print("Diferencia A - B:", diferencia)

# Devuelve los elementos de A que no están en B.

print("Diferencia con -:", a - b)


# ============================================================
# 12. DIFERENCIA SIMÉTRICA
# ============================================================

diferencia_simetrica = a.symmetric_difference(b)

print("Diferencia simétrica:", diferencia_simetrica)

# Devuelve los elementos que están en uno u otro,
# pero no en ambos.

print("Diferencia simétrica con ^:", a ^ b)


# ============================================================
# 13. RECORRER UN CONJUNTO CON FOR
# ============================================================

lenguajes = {"Python", "Java", "C++"}

for lenguaje in lenguajes:
    print("Lenguaje:", lenguaje)

# El orden de recorrido no está garantizado.


# ============================================================
# 14. CREAR UN CONJUNTO VACÍO
# ============================================================

conjunto_vacio = set()

print("Conjunto vacío:", conjunto_vacio)
print("Tipo:", type(conjunto_vacio))

# {} crea un diccionario vacío, no un conjunto.

diccionario_vacio = {}

print("Tipo de {}:", type(diccionario_vacio))


# ============================================================
# 15. ELIMINAR DUPLICADOS DE UNA LISTA
# ============================================================

numeros = [1, 2, 2, 3, 3, 4, 5, 5]

numeros_unicos = set(numeros)

print("Lista original:", numeros)
print("Sin duplicados:", numeros_unicos)

# set() elimina duplicados, pero no conserva
# necesariamente el orden original.


# ============================================================
# 16. EJEMPLO PRÁCTICO: ELEMENTOS HASHABLES
# ============================================================

# Los conjuntos pueden contener números, cadenas de texto
# y tuplas cuyos elementos sean hashables.

datos = {"Python", 10, 3.14, ("Daniel", 25)}

print("Conjunto con elementos hashables:", datos)

# Todos estos elementos son hashables.
# Por eso Python permite almacenarlos dentro del set.


# ============================================================
# 17. CONSULTAR EL HASH DE UN ELEMENTO
# ============================================================

nombre = "Daniel"
numero = 25

print("Hash del nombre:", hash(nombre))
print("Hash del número:", hash(numero))

# hash() devuelve un valor entero.
# Para un mismo objeto hashable, su hash permanece estable
# durante su vida útil.
#
# El hash de cadenas de texto puede cambiar
# al reiniciar Python.


# ============================================================
# 18. REGLA: OBJETOS IGUALES, HASHES IGUALES
# ============================================================

numero1 = 10
numero2 = 10.0

print("¿Son iguales?:", numero1 == numero2)
print("Hash del entero:", hash(numero1))
print("Hash del decimal:", hash(numero2))
print("¿Hashes iguales?:", hash(numero1) == hash(numero2))

# Aunque son tipos diferentes (int y float),
# sus valores son iguales.
# Por eso también deben tener hashes iguales.


# ============================================================
# 19. COLISIONES DE HASH
# ============================================================

valor1 = -1
valor2 = -2

print("Hash de -1:", hash(valor1))
print("Hash de -2:", hash(valor2))
print("¿Son iguales?:", valor1 == valor2)

# En CPython, hash(-1) y hash(-2) producen -2.
#
# Una colisión ocurre cuando dos objetos diferentes
# tienen el mismo hash.
#
# Tener el mismo hash NO significa que sean iguales.


# ============================================================
# 20. EJEMPLO DE UN OBJETO NO HASHABLE
# ============================================================

lista_numeros = [10, 20, 30]

# Las listas no son hashables porque son modificables.
#
# Si ejecutamos:
#
# print(hash(lista_numeros))
#
# Python generará:
# TypeError: unhashable type: 'list'

# Para comprobarlo sin detener el programa:

try:
    print(hash(lista_numeros))

except TypeError:
    print("Error: las listas no son hashables.")


# ============================================================
# 21. TUPLAS HASHABLES Y NO HASHABLES
# ============================================================

# Tupla que contiene solamente números.
tupla_valida = (10, 20, 30)

print("Hash de tupla válida:", hash(tupla_valida))

# Tupla que contiene una lista.
tupla_invalida = (10, [20, 30])

try:
    print(hash(tupla_invalida))

except TypeError:
    print("Error: la tupla contiene una lista no hashable.")

# APUNTE:
# Una tupla es hashable solamente cuando todos
# sus elementos también son hashables.


# ============================================================
# APUNTES Y RECOMENDACIONES
# ============================================================

# MÉTODOS DE CONJUNTOS:
#
# add()                  -> Agrega un elemento.
# update()               -> Agrega varios elementos.
# remove()               -> Elimina; genera error si no existe.
# discard()              -> Elimina; no genera error si no existe.
# pop()                  -> Elimina un elemento arbitrario.
# clear()                -> Vacía el conjunto.
# union()                -> Une conjuntos.
# intersection()         -> Elementos en común.
# difference()           -> Elementos exclusivos del primero.
# symmetric_difference() -> Elementos no compartidos.

# CONCEPTOS DE HASH:
#
# hash() -> Calcula el hash de un objeto hashable.
#
# REGLAS:
# 1. Un objeto hashable debe conservar su hash.
# 2. Objetos iguales deben tener hashes iguales.
# 3. Objetos diferentes pueden compartir un hash.
# 4. Los hashes permiten búsquedas eficientes.
#
# RECOMENDACIONES:
# - Utiliza set cuando necesites elementos únicos.
# - No intentes acceder a un set mediante índices.
# - Utiliza discard() si no sabes si existe un elemento.
# - Recuerda que list, dict y set no son hashables.
# - Una tupla con listas tampoco es hashable.
# - Un mismo hash no garantiza igualdad.

print("\nFin de los ejercicios de conjuntos.")