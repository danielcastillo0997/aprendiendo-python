# ============================================================
# TUPLAS EN PYTHON
# ============================================================

# Una tupla es una colección de elementos que:
# 1. Es ordenada.
# 2. Es inmutable (no permite cambiar, agregar o eliminar
#    elementos directamente).
# 3. Permite elementos duplicados.
# 4. Puede almacenar diferentes tipos de datos.
# 5. Utiliza índices que comienzan en 0.


# ============================================================
# 1. CREAR UNA TUPLA
# ============================================================

# Índices:          0          1       2        3
tecnologias = ("Python", "Javascript", "Go", "Python")

print("Lista de tecnologías:", tecnologias)

# Acceder a un elemento por su índice
print("Tecnología en la posición 1:", tecnologias[1])

# Consultar el tipo de dato
print("Tipo de dato:", type(tecnologias))

# Python permite valores duplicados dentro de una tupla.
# En este ejemplo, "Python" aparece dos veces.


# ============================================================
# 2. TUPLAS DE UN SOLO ELEMENTO
# ============================================================

# INCORRECTO: Python interpreta esto como un string.
fruta = ("Manzana")

print("Tipo de fruta:", type(fruta))

# CORRECTO: Para crear una tupla con un elemento,
# debemos incluir una coma al final.
fruta = ("Manzana",)

print("Tupla de una fruta:", fruta)
print("Tipo de dato:", type(fruta))

# APUNTE:
# La coma es lo que permite identificar una tupla
# de un solo elemento.


# ============================================================
# 3. TUPLAS CON DIFERENTES TIPOS DE DATOS
# ============================================================

tupla = ("Python", 5, True)

print("Tupla mixta:", tupla)
print("Tipo de dato:", type(tupla))

# Una tupla puede almacenar:
# str   -> cadenas de texto
# int   -> números enteros
# bool  -> valores booleanos


# ============================================================
# 4. DESEMPAQUETADO DE TUPLAS
# ============================================================

# Desempaquetar significa asignar los valores
# de una tupla a diferentes variables.

x, y, z = tupla

print("Valor de x:", x)
print("Valor de y:", y)
print("Valor de z:", z)

# Otro ejemplo tomado de la imagen:

tupla_colores = ("rojo", "verde", "azul")

color1, color2, color3 = tupla_colores

print("Color 1:", color1)
print("Color 2:", color2)
print("Color 3:", color3)

# RECOMENDACIÓN:
# Al desempaquetar, normalmente debe existir
# la misma cantidad de variables que de elementos.


# ============================================================
# 5. UNIR TUPLAS
# ============================================================

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)

tupla3 = tupla1 + tupla2

print("Tupla unida:", tupla3)

# RESULTADO:
# (1, 2, 3, 3, 4, 5)

# El operador + crea una nueva tupla.
# Los valores duplicados se conservan.


# ============================================================
# 6. MULTIPLICAR TUPLAS
# ============================================================

print("Tupla multiplicada:", tupla * 2)

# El operador * repite los elementos de una tupla.
# No multiplica matemáticamente cada elemento.


# ============================================================
# 7. RECORRER UNA TUPLA CON FOR
# ============================================================

print("Elementos de la tupla:")

for item in tupla:
    print(item)

# APUNTE:
# El ciclo for permite recorrer cada elemento.
# La variable item toma un valor diferente
# en cada iteración.


print("-" * 40)


# ============================================================
# 8. MODIFICAR UNA TUPLA INDIRECTAMENTE
# ============================================================

# Las tuplas son inmutables.
# No podemos agregar elementos directamente.

tuplaAModificar = ("Python", "Javascript", "Go")

print("Tupla original:", tuplaAModificar)

# PASO 1: Convertir la tupla en lista.
listaComodin = list(tuplaAModificar)

print("Convertida en lista:", listaComodin)

# PASO 2: Agregar un elemento a la lista.
listaComodin.append("ReactJS")

print("Lista modificada:", listaComodin)

# PASO 3: Convertir nuevamente en tupla.
tuplaAModificar = tuple(listaComodin)

print("Nueva tupla:", tuplaAModificar)

# IMPORTANTE:
# No modificamos la tupla original directamente.
# Creamos una nueva tupla a partir de la lista.


print("-" * 40)


# ============================================================
# 9. CONTAR ELEMENTOS CON LEN()
# ============================================================

tupla_mixta = ("Python", 10, True, 3.14)

print("Tupla mixta:", tupla_mixta)
print("Tipo de dato:", type(tupla_mixta))

print("Cantidad de elementos:", len(tupla_mixta))

# len() devuelve la cantidad de elementos de una tupla.


# ============================================================
# 10. EJEMPLO DE CARROS (IMAGEN)
# ============================================================

Carros = (
    "Lamborghini",
    "Ferrari",
    "Porsche",
    "McLaren",
    "Bugatti",
    "Aston Martin",
    "Maserati",
    "Rolls-Royce",
    "Bentley",
    "Pagani",
    "Koenigsegg"
)

# Mostrar la tupla completa.
print("Tupla de carros:", Carros)

# Consultar el carro en el índice 3.
print("Carro en posición 3:", Carros[3])

# Contar los elementos de la tupla.
print("Cantidad de carros:", len(Carros))

# Ordenar alfabéticamente.
print("Carros ordenados alfabéticamente:", sorted(Carros))

# Consultar el tipo de dato.
print("Tipo de dato:", type(Carros))

# APUNTE:
# sorted() devuelve una LISTA ordenada.
# No modifica la tupla original.

print("-" * 40)


# ============================================================
# 11. OTRO EJEMPLO DE TUPLA CON UN SOLO ELEMENTO
# ============================================================

Carro = ("Dodge Charger",)

print("Tipo de dato:", type(Carro))
print("Tupla:", Carro)

# Una tupla con un solo elemento necesita una coma.


print("-" * 40)


# ============================================================
# 12. COMPROBAR SI UN ELEMENTO EXISTE
# ============================================================

if "Python" in tecnologias:
    print("Python está dentro de la tupla.")

# El operador in permite comprobar la pertenencia.
# Devuelve True o False.


# ============================================================
# 13. ACCEDER A RANGOS DE UNA TUPLA (SLICING)
# ============================================================

numeros = (10, 20, 30, 40, 50)

print("Tupla completa:", numeros)

# Obtener los primeros tres elementos.
print("Primeros tres:", numeros[:3])

# Obtener elementos desde el índice 2.
print("Desde el índice 2:", numeros[2:])

# Obtener una parte de la tupla.
print("Entre índices 1 y 3:", numeros[1:4])

# APUNTE:
# El último índice del rango no se incluye.


# ============================================================
# 14. CONTAR ELEMENTOS REPETIDOS
# ============================================================

print("Veces que aparece Python:",
      tecnologias.count("Python"))

# count() cuenta cuántas veces aparece un valor.


# ============================================================
# 15. BUSCAR LA POSICIÓN DE UN ELEMENTO
# ============================================================

print("Índice de Javascript:",
      tecnologias.index("Javascript"))

# index() devuelve la primera posición donde
# aparece el elemento buscado.


# ============================================================
# APUNTES Y RECOMENDACIONES
# ============================================================

# LISTAS:
# - Se crean con corchetes [].
# - Son mutables.
# - Permiten agregar, eliminar y modificar elementos.

# TUPLAS:
# - Normalmente se crean con paréntesis ().
# - Son inmutables.
# - Permiten duplicados.
# - Conservan el orden.
# - Admiten distintos tipos de datos.

# FUNCIONES Y MÉTODOS IMPORTANTES:
#
# len()    -> Cuenta elementos.
# type()   -> Identifica el tipo de dato.
# tuple()  -> Convierte un iterable en tupla.
# list()   -> Convierte una tupla en lista.
# sorted() -> Devuelve una lista ordenada.
# count()  -> Cuenta apariciones de un elemento.
# index()  -> Busca la primera posición de un elemento.

# RECOMENDACIONES:
# 1. Utiliza listas cuando necesites modificar elementos.
# 2. Utiliza tuplas cuando quieras mantener datos fijos.
# 3. Recuerda que los índices comienzan en 0.
# 4. Usa una coma para crear tuplas de un elemento.
# 5. Respeta la indentación de los bloques for e if.

print("\nFin de los ejercicios de tuplas.")