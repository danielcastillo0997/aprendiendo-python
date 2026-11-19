
# ============================================================
# FUNCIONES LAMBDA EN PYTHON
# ============================================================

# Una función lambda es una función pequeña y anónima.
# "Anónima" significa que no necesita un nombre definido
# mediante def.
#
# SINTAXIS:
# lambda parametros: expresion
#
# CARACTERÍSTICAS:
# 1. Se crea utilizando la palabra lambda.
# 2. Puede recibir varios parámetros.
# 3. Contiene una sola expresión.
# 4. Devuelve automáticamente el resultado.
# 5. Puede utilizarse dentro de otras funciones.


# ============================================================
# NIVEL 1 - FUNCIÓN NORMAL VS FUNCIÓN LAMBDA
# ============================================================

# Función normal con def.

def sumar_normal(a, b):
    return a + b

print("Suma normal:", sumar_normal(5, 3))


# La misma operación utilizando lambda.

sumar_lambda = lambda a, b: a + b

print("Suma con lambda:", sumar_lambda(5, 3))

# RESULTADO:
# Suma normal: 8
# Suma con lambda: 8
#
# DIFERENCIA:
# def permite crear funciones con varias instrucciones.
# lambda utiliza una sola expresión.


# ============================================================
# NIVEL 2 - LAMBDA CON UN PARÁMETRO
# ============================================================

doble = lambda numero: numero * 2

print("Doble de 5:", doble(5))
print("Doble de 10:", doble(10))

# RESULTADO:
# Doble de 5: 10
# Doble de 10: 20

# APUNTE:
# numero recibe el valor enviado.
# La expresión numero * 2 devuelve el resultado.


# ============================================================
# NIVEL 3 - LAMBDA CON VARIOS PARÁMETROS
# ============================================================

multiplicar_lambda = lambda a, b: a * b

print("Multiplicación:", multiplicar_lambda(4, 5))

# RESULTADO:
# 20


# ============================================================
# NIVEL 4 - LAMBDA PARA CALCULAR POTENCIAS
# ============================================================

potencia_lambda = lambda base, exponente: base ** exponente

print("2 elevado a 3:", potencia_lambda(2, 3))
print("5 elevado a 2:", potencia_lambda(5, 2))

# RESULTADO:
# 8
# 25


# ============================================================
# NIVEL 5 - UNA FUNCIÓN QUE DEVUELVE OTRA FUNCIÓN
# ============================================================

# Primero vamos a comprender el concepto utilizando def.

def crear_duplicador():

    def duplicar(numero):
        return numero * 2

    return duplicar


# Guardamos la función que nos devuelve.
duplicador_normal = crear_duplicador()

# Ejecutamos la función que recibimos.
print("Duplicador:", duplicador_normal(5))

# RESULTADO:
# 10
#
# IMPORTANTE:
# return duplicar devuelve la función.
# return duplicar() intentaría ejecutarla sin argumentos.


# ============================================================
# NIVEL 6 - TU EJEMPLO ORIGINAL CON LAMBDA
# ============================================================

def mifuncion(n):
    return lambda a: a * n


duplicador = mifuncion(2)
triplicador = mifuncion(3)
quintuplicador = mifuncion(5)

print(duplicador(5))       # 10
print(triplicador(5))      # 15
print(quintuplicador(5))   # 25

# EXPLICACIÓN:
#
# mifuncion(n) recibe un número que será el multiplicador.
#
# return lambda a: a * n
# devuelve una función que multiplica a por n.
#
# duplicador = mifuncion(2)
# -> Crea una función que multiplica por 2.
#
# triplicador = mifuncion(3)
# -> Crea una función que multiplica por 3.
#
# quintuplicador = mifuncion(5)
# -> Crea una función que multiplica por 5.


# ============================================================
# NIVEL 7 - UTILIZAR LOS MULTIPLICADORES
# ============================================================

print("\nDUPLICADOR")

print(duplicador(2))
print(duplicador(5))
print(duplicador(10))

print("\nTRIPLICADOR")

print(triplicador(2))
print(triplicador(5))
print(triplicador(10))

print("\nQUINTUPLICADOR")

print(quintuplicador(2))
print(quintuplicador(5))
print(quintuplicador(10))

# APUNTE:
# Cada multiplicador conserva el valor de n
# con el que fue creado.
#
# Esto se conoce como closure o cierre.


# ============================================================
# NIVEL 8 - CREAR MÁS MULTIPLICADORES
# ============================================================

multiplicar_por_10 = mifuncion(10)
multiplicar_por_100 = mifuncion(100)

print("10 x 7:", multiplicar_por_10(7))
print("100 x 7:", multiplicar_por_100(7))

# RESULTADO:
# 70
# 700

# Podemos crear diferentes funciones reutilizando
# la misma función mifuncion().


# ============================================================
# NIVEL 9 - LAMBDA CON CONDICIONES
# ============================================================

# Una expresión lambda también puede contener
# una expresión condicional.

es_par_lambda = lambda numero: numero % 2 == 0

print("¿10 es par?:", es_par_lambda(10))
print("¿7 es par?:", es_par_lambda(7))

# RESULTADO:
# True
# False

# Otro ejemplo:

mayor_edad = lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad"

print(mayor_edad(20))
print(mayor_edad(15))

# Una lambda puede utilizar una expresión if-else.


# ============================================================
# NIVEL 10 - LAMBDA CON LISTAS Y MAP()
# ============================================================

numeros = [1, 2, 3, 4, 5]

# map() aplica una función a cada elemento.

numeros_dobles = list(map(lambda n: n * 2, numeros))

print("Lista original:", numeros)
print("Lista duplicada:", numeros_dobles)

# RESULTADO:
# [2, 4, 6, 8, 10]

# APUNTE:
# map() aplica la operación a cada elemento.
# list() convierte el resultado en una lista.


# ============================================================
# NIVEL 11 - LAMBDA CON FILTER()
# ============================================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda n: n % 2 == 0, numeros))

print("Números pares:", pares)

# RESULTADO:
# [2, 4, 6, 8, 10]

# filter() conserva los elementos para los que
# la función devuelve un valor verdadero.


# ============================================================
# NIVEL 12 - LAMBDA PARA ORDENAR DICCIONARIOS
# ============================================================

productos = [
    {"nombre": "Mouse", "precio": 45000},
    {"nombre": "Teclado", "precio": 80000},
    {"nombre": "Monitor", "precio": 600000}
]

# Ordenamos los productos utilizando el precio.

productos_ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"]
)

print("\nPRODUCTOS ORDENADOS POR PRECIO:")

for producto in productos_ordenados:
    print(producto["nombre"], producto["precio"])

# RESULTADO:
# Mouse 45000
# Teclado 80000
# Monitor 600000

# APUNTE:
# sorted() ordena los elementos.
# key indica qué valor se utiliza para ordenar.
# lambda permite extraer el precio de cada producto.


# ============================================================
# APUNTES FINALES SOBRE LAMBDA
# ============================================================

# def:
# Permite crear funciones normales.
#
# lambda:
# Permite crear funciones pequeñas mediante
# una sola expresión.
#
# return:
# En una función def devuelve un resultado.
#
# closure:
# Es una función que conserva acceso a variables
# de su entorno exterior.
#
# map():
# Aplica una función a los elementos de un iterable.
#
# filter():
# Selecciona elementos según una condición.
#
# sorted():
# Permite ordenar elementos utilizando una clave.


# RECOMENDACIONES:
#
# 1. Aprende primero las funciones con def.
# 2. Utiliza lambda para operaciones pequeñas y sencillas.
# 3. Si la lógica es compleja, utiliza def.
# 4. Recuerda que lambda devuelve automáticamente su expresión.
# 5. Una función puede devolver otra función.
# 6. Los closures permiten conservar variables externas.
# 7. Practica map(), filter() y sorted() con listas.
#
# NOTA:
# Por estilo, para funciones con nombre reutilizables,
# normalmente se prefiere def en lugar de asignar
# una lambda directamente a una variable.


print("\nFin de los ejercicios de funciones lambda.")
