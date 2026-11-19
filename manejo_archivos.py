
# ============================================================
# MANEJO DE ARCHIVOS EN PYTHON
# Archivo: manejo_archivos.py
# ============================================================

# OBJETIVO:
# Aprender a crear, escribir, leer, modificar y eliminar
# archivos utilizando Python.
#
# CONCEPTOS:
#
# open()  -> Abre un archivo.
# with    -> Administra su apertura y cierre.
# read()  -> Lee el contenido completo.
# readline() -> Lee una línea.
# readlines() -> Devuelve las líneas como una lista.
# write() -> Escribe información.
# close() -> Cierra el archivo.
#
# MODOS:
#
# "r"  -> Leer.
# "w"  -> Escribir, creando o sobrescribiendo.
# "a"  -> Agregar información al final.
# "x"  -> Crear un archivo nuevo.
# "r+" -> Leer y escribir.
# "w+" -> Escribir y leer, borrando contenido anterior.


# ============================================================
# NIVEL 1 - PREPARAR NUESTRA CARPETA DE PRÁCTICA
# ============================================================

from pathlib import Path

# __file__ representa la ubicación de este script.
# Path(__file__).resolve().parent obtiene su carpeta.

carpeta = Path(__file__).resolve().parent / "archivos_practica"

# Crear la carpeta si no existe.
carpeta.mkdir(exist_ok=True)

# Ruta del archivo de ejemplo.
archivo = carpeta / "archivo.txt"

print("Carpeta de práctica:", carpeta)

# APUNTE:
# pathlib permite construir rutas de archivos.
# Así evitamos depender de la carpeta actual
# desde donde ejecutamos el programa.


# ============================================================
# NIVEL 2 - CREAR Y ESCRIBIR UN ARCHIVO CON W
# ============================================================

with open(archivo, "w", encoding="utf-8") as f:

    f.write("Hola mundo desde Python\n")
    f.write("Estoy aprendiendo manejo de archivos\n")
    f.write("Este es mi primer archivo de texto\n")

print("\nArchivo creado correctamente.")

# EXPLICACIÓN:
#
# open() abre el archivo.
# "w" permite escribir.
# encoding="utf-8" permite trabajar con tildes y ñ.
# as f guarda la referencia al archivo.
# f.write() escribe texto.
#
# \n representa un salto de línea.
#
# IMPORTANTE:
# "w" sobrescribe el contenido anterior.


# ============================================================
# NIVEL 3 - LEER UN ARCHIVO CON R
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    contenido = f.read()

print("\nCONTENIDO DEL ARCHIVO:")
print(contenido)

# read() lee todo el contenido desde
# la posición actual del cursor.


# ============================================================
# NIVEL 4 - LEER UNA LÍNEA CON READLINE()
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    primera_linea = f.readline()

print("Primera línea:", primera_linea.strip())

# readline() lee una línea.
# strip() elimina espacios y saltos de línea
# al comienzo y al final del texto.


# ============================================================
# NIVEL 5 - LEER VARIAS LÍNEAS
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    primera = f.readline()
    segunda = f.readline()

print("\nPrimera línea:", primera.strip())
print("Segunda línea:", segunda.strip())

# Cada llamada a readline() avanza el cursor.


# ============================================================
# NIVEL 6 - READLINES()
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    lineas = f.readlines()

print("\nLista de líneas:", lineas)

# readlines() devuelve una lista de cadenas.
# Los saltos de línea pueden permanecer en cada elemento.

for linea in lineas:
    print("Texto:", linea.strip())


# ============================================================
# NIVEL 7 - RECORRER EL ARCHIVO CON FOR
# ============================================================

print("\nRECORRIENDO EL ARCHIVO:")

with open(archivo, "r", encoding="utf-8") as f:

    for numero, linea in enumerate(f, start=1):

        print(numero, ":", linea.strip())

# enumerate() permite obtener el número
# de línea y el contenido al mismo tiempo.


# ============================================================
# NIVEL 8 - AGREGAR INFORMACIÓN CON A
# ============================================================

with open(archivo, "a", encoding="utf-8") as f:

    f.write("Nueva línea agregada con append\n")

print("\nInformación agregada.")

# El modo "a" agrega información al final.
# No borra el contenido anterior.


# ============================================================
# NIVEL 9 - COMPROBAR EL CONTENIDO ACTUALIZADO
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    print("\nArchivo actualizado:")
    print(f.read())

# Ahora el archivo contiene cuatro líneas.


# ============================================================
# NIVEL 10 - CREAR UN ARCHIVO EXCLUSIVAMENTE CON X
# ============================================================

archivo_nuevo = carpeta / "nuevo_archivo.txt"

try:

    with open(archivo_nuevo, "x", encoding="utf-8") as f:
        f.write("Archivo creado con el modo x\n")

except FileExistsError:
    print("El archivo ya existe y no puede crearse nuevamente.")

else:
    print("Archivo creado correctamente con x.")

# APUNTE:
# "x" crea un archivo nuevo.
# Si ya existe, genera FileExistsError.
#
# A diferencia de "w", no sobrescribe.


# ============================================================
# NIVEL 11 - MANEJAR FILENOTFOUNDERROR
# ============================================================

archivo_inexistente = carpeta / "no_existe.txt"

try:

    with open(archivo_inexistente, "r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:
    print("\nError: El archivo no fue encontrado.")

# Este ejemplo combina manejo de archivos
# con try y except.


# ============================================================
# NIVEL 12 - REPRODUCIR TU EJEMPLO ORIGINAL
# ============================================================

# En tu imagen tenías un try que intentaba leer
# un archivo y, si no existía, lo creaba con "x".

archivo_ejemplo = carpeta / "ejemplo_original.txt"

try:

    with open(archivo_ejemplo, "r", encoding="utf-8") as f:

        print(f.read())
        print(f.readline())

except FileNotFoundError:

    with open(archivo_ejemplo, "x", encoding="utf-8") as f:
        pass

    print("Hola mundo desde archivo.")

# IMPORTANTE:
#
# read() consume el contenido desde la posición actual
# hasta el final del archivo.
#
# Por eso, si después llamamos a readline()
# sin mover el cursor, normalmente devuelve "".


# ============================================================
# NIVEL 13 - ENTENDER EL CURSOR DEL ARCHIVO
# ============================================================

with open(archivo, "r", encoding="utf-8") as f:

    print("\nPrimera lectura:")
    print(f.read())

    print("Segunda lectura:")
    print(repr(f.read()))

    # Volvemos al principio.
    f.seek(0)

    print("Después de seek(0):")
    print(f.readline().strip())

# APUNTES:
#
# El archivo tiene un cursor de lectura.
#
# read() avanza ese cursor.
# seek(0) regresa al comienzo.
# tell() permite consultar la posición actual.


# ============================================================
# NIVEL 14 - LEER Y ESCRIBIR CON R+
# ============================================================

archivo_rplus = carpeta / "ejemplo_rplus.txt"

# Creamos primero un archivo de prueba.
with open(archivo_rplus, "w", encoding="utf-8") as f:
    f.write("Python es interesante.\n")

# Lo abrimos con r+.
with open(archivo_rplus, "r+", encoding="utf-8") as f:

    contenido = f.read()

    print("\nContenido original:", contenido.strip())

    # Después de read(), el cursor está al final.
    f.write("Nueva línea desde r+.\n")

# Revisamos el archivo.
with open(archivo_rplus, "r", encoding="utf-8") as f:
    print(f.read())

# RECOMENDACIÓN:
# r+ no borra automáticamente el archivo.
#
# Sin embargo, escribir en posiciones existentes
# puede sobrescribir parte de su contenido.
# No debe confundirse con el modo "a".


# ============================================================
# NIVEL 15 - ESCRIBIR Y LEER CON W+
# ============================================================

archivo_wplus = carpeta / "ejemplo_wplus.txt"

with open(archivo_wplus, "w+", encoding="utf-8") as f:

    f.write("Primera línea con w+\n")
    f.write("Segunda línea con w+\n")

    # Volvemos al principio para leer.
    f.seek(0)

    print("\nContenido escrito con w+:")
    print(f.read())

# IMPORTANTE:
# w+ elimina el contenido anterior al abrir el archivo.
# Permite escribir y leer.


# ============================================================
# NIVEL 16 - UTILIZAR WRITE() CON VARIABLES
# ============================================================

nombre = "Daniel"
curso = "Python"
nivel = "Principiante"

archivo_estudiante = carpeta / "estudiante.txt"

with open(archivo_estudiante, "w", encoding="utf-8") as f:

    f.write(f"Nombre: {nombre}\n")
    f.write(f"Curso: {curso}\n")
    f.write(f"Nivel: {nivel}\n")

with open(archivo_estudiante, "r", encoding="utf-8") as f:
    print("\nDATOS DEL ESTUDIANTE:")
    print(f.read())

# Las f-strings permiten incorporar variables
# dentro de cadenas de texto.


# ============================================================
# NIVEL 17 - GUARDAR UNA LISTA EN UN ARCHIVO
# ============================================================

frutas = ["Manzana", "Naranja", "Pera", "Kiwi"]

archivo_frutas = carpeta / "frutas.txt"

with open(archivo_frutas, "w", encoding="utf-8") as f:

    for fruta in frutas:
        f.write(fruta + "\n")

print("\nFrutas guardadas.")

# Leemos la lista desde el archivo.

with open(archivo_frutas, "r", encoding="utf-8") as f:

    frutas_recuperadas = []

    for linea in f:
        frutas_recuperadas.append(linea.strip())

print("Frutas recuperadas:", frutas_recuperadas)

# Este ejemplo combina:
# Listas + for + manejo de archivos.


# ============================================================
# NIVEL 18 - GUARDAR DATOS DE UN INVENTARIO
# ============================================================

inventario = {
    "P001": {"nombre": "Tornillo", "cantidad": 20},
    "P002": {"nombre": "Tuerca", "cantidad": 50},
    "P003": {"nombre": "Arandela", "cantidad": 100}
}

archivo_inventario = carpeta / "inventario.txt"

with open(archivo_inventario, "w", encoding="utf-8") as f:

    for codigo, producto in inventario.items():

        linea = (
            f"{codigo},"
            f"{producto['nombre']},"
            f"{producto['cantidad']}\n"
        )

        f.write(linea)

print("\nInventario guardado.")

with open(archivo_inventario, "r", encoding="utf-8") as f:

    print("INVENTARIO:")
    print(f.read())

# RESULTADO:
#
# P001,Tornillo,20
# P002,Tuerca,50
# P003,Arandela,100
#
# Es un ejemplo sencillo de texto separado por comas.
# Para datos CSV más complejos, conviene usar el módulo csv.


# ============================================================
# NIVEL 19 - CONTAR LAS LÍNEAS DE UN ARCHIVO
# ============================================================

with open(archivo_inventario, "r", encoding="utf-8") as f:

    cantidad_lineas = sum(1 for linea in f)

print("Cantidad de registros:", cantidad_lineas)

# sum() suma los valores generados.
# Cada línea aporta 1 al contador.


# ============================================================
# NIVEL 20 - COMPROBAR SI EXISTE UN ARCHIVO
# ============================================================

print("\n¿Existe archivo.txt?:", archivo.exists())

print("¿Existe no_existe.txt?:",
      archivo_inexistente.exists())

# exists() permite comprobar si existe una ruta.


# ============================================================
# NIVEL 21 - ELIMINAR UN ARCHIVO DE PRUEBA
# ============================================================

archivo_temporal = carpeta / "temporal.txt"

# Creamos un archivo temporal.
with open(archivo_temporal, "w", encoding="utf-8") as f:
    f.write("Archivo de prueba para eliminar.")

# Comprobamos su existencia.
print("¿Existe temporal?:", archivo_temporal.exists())

# Eliminamos únicamente el archivo temporal
# que acabamos de crear.
archivo_temporal.unlink()

print("¿Existe después?:", archivo_temporal.exists())

# IMPORTANTE:
# unlink() elimina un archivo del disco.
# No lo utilices sobre archivos importantes
# sin comprobar antes la ruta.


# ============================================================
# APUNTES FINALES
# ============================================================

# MODOS DE ARCHIVOS:
#
# r  -> Leer. Requiere que el archivo exista.
# w  -> Escribir. Crea o sobrescribe.
# a  -> Agregar información al final.
# x  -> Crear un archivo nuevo exclusivamente.
# r+ -> Leer y escribir. No borra al abrir.
# w+ -> Leer y escribir. Borra al abrir.
#
# FUNCIONES Y MÉTODOS:
#
# open()      -> Abre un archivo.
# read()      -> Lee todo el contenido restante.
# readline()  -> Lee una línea.
# readlines() -> Devuelve las líneas en una lista.
# write()     -> Escribe texto.
# seek()      -> Cambia la posición del cursor.
# tell()      -> Consulta la posición del cursor.
# close()     -> Cierra el archivo.
#
# PATHLIB:
#
# Path()   -> Representa una ruta.
# mkdir()  -> Crea una carpeta.
# exists() -> Comprueba si existe una ruta.
# unlink() -> Elimina un archivo.


# RECOMENDACIONES:
#
# 1. Utiliza with open() para manejar archivos.
# 2. Especifica encoding="utf-8" para archivos de texto.
# 3. Evita usar "w" con archivos importantes sin respaldo.
# 4. Recuerda que \n representa un salto de línea.
# 5. Utiliza "a" para agregar información sin borrar.
# 6. Utiliza try/except para gestionar archivos inexistentes.
# 7. Recuerda que read() mueve el cursor.
# 8. Utiliza pathlib para trabajar con rutas.
# 9. Haz las primeras pruebas con archivos temporales.
# 10. Comprueba siempre qué archivos se están modificando.


print("\nFin de los ejercicios de manejo de archivos.")
