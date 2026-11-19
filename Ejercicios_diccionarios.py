
# ============================================================
# PRÁCTICA DE DICCIONARIOS EN PYTHON
# 8 EJERCICIOS RESUELTOS - DE BÁSICO A AVANZADO
# ============================================================

# OBJETIVO:
# Aplicar los conocimientos sobre diccionarios:
#
# - Creación y consulta.
# - Modificación y eliminación.
# - Bucles for.
# - Listas dentro de diccionarios.
# - Diccionarios anidados.
# - Condicionales if.
# - Inventarios y cálculos.
# - Claves hashables.
#
# Cada ejercicio contiene:
# 1. Enunciado.
# 2. Solución.
# 3. Explicación.
# 4. Resultado esperado.


# ============================================================
# NIVEL 1 - FUNDAMENTOS
# ============================================================

# EJERCICIO 1:
# Crear un diccionario llamado libro con:
# título, autor, año y precio.
#
# Consultar sus valores, sus claves y contar sus elementos.


# SOLUCIÓN:

libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967,
    "precio": 45000
}

# Mostrar el diccionario completo.
print("Libro:", libro)

# Consultar valores individuales.
print("Título:", libro["titulo"])
print("Autor:", libro["autor"])
print("Año:", libro["año"])
print("Precio:", libro["precio"])

# Consultar todas las claves.
print("Claves:", libro.keys())

# Consultar todos los valores.
print("Valores:", libro.values())

# Consultar todos los pares clave-valor.
print("Elementos:", libro.items())

# Contar elementos.
print("Cantidad de propiedades:", len(libro))

# EXPLICACIÓN:
#
# libro["titulo"] -> Consulta el valor de una clave.
# keys()          -> Devuelve las claves.
# values()        -> Devuelve los valores.
# items()         -> Devuelve pares clave-valor.
# len()           -> Cuenta las propiedades.
#
# RESULTADO ESPERADO:
# Título: Cien años de soledad
# Autor: Gabriel García Márquez
# Año: 1967
# Precio: 45000
# Cantidad de propiedades: 4


print("-" * 50)


# ============================================================
# NIVEL 2 - MODIFICACIONES
# ============================================================

# EJERCICIO 2:
# Crear un diccionario de un celular.
#
# 1. Cambiar su precio.
# 2. Agregar el color.
# 3. Eliminar una propiedad.


# SOLUCIÓN:

celular = {
    "marca": "Samsung",
    "modelo": "Galaxy A35",
    "precio": 1200000,
    "almacenamiento": "128 GB"
}

print("Celular original:", celular)

# 1. Modificar el precio.
celular["precio"] = 1100000

print("Precio actualizado:", celular["precio"])

# 2. Agregar una nueva propiedad.
celular["color"] = "Negro"

print("Celular con color:", celular)

# 3. Eliminar almacenamiento.
celular.pop("almacenamiento")

print("Celular después de eliminar:", celular)

# 4. Modificar varios datos con update().
celular.update({
    "precio": 1050000,
    "color": "Azul"
})

print("Celular actualizado con update():", celular)

# EXPLICACIÓN:
#
# diccionario["clave"] = valor
# -> Agrega o modifica una propiedad.
#
# pop("clave")
# -> Elimina una propiedad específica.
#
# update()
# -> Modifica o agrega varios elementos.
#
# RESULTADO FINAL:
# {
#   'marca': 'Samsung',
#   'modelo': 'Galaxy A35',
#   'precio': 1050000,
#   'color': 'Azul'
# }


print("-" * 50)


# ============================================================
# NIVEL 3 - BUCLES FOR
# ============================================================

# EJERCICIO 3:
# Crear un diccionario con las notas de tres materias.
#
# Recorrer:
# 1. Las claves.
# 2. Los valores.
# 3. Los pares clave-valor.


# SOLUCIÓN:

notas = {
    "Matematicas": 4.5,
    "Ingles": 4.2,
    "Python": 5.0
}

# 1. Recorrer las claves.
print("MATERIAS:")

for materia in notas:
    print(materia)

# 2. Recorrer los valores.
print("\nCALIFICACIONES:")

for calificacion in notas.values():
    print(calificacion)

# 3. Recorrer claves y valores.
print("\nMATERIAS Y CALIFICACIONES:")

for materia, calificacion in notas.items():
    print(materia, ":", calificacion)

# 4. Calcular el promedio.
suma_notas = 0

for calificacion in notas.values():
    suma_notas += calificacion

promedio = suma_notas / len(notas)

print("Promedio:", round(promedio, 2))

# EXPLICACIÓN:
#
# for materia in notas:
# -> Recorre las claves.
#
# for nota in notas.values():
# -> Recorre los valores.
#
# for clave, valor in notas.items():
# -> Recorre pares clave-valor.
#
# += acumula valores.
# len(notas) indica la cantidad de materias.
#
# RESULTADO:
# Matematicas: 4.5
# Ingles: 4.2
# Python: 5.0
# Promedio: 4.57


print("-" * 50)


# ============================================================
# NIVEL 4 - LISTAS DENTRO DE DICCIONARIOS
# ============================================================

# EJERCICIO 4:
# Crear un diccionario llamado estudiante.
#
# Debe contener:
# - Nombre.
# - Edad.
# - Lista de cursos.
#
# Consultar el segundo curso y agregar uno nuevo.


# SOLUCIÓN:

estudiante = {
    "nombre": "Daniel",
    "edad": 28,
    "cursos": ["Python", "SQL", "Excel"]
}

print("Estudiante:", estudiante)

# Consultar todos los cursos.
print("Cursos:", estudiante["cursos"])

# Consultar el segundo curso.
print("Segundo curso:", estudiante["cursos"][1])

# Agregar un nuevo curso.
estudiante["cursos"].append("Power BI")

print("Cursos actualizados:", estudiante["cursos"])

# Modificar el primer curso.
estudiante["cursos"][0] = "Python Avanzado"

print("Cursos modificados:", estudiante["cursos"])

# Recorrer los cursos.
print("\nCURSOS DEL ESTUDIANTE:")

for curso in estudiante["cursos"]:
    print(curso)

# EXPLICACIÓN:
#
# estudiante["cursos"]
# -> Accede a la lista.
#
# estudiante["cursos"][1]
# -> Accede al segundo elemento.
#
# append()
# -> Agrega un curso al final.
#
# estudiante["cursos"][0] = ...
# -> Modifica el primer elemento.
#
# RESULTADO FINAL:
# ['Python Avanzado', 'SQL', 'Excel', 'Power BI']


print("-" * 50)


# ============================================================
# NIVEL 5 - DICCIONARIOS ANIDADOS
# ============================================================

# EJERCICIO 5:
# Crear una tienda con dos categorías.
#
# Cada categoría debe contener dos productos.
#
# Agregar un nuevo producto sin reemplazar los anteriores.


# SOLUCIÓN:

tienda = {
    "tecnologia": {
        "producto1": "Computador",
        "producto2": "Mouse"
    },
    "papeleria": {
        "producto1": "Cuaderno",
        "producto2": "Lapiz"
    }
}

print("Tienda original:", tienda)

# Consultar un producto específico.
print("Primer producto de tecnología:",
      tienda["tecnologia"]["producto1"])

# Agregar un tercer producto a tecnología.
tienda["tecnologia"]["producto3"] = "Teclado"

# Agregar un tercer producto a papelería.
tienda["papeleria"]["producto3"] = "Borrador"

print("Tienda actualizada:", tienda)

# Recorrer las categorías y sus productos.
print("\nPRODUCTOS DE LA TIENDA:")

for categoria, productos in tienda.items():

    print("\nCategoría:", categoria)

    for codigo, nombre in productos.items():
        print(codigo, ":", nombre)

# EXPLICACIÓN:
#
# tienda["tecnologia"]["producto3"] = "Teclado"
#
# Primero accedemos al diccionario "tecnologia".
# Luego agregamos una nueva clave.
#
# No reemplazamos el diccionario interno.
#
# El primer for recorre las categorías.
# El segundo for recorre los productos.


print("-" * 50)


# ============================================================
# NIVEL 6 - FAMILIA Y BUCLES ANIDADOS
# ============================================================

# EJERCICIO 6:
# Crear una familia con tres integrantes.
#
# Cada integrante debe tener:
# - Nombre.
# - Edad.
#
# Imprimir solamente los integrantes mayores de 10 años.


# SOLUCIÓN:

familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 15
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 12
    }
}

print("Integrantes mayores de 10 años:")

for hijo, datos in familia.items():

    if datos["edad"] > 10:

        print(
            datos["nombre"],
            "tiene",
            datos["edad"],
            "años"
        )

# RESULTADO:
# Ana tiene 15 años
# Marcelo tiene 12 años

# EXPLICACIÓN:
#
# familia.items() devuelve cada hijo y sus datos.
#
# datos["edad"] consulta la edad.
#
# if datos["edad"] > 10:
# Comprueba si la edad es mayor que 10.
#
# Si se cumple, ejecuta print().


# EJEMPLO ADICIONAL:
# Mostrar todos los integrantes con sus propiedades.

print("\nINFORMACIÓN COMPLETA DE LA FAMILIA:")

for hijo, datos in familia.items():

    print("\n", hijo)

    for clave, valor in datos.items():
        print(clave, ":", valor)

# Aquí utilizamos dos bucles for anidados.


print("-" * 50)


# ============================================================
# NIVEL 7 - INVENTARIOS
# ============================================================

# EJERCICIO 7:
# Crear un inventario de tres productos.
#
# Cada producto debe contener:
# - Nombre.
# - Precio.
# - Cantidad.
#
# Calcular:
# 1. El valor de cada producto.
# 2. El valor total del inventario.


# SOLUCIÓN:

inventario = {
    "P001": {
        "nombre": "Tornillo",
        "precio": 1500,
        "cantidad": 20
    },
    "P002": {
        "nombre": "Tuerca",
        "precio": 800,
        "cantidad": 50
    },
    "P003": {
        "nombre": "Arandela",
        "precio": 500,
        "cantidad": 100
    }
}

# Variable acumuladora.
valor_total_inventario = 0

print("REPORTE DE INVENTARIO:")

for codigo, producto in inventario.items():

    # Calculamos el subtotal.
    subtotal = producto["precio"] * producto["cantidad"]

    # Acumulamos el valor.
    valor_total_inventario += subtotal

    # Mostramos información.
    print("\nCódigo:", codigo)
    print("Producto:", producto["nombre"])
    print("Precio unitario:", producto["precio"])
    print("Cantidad:", producto["cantidad"])
    print("Subtotal:", subtotal)

print("\nVALOR TOTAL DEL INVENTARIO:",
      valor_total_inventario)

# RESULTADOS:
#
# Tornillo:
# 1500 * 20 = 30000
#
# Tuerca:
# 800 * 50 = 40000
#
# Arandela:
# 500 * 100 = 50000
#
# TOTAL: 120000


# EJEMPLO ADICIONAL:
# Buscar productos con inventario inferior a 30 unidades.

print("\nPRODUCTOS CON MENOS DE 30 UNIDADES:")

for codigo, producto in inventario.items():

    if producto["cantidad"] < 30:
        print(producto["nombre"], producto["cantidad"])

# RESULTADO:
# Tornillo 20

# EXPLICACIÓN:
#
# Utilizamos:
# - Diccionarios anidados.
# - Bucles for.
# - Operaciones aritméticas.
# - Acumuladores.
# - Condicionales if.


print("-" * 50)


# ============================================================
# NIVEL 8 - CLAVES HASHABLES Y ESTRUCTURAS
# ============================================================

# EJERCICIO 8:
# Crear un diccionario vacío.
#
# Agregar tres claves de distintos tipos hashables.
#
# Después volver a asignar una clave existente
# y comprobar qué ocurre.


# SOLUCIÓN:

registros = {}

print("Diccionario inicial:", registros)

# Primera clave: cadena de texto (str).
registros["nombre"] = "Daniel"

# Segunda clave: número entero (int).
registros[1001] = "Código de empleado"

# Tercera clave: tupla (tuple).
registros[(2026, 11)] = "Periodo noviembre"

print("Diccionario con registros:", registros)

# Consultar las claves.
print("Claves:", registros.keys())

# Consultar valores.
print("Valores:", registros.values())

# Modificar una clave existente.
registros["nombre"] = "Carlos"

print("Diccionario actualizado:", registros)

# RESULTADO:
# La clave "nombre" conserva su posición.
# Su valor cambia de Daniel a Carlos.
#
# No se crea una segunda clave "nombre".


# ------------------------------------------------------------
# EJEMPLO ADICIONAL: CLAVE NO HASHABLE
# ------------------------------------------------------------

# Las listas no pueden utilizarse como claves.
#
# EJEMPLO INCORRECTO:
#
# registros[[1, 2]] = "Lista"
#
# Esto genera:
# TypeError: unhashable type: 'list'


# Podemos observar el error sin detener el programa.

try:
    registros[[1, 2]] = "Lista"

except TypeError:
    print("Error: una lista no puede ser clave de un diccionario.")


# ------------------------------------------------------------
# EJEMPLO ADICIONAL: HASH DE LAS CLAVES
# ------------------------------------------------------------

print("Hash del texto:", hash("nombre"))
print("Hash del entero:", hash(1001))
print("Hash de la tupla:", hash((2026, 11)))

# APUNTE:
#
# Las claves de los diccionarios deben ser hashables.
#
# TIPOS COMUNES:
# str   -> Sí.
# int   -> Sí.
# float -> Sí.
# bool  -> Sí.
# tuple -> Sí, si sus elementos son hashables.
#
# list -> No.
# dict -> No.
# set  -> No.


print("-" * 50)


# ============================================================
# RESUMEN FINAL DE LA PRÁCTICA
# ============================================================

# NIVEL 1:
# Creación, consultas, keys(), values(), items() y len().
#
# NIVEL 2:
# Modificar, agregar, update() y pop().
#
# NIVEL 3:
# Recorrer claves, valores y pares con for.
#
# NIVEL 4:
# Trabajar con listas dentro de diccionarios.
#
# NIVEL 5:
# Crear y modificar diccionarios anidados.
#
# NIVEL 6:
# Combinar diccionarios, for e if.
#
# NIVEL 7:
# Calcular inventarios mediante acumuladores.
#
# NIVEL 8:
# Trabajar con claves hashables y errores.


# ============================================================
# RECOMENDACIONES DE ESTUDIO
# ============================================================

# 1. Ejecuta primero cada ejercicio por separado.
# 2. Cambia los valores para observar diferencias.
# 3. Intenta anticipar el resultado antes de ejecutarlo.
# 4. Practica escribir los diccionarios sin copiar.
# 5. Respeta la indentación de los bucles y condicionales.
# 6. Utiliza nombres descriptivos para tus variables.
# 7. Aprende a interpretar los errores de Python.
# 8. Repite los ejercicios modificando los datos.


print("\n¡Felicitaciones! Terminaste las 8 prácticas.")
print("Fin de la práctica de diccionarios en Python.")
