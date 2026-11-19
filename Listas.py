# ============================================================
# LISTAS EN PYTHON
# ============================================================
# APUNTES:
# - Las listas son ordenadas: conservan la posición de sus elementos.
# - Son modificables: podemos cambiar, agregar y eliminar elementos.
# - Permiten valores duplicados y distintos tipos de datos.
# - Los índices empiezan en 0, no en 1.

# 1. CREAR UNA LISTA Y CONSULTAR SUS ELEMENTOS
# Índices:       0          1            2
frutas = ["Manzana", "Naranja", "Mandarina"]

print("Lista de frutas:", frutas)
print("Tipo de la lista frutas:", type(frutas))
print("Fruta de la posición 1:", frutas[1])  # Naranja

# 2. MODIFICAR UN ELEMENTO
frutas[1] = "Banana"
print("Elemento nuevo en la posición 1:", frutas[1])
print("Lista de frutas actualizada:", frutas)

# 3. LISTAS CON DISTINTOS TIPOS DE DATOS
lista_mixta = ["Henry Fonck", 5, True]
print("Lista mixta:", lista_mixta)
print("Tipo:", type(lista_mixta))

# len() indica cuántos elementos tiene una lista.
print("Número de elementos de la lista mixta:", len(lista_mixta))
print("Número de elementos de la lista de frutas:", len(frutas))

# 4. EXTRAER UNA PARTE DE LA LISTA (SLICING)
# frutas[1:] muestra desde el índice 1 hasta el final.
print("Frutas desde la posición 1:", frutas[1:])

# 5. COMPROBAR SI UN ELEMENTO EXISTE
if "Manzana" in frutas:
    print("La manzana está dentro de la lista de frutas")

print("\n--- MÉTODOS DE LISTAS ---")

# 6. MÉTODOS PARA AGREGAR, ELIMINAR Y ORDENAR ELEMENTOS
vehiculos = ["Auto", "Moto", "Avion"]
print("Lista inicial:", vehiculos)

# append(): agrega un elemento al final.
vehiculos.append("Barco")
print("Después de append:", vehiculos)

# insert(índice, valor): agrega un elemento en una posición específica.
vehiculos.insert(1, "Bicicleta")
print("Después de insert:", vehiculos)

# remove(valor): elimina la primera aparición del valor indicado.
vehiculos.remove("Auto")
print("Después de remove:", vehiculos)

# pop(índice): elimina y devuelve el elemento de la posición indicada.
vehiculo_eliminado = vehiculos.pop(1)
print("Elemento eliminado con pop:", vehiculo_eliminado)
print("Después de pop:", vehiculos)

# sort(): ordena la lista (en este caso, alfabéticamente).
vehiculos.sort()
print("Después de sort:", vehiculos)

# reverse(): invierte el orden actual de la lista.
# No es lo mismo que ordenar alfabéticamente en orden descendente.
vehiculos.reverse()
print("Después de reverse:", vehiculos)

print("\n--- UNIR LISTAS ---")

# 7. UNIR LISTAS CON EL OPERADOR +
coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]
coleccion3 = coleccion1 + coleccion2
print("Nueva lista creada con +:", coleccion3)
# El operador + no modifica las listas originales.

# 8. EXTENDER UNA LISTA CON extend()
coleccion1.extend(coleccion2)
print("Colección 1 después de extend:", coleccion1)
# extend() modifica la lista original.

# ============================================================
# EJERCICIO PRÁCTICO: LISTA DE INVITADOS
# ============================================================
# Este ejemplo reúne lo aprendido: índices, slicing, len(),
# modificación, métodos, pertenencia, orden y unión de listas.

# 1. Crear una lista (ordenada, mutable, con duplicados)
invitados = ["Ana", "Betto", "Carla", "Betto"]
print("\n--- LISTA DE INVITADOS ---")
print("Lista inicial:", invitados)

# 2. Acceso por índices y slicing (rangos)
print("El primer invitado es:", invitados[0])
print("Los dos primeros son:", invitados[:2])  # No incluye el índice 2

# 3. Medir el largo con len()
print("Cantidad de invitados:", len(invitados))

# 4. Modificar un elemento (mutabilidad)
invitados[1] = "Bernardo"  # Cambiamos el primer 'Betto' por su nombre real
print("Lista tras corrección:", invitados)

# 5. Agregar elementos (append e insert)
invitados.append("Daniel")  # Al final
invitados.insert(2, "Elena")  # En la posición 2
print("Lista tras agregar:", invitados)

# 6. Eliminar elementos (remove y pop)
invitados.remove("Betto")  # Elimina la primera coincidencia restante
eliminado = invitados.pop(0)  # Elimina y guarda a 'Ana' (índice 0)
print("Invitado que no pudo venir:", eliminado)
print("Lista actual:", invitados)

# 7. Comprobar pertenencia (in)
if "Elena" in invitados:
    print("Elena ya está en la lista.")

# 8. Ordenar (sort y reverse)
invitados.sort()  # Orden alfabético
print("Lista ordenada:", invitados)

invitados.reverse()  # Invierte el orden actual
print("Lista invertida:", invitados)

# 9. Unir listas (+)
nuevos = ["Fran", "Gaby"]
lista_final = invitados + nuevos  # Crea una nueva lista
print("Lista final combinada:", lista_final)

# APUNTES DEL EJERCICIO:
# - Los índices empiezan desde 0.
# - invitados[:2] incluye los elementos de índices 0 y 1.
# - Las listas permiten nombres repetidos, como 'Betto'.
# - Al cambiar invitados[1], el otro 'Betto' permanece en la lista.
# - remove() elimina por valor; pop() elimina por índice y devuelve el valor.
# - sort() y reverse() modifican la lista original.
# - El operador + crea una lista nueva sin modificar invitados ni nuevos.

# ============================================================
# RECOMENDACIONES PARA ESTUDIAR
# ============================================================
# 1. Cambia los valores de las listas para observar el resultado.
# 2. Recuerda: posición 1 significa el SEGUNDO elemento.
# 3. Practica la diferencia entre append() e insert().
# 4. Practica la diferencia entre remove() y pop().
# 5. Compara el operador + con extend(): uno crea una lista
#    nueva y el otro modifica una lista existente.
# 6. Guarda los cambios antes de ejecutar el archivo en VS Code.
