
# Ejemplos de uso de comillas simples, dobles y triples en Python

# print("Hola "mundo"") # esto da error por las comillas dobles dentro de otras comillas dobles

print('Hola "mundo"')  # esto funciona correctamente
print("Hola 'mundo'")  # esto también funciona correctamente
print('''Hola "mundo"''')  # esto también funciona correctamente
print("""Hola 'mundo'""")  # esto también funciona correctamente


# Texto de múltiples líneas con comillas triples

multiples_lineas = '''Este es un texto
que abarca varias líneas
y mantiene el formato
incluso con espacios en blanco.'''

print(multiples_lineas)


# método lenght = len(multiples_lineas)
# print("La longitud del texto es:", lenght)

palabra = "Murciélago"
print(len(palabra))  # Salida: 10


# Métodos de cadenas de texto

print(palabra.upper())       # Salida: MURCIÉLAGO
print(palabra.lower())       # Salida: murciélago
print(palabra.capitalize())  # Salida: Murciélago
print(palabra.replace("a", "o"))  # Salida: Murciélogo
print(palabra.split("i"))    # Salida: ['Murc', 'élago']
print(palabra[0])            # Salida: M


# Operadores de pertenencia en cadenas de texto

texto = "Este curso es de fundamentos de Python"

estaIncluido = "Python" in texto  # método in verifica si una subcadena está presente en una cadena (Es Case Sensitive)
print(estaIncluido)  # Salida: True

noEstaIncluida = "Java" not in texto  # método not in verifica si una subcadena no está presente en una cadena (Es Case Sensitive)
print(noEstaIncluida)  # Salida: True


# Métodos de eliminación de espacios en cadenas de texto

espacios = "   Hola Mundo   "
print(espacios.strip())   # Salida: "Hola Mundo" (elimina espacios en blanco al inicio y al final)
print(espacios.lstrip())  # Salida: "Hola Mundo   " (elimina espacios en blanco al inicio)
print(espacios.rstrip())  # Salida: "   Hola Mundo" (elimina espacios en blanco al final)


# Indexación y segmentación (slicing) de cadenas de texto

texto2 = "Este es un ejemplo de texto"

print(texto2[5])      # Salida: e (acceso al carácter en la posición 5)
print(texto2[0:4])    # Salida: Este (subcadena desde la posición 0 hasta la 4, sin incluir la 4)
print(texto2[-5:])    # Salida: texto (últimos 5 caracteres)
print(texto2[:7])     # Salida: Este es (subcadena desde el inicio hasta la posición 7, sin incluir la 7)
print(texto2[::2])    # Cada segundo carácter
print(texto2[::-1])   # Cadena invertida


# Ejemplo de cadenas de texto inmutables

# Método replace
# no modifica la cadena original, sino que devuelve una nueva cadena con las modificaciones realizadas

curso = "Este es un curso de Javascript"
print(curso.replace("Javascript", "Python"))  # Salida: Este es un curso de Python
print(curso)  # Salida: Este es un curso de Javascript (la cadena original no se modifica)


# Método split para dividir cadenas de texto en elementos de una lista

textoDividido = texto2.split(" ")  # Divide la cadena en una lista de palabras usando el espacio como separador
print(textoDividido)  # Salida: ['Este', 'es', 'un', 'ejemplo', 'de', 'texto']


# Normalización de cadenas de texto

texto3 = "Este Texto Tiene Mayúsculas y minúsculas"

print("mayúsculas".lower() in texto3.lower())  # Salida: True (normaliza ambas cadenas a minúsculas antes de la comparación)
