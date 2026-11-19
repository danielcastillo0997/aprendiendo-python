
# ============================================================
# DICCIONARIOS EN PYTHON - EJERCICIOS ADICIONALES
# ============================================================
#
# OBJETIVO:
# Reforzar los 42 ejercicios del script original.
# Practicar cada concepto con ejemplos diferentes.
#
# METODOLOGÍA:
# 1. Leer el ejemplo.
# 2. Ejecutarlo.
# 3. Observar el resultado.
# 4. Modificar los valores y volver a ejecutarlo.
#
# ============================================================


# ============================================================
# NIVEL 1 - CONCEPTOS BÁSICOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1. CREAR UN DICCIONARIO
# ------------------------------------------------------------

# Ejemplo adicional: información de un país.

pais = {
    "nombre": "Colombia",
    "capital": "Bogotá",
    "idioma": "Español"
}

print("Información del país:", pais)
print("Tipo de dato:", type(pais))

# APUNTE:
# Cada clave identifica un valor.
# Podemos almacenar diferentes propiedades
# relacionadas con un mismo objeto.


# ------------------------------------------------------------
# EJERCICIO 2. ACCEDER A LOS VALORES
# ------------------------------------------------------------

print("Nombre:", pais["nombre"])
print("Capital:", pais["capital"])
print("Idioma:", pais["idioma"])

# RESULTADO:
# Nombre: Colombia
# Capital: Bogotá
# Idioma: Español

# RECOMENDACIÓN:
# Utiliza los nombres exactos de las claves.
# Python distingue entre mayúsculas y minúsculas.


# ------------------------------------------------------------
# EJERCICIO 3. UTILIZAR GET()
# ------------------------------------------------------------

computador = {
    "marca": "Lenovo",
    "memoria": "16 GB"
}

print("Marca:", computador.get("marca"))

# La clave "procesador" no existe.
print("Procesador:", computador.get("procesador"))

# Agregamos un valor predeterminado.
print("Procesador:", computador.get("procesador", "No disponible"))

# RESULTADO:
# Marca: Lenovo
# Procesador: None
# Procesador: No disponible

# get() es útil cuando una clave podría faltar.


# ------------------------------------------------------------
# EJERCICIO 4. CONSULTAR LAS CLAVES CON KEYS()
# ------------------------------------------------------------

producto = {
    "codigo": "A001",
    "nombre": "Mouse",
    "precio": 45000
}

print("Claves:", producto.keys())

# Recorremos las claves.
for clave in producto.keys():
    print("Propiedad:", clave)

# RESULTADO:
# codigo
# nombre
# precio


# ------------------------------------------------------------
# EJERCICIO 5. CONSULTAR LOS VALORES CON VALUES()
# ------------------------------------------------------------

print("Valores:", producto.values())

for valor in producto.values():
    print("Dato:", valor)

# RESULTADO:
# A001
# Mouse
# 45000

# APUNTE:
# values() devuelve una vista de los valores.
# No necesitamos conocer las claves para recorrerlos.


# ------------------------------------------------------------
# EJERCICIO 6. CONSULTAR ITEMS()
# ------------------------------------------------------------

print("Pares clave-valor:", producto.items())

for elemento in producto.items():
    print(elemento)

# RESULTADO:
# ('codigo', 'A001')
# ('nombre', 'Mouse')
# ('precio', 45000)

# items() permite obtener cada par como una tupla.


# ------------------------------------------------------------
# EJERCICIO 7. CONTAR CON LEN()
# ------------------------------------------------------------

pelicula = {
    "titulo": "Avatar",
    "año": 2009,
    "genero": "Ciencia ficción",
    "duracion": 162
}

print("Cantidad de propiedades:", len(pelicula))

# RESULTADO:
# 4

# len() cuenta los pares clave-valor.
# No cuenta las letras ni los caracteres.


# ------------------------------------------------------------
# EJERCICIO 8. COMPROBAR CLAVES CON IN
# ------------------------------------------------------------

print("¿Existe titulo?:", "titulo" in pelicula)
print("¿Existe director?:", "director" in pelicula)

if "genero" in pelicula:
    print("La película tiene un género registrado.")

# RESULTADO:
# True
# False
# La película tiene un género registrado.


# ============================================================
# NIVEL 2 - MODIFICAR DICCIONARIOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 9. MODIFICAR UN VALOR
# ------------------------------------------------------------

estudiante = {
    "nombre": "Carlos",
    "edad": 20
}

estudiante["edad"] = 21

print("Estudiante actualizado:", estudiante)

# Cambiamos solamente el valor de "edad".
# Las demás propiedades permanecen iguales.


# ------------------------------------------------------------
# EJERCICIO 10. AGREGAR UNA CLAVE
# ------------------------------------------------------------

estudiante["ciudad"] = "Bogotá"

print("Estudiante con ciudad:", estudiante)

# Como "ciudad" no existía, Python la agrega.
#
# REGLA:
# Clave existente -> Modifica el valor.
# Clave nueva     -> Agrega un elemento.


# ------------------------------------------------------------
# EJERCICIO 11. MODIFICAR CON UPDATE()
# ------------------------------------------------------------

empleado = {
    "nombre": "Ana",
    "cargo": "Auxiliar",
    "salario": 2000000
}

empleado.update({"salario": 2500000})

print("Salario actualizado:", empleado["salario"])

# update() modifica el valor de una clave existente.


# ------------------------------------------------------------
# EJERCICIO 12. AGREGAR VARIOS ELEMENTOS
# ------------------------------------------------------------

empleado.update({
    "departamento": "Contabilidad",
    "ciudad": "Medellín",
    "activo": True
})

print("Empleado actualizado:", empleado)

# Podemos agregar varias propiedades
# utilizando una sola instrucción update().


# ============================================================
# NIVEL 3 - ELIMINAR ELEMENTOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 13. ELIMINAR CON POP()
# ------------------------------------------------------------

frutas = {
    "fruta1": "Manzana",
    "fruta2": "Pera",
    "fruta3": "Naranja"
}

eliminada = frutas.pop("fruta2")

print("Fruta eliminada:", eliminada)
print("Frutas restantes:", frutas)

# pop() elimina una clave específica.
# También devuelve el valor eliminado.


# ------------------------------------------------------------
# EJERCICIO 14. ELIMINAR CON POPITEM()
# ------------------------------------------------------------

colores = {
    "color1": "Rojo",
    "color2": "Verde",
    "color3": "Azul"
}

eliminado = colores.popitem()

print("Par eliminado:", eliminado)
print("Colores restantes:", colores)

# RESULTADO:
# Par eliminado: ('color3', 'Azul')

# popitem() elimina el último par insertado.


# ------------------------------------------------------------
# EJERCICIO 15. ELIMINAR CON DEL
# ------------------------------------------------------------

animal = {
    "especie": "Perro",
    "nombre": "Max",
    "edad": 5
}

del animal["edad"]

print("Animal sin edad:", animal)

# del elimina una clave y su valor.

# IMPORTANTE:
# Si la clave no existe, genera KeyError.


# ============================================================
# NIVEL 4 - BUCLES FOR
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 16. RECORRER CLAVES
# ------------------------------------------------------------

notas = {
    "matematicas": 4.5,
    "ingles": 4.2,
    "python": 5.0
}

for materia in notas:
    print("Materia:", materia)

# Al recorrer directamente un diccionario
# obtenemos sus claves.


# ------------------------------------------------------------
# EJERCICIO 17. RECORRER VALORES
# ------------------------------------------------------------

for nota in notas.values():
    print("Calificación:", nota)

# values() permite recorrer solamente los valores.


# ------------------------------------------------------------
# EJERCICIO 18. DESEMPAQUETAR CON ITEMS()
# ------------------------------------------------------------

for materia, nota in notas.items():
    print(materia, "tiene una nota de", nota)

# EJEMPLO:
# matematicas tiene una nota de 4.5

# materia recibe la clave.
# nota recibe el valor.


# ------------------------------------------------------------
# EJERCICIO 19. RECORRER SIN DESEMPAQUETAR
# ------------------------------------------------------------

for elemento in notas.items():
    print("Tupla:", elemento)
    print("Clave:", elemento[0])
    print("Valor:", elemento[1])

# Cada elemento es una tupla (clave, valor).
#
# elemento[0] -> Clave.
# elemento[1] -> Valor.


# ============================================================
# NIVEL 5 - ESTRUCTURAS MIXTAS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 20. DIFERENTES TIPOS DE DATOS
# ------------------------------------------------------------

usuario = {
    "nombre": "Daniel",
    "edad": 28,
    "activo": True,
    "estatura": 1.72,
    "habilidades": ["Python", "SQL", "Excel"]
}

print("Información del usuario:", usuario)

# Este diccionario contiene:
# str, int, bool, float y list.


# ------------------------------------------------------------
# EJERCICIO 21. ACCEDER A UNA LISTA INTERNA
# ------------------------------------------------------------

print("Primera habilidad:", usuario["habilidades"][0])
print("Segunda habilidad:", usuario["habilidades"][1])
print("Tercera habilidad:", usuario["habilidades"][2])

# Primero accedemos a la clave "habilidades".
# Después utilizamos el índice de la lista.


# ------------------------------------------------------------
# EJERCICIO 22. MODIFICAR UNA LISTA INTERNA
# ------------------------------------------------------------

usuario["habilidades"].append("Power BI")

print("Habilidades actualizadas:", usuario["habilidades"])

# append() agrega un nuevo elemento a la lista.

usuario["habilidades"].remove("Excel")

print("Después de eliminar Excel:", usuario["habilidades"])

# Podemos utilizar los métodos de listas
# cuando el valor de una clave es una lista.


# ============================================================
# NIVEL 6 - DICCIONARIOS ANIDADOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 23. CREAR DICCIONARIOS ANIDADOS
# ------------------------------------------------------------

vehiculos = {
    "auto1": {
        "marca": "Toyota",
        "modelo": "Corolla"
    },
    "auto2": {
        "marca": "Mazda",
        "modelo": "CX-5"
    }
}

print("Vehículos:", vehiculos)

# Cada vehículo es un diccionario interno.


# ------------------------------------------------------------
# EJERCICIO 24. ACCEDER A VALORES INTERNOS
# ------------------------------------------------------------

print("Marca del primer auto:",
      vehiculos["auto1"]["marca"])

print("Modelo del segundo auto:",
      vehiculos["auto2"]["modelo"])

# RESULTADO:
# Toyota
# CX-5

# Utilizamos dos claves para llegar al valor.


# ============================================================
# NIVEL 7 - ÚTILES ESCOLARES
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 25. DICCIONARIO DE ÚTILES
# ------------------------------------------------------------

utiles = {
    "cuadernos": {
        "matematicas": "Cuadriculado",
        "español": "Rayado"
    },
    "lapices": {
        "negro": "HB",
        "dibujo": "2B"
    }
}

print("Útiles escolares:", utiles)


# ------------------------------------------------------------
# EJERCICIO 26. CONSULTAR UN VALOR ANIDADO
# ------------------------------------------------------------

print("Cuaderno de matemáticas:",
      utiles["cuadernos"]["matematicas"])

# RESULTADO:
# Cuadriculado


# ------------------------------------------------------------
# EJERCICIO 27. REEMPLAZAR CON UPDATE()
# ------------------------------------------------------------

# Creamos una copia con un diccionario interno nuevo.
# Así conservamos el ejemplo original para estudiarlo.

utiles_copia = {
    "cuadernos": utiles["cuadernos"].copy(),
    "lapices": utiles["lapices"].copy()
}

utiles_copia.update({"cuadernos": "Cuaderno nuevo"})

print("Después de update:", utiles_copia)

# ATENCIÓN:
# Se reemplaza el diccionario interno completo
# por el texto "Cuaderno nuevo".


# ------------------------------------------------------------
# EJERCICIO 28. AGREGAR UNA CLAVE INTERNA
# ------------------------------------------------------------

utiles["cuadernos"]["ingles"] = "Rayado"

print("Cuadernos actualizados:", utiles["cuadernos"])

# Aquí conservamos el diccionario interno
# y agregamos una propiedad nueva.


# ------------------------------------------------------------
# EJERCICIO 29. CONSULTAR CLAVES PRINCIPALES
# ------------------------------------------------------------

print("Categorías:", utiles.keys())

for categoria in utiles.keys():
    print("Categoría escolar:", categoria)

# RESULTADO:
# cuadernos
# lapices


# ============================================================
# NIVEL 8 - FAMILIA Y BUCLES ANIDADOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 30. DICCIONARIO FAMILIAR
# ------------------------------------------------------------

familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print("Familia:", familia)


# ------------------------------------------------------------
# EJERCICIO 31. ACCEDER A UN HIJO
# ------------------------------------------------------------

print("Primer hijo:", familia["hijo1"]["nombre"])
print("Edad del segundo hijo:", familia["hijo2"]["edad"])

# Accedemos a un diccionario interno
# y después a una propiedad específica.


# ------------------------------------------------------------
# EJERCICIO 32. RECORRER ITEMS() CON ÍNDICES
# ------------------------------------------------------------

for hijo in familia.items():

    print("\n", hijo[0])

    for dato in hijo[1].items():
        print(dato[0], dato[1])

# hijo[0] -> Clave principal.
# hijo[1] -> Diccionario interno.
#
# dato[0] -> Propiedad.
# dato[1] -> Valor de la propiedad.


# ------------------------------------------------------------
# EJERCICIO 33. DESEMPAQUETADO DIRECTO
# ------------------------------------------------------------

for hijo, datos in familia.items():

    print("\n", hijo)

    for clave, valor in datos.items():
        print(clave, valor)

# Esta forma utiliza nombres descriptivos.
# Es más legible que acceder mediante [0] y [1].


# ------------------------------------------------------------
# EJERCICIO 34. CONSULTAR DATOS ESPECÍFICOS
# ------------------------------------------------------------

for hijo, datos in familia.items():

    print(
        datos["nombre"],
        "tiene",
        datos["edad"],
        "años"
    )

# También podemos aplicar condiciones.

for hijo, datos in familia.items():

    if datos["edad"] >= 7:
        print(datos["nombre"], "tiene 7 años o más.")

# Aquí combinamos:
# Diccionarios + for + if.


# ============================================================
# NIVEL 9 - COPIAR Y VACIAR
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 35. COPIAR CON COPY()
# ------------------------------------------------------------

original = {
    "nombre": "Ana",
    "edad": 25
}

copia = original.copy()

copia["edad"] = 30

print("Original:", original)
print("Copia:", copia)

# RESULTADO:
# El original conserva edad 25.
# La copia tiene edad 30.
#
# copy() crea una copia superficial.


# ------------------------------------------------------------
# EJERCICIO 36. VACIAR CON CLEAR()
# ------------------------------------------------------------

datos = {
    "nombre": "Carlos",
    "ciudad": "Bogotá"
}

print("Antes de clear:", datos)

datos.clear()

print("Después de clear:", datos)

# RESULTADO:
# {}

# clear() elimina todos los elementos.
# No elimina la variable.


# ============================================================
# NIVEL 10 - INVENTARIOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 37. PRODUCTO INDIVIDUAL
# ------------------------------------------------------------

producto = {
    "nombre": "Teclado",
    "precio": 80000,
    "cantidad": 5
}

total = producto["precio"] * producto["cantidad"]

print("Producto:", producto["nombre"])
print("Valor del inventario:", total)

# RESULTADO:
# 400000

# Este ejercicio combina diccionarios
# y operaciones aritméticas.


# ------------------------------------------------------------
# EJERCICIO 38. INVENTARIO CON VARIOS PRODUCTOS
# ------------------------------------------------------------

inventario = {
    "P001": {
        "nombre": "Mouse",
        "precio": 45000,
        "cantidad": 10
    },
    "P002": {
        "nombre": "Monitor",
        "precio": 600000,
        "cantidad": 3
    },
    "P003": {
        "nombre": "Teclado",
        "precio": 80000,
        "cantidad": 5
    }
}

for codigo, producto in inventario.items():

    print("\nCódigo:", codigo)
    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"])
    print("Cantidad:", producto["cantidad"])

# El bucle externo recorre los productos.


# ------------------------------------------------------------
# EJERCICIO 39. ACUMULAR EL TOTAL
# ------------------------------------------------------------

valor_total = 0

for producto in inventario.values():

    subtotal = producto["precio"] * producto["cantidad"]

    valor_total += subtotal

    print("Subtotal:", producto["nombre"], subtotal)

print("Valor total del inventario:", valor_total)

# RESULTADO:
# Mouse:   450000
# Monitor: 1800000
# Teclado: 400000
#
# TOTAL: 2650000

# += permite acumular cantidades.
#
# valor_total += subtotal
#
# Equivale a:
#
# valor_total = valor_total + subtotal


# ============================================================
# NIVEL 11 - CLAVES Y TIPOS DE DICCIONARIOS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 40. CLAVES HASHABLES
# ------------------------------------------------------------

registros = {
    "usuario": "Daniel",
    1001: "Código de empleado",
    (2026, 11): "Periodo"
}

print("Diccionario:", registros)

print("Código:", registros[1001])
print("Periodo:", registros[(2026, 11)])

# Las claves deben ser hashables.
#
# str -> Sí.
# int -> Sí.
# tuple -> Sí, si sus elementos son hashables.
#
# list -> No.


# ------------------------------------------------------------
# EJERCICIO 41. CLAVES DUPLICADAS
# ------------------------------------------------------------

precios = {
    "manzana": 2000,
    "pera": 3000,
    "manzana": 2500
}

print("Precios:", precios)

# RESULTADO:
# {'manzana': 2500, 'pera': 3000}
#
# Una clave no puede aparecer dos veces como
# entrada independiente.
#
# La última asignación reemplaza el valor anterior.


# ------------------------------------------------------------
# EJERCICIO 42. CREAR UN DICCIONARIO VACÍO
# ------------------------------------------------------------

clientes = {}

print("Diccionario vacío:", clientes)

# Agregamos información progresivamente.

clientes["cliente1"] = "Empresa ABC"
clientes["cliente2"] = "Empresa XYZ"

print("Diccionario con clientes:", clientes)

# También podemos utilizar dict().

otro_diccionario = dict()

print("Otro diccionario vacío:", otro_diccionario)


# ============================================================
# RESUMEN FINAL
# ============================================================

# CONCEPTOS PRACTICADOS:
#
# 1. Crear diccionarios.
# 2. Consultar valores.
# 3. Utilizar get().
# 4. Consultar keys().
# 5. Consultar values().
# 6. Consultar items().
# 7. Contar con len().
# 8. Comprobar claves con in.
# 9. Modificar valores.
# 10. Agregar claves.
# 11. Modificar con update().
# 12. Agregar varios elementos.
# 13. Eliminar con pop().
# 14. Eliminar con popitem().
# 15. Eliminar con del.
# 16. Recorrer claves.
# 17. Recorrer valores.
# 18. Desempaquetar items().
# 19. Acceder a tuplas mediante índices.
# 20. Combinar diferentes tipos de datos.
# 21. Acceder a listas internas.
# 22. Modificar listas internas.
# 23. Crear diccionarios anidados.
# 24. Consultar valores internos.
# 25. Crear diccionarios de útiles.
# 26. Consultar propiedades anidadas.
# 27. Reemplazar valores con update().
# 28. Agregar claves internas.
# 29. Consultar categorías.
# 30. Crear diccionarios familiares.
# 31. Acceder a datos específicos.
# 32. Recorrer diccionarios con índices.
# 33. Desempaquetar diccionarios anidados.
# 34. Combinar for e if.
# 35. Copiar con copy().
# 36. Vaciar con clear().
# 37. Calcular valores de productos.
# 38. Recorrer inventarios.
# 39. Acumular valores con +=.
# 40. Utilizar claves hashables.
# 41. Comprender claves duplicadas.
# 42. Crear diccionarios vacíos.

print("\nFin de los ejercicios adicionales de diccionarios.")
