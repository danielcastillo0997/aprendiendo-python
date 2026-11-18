# # Listas: son ordenadas, mutables y permiten duplicados

# #             0          1         2
# frutas = ['Manzana', 'Naranja', 'Mandarina', 'Naranja']
# print(frutas)
# print(type(frutas))

# print(frutas[1])

# frutas[1] = 'Banana'
# print(frutas[1])

# lista = ['Fabio',30,True]
# print(lista)
# print(type(lista))

# print(len(lista))

# print(len(frutas))

# print(frutas[0:2])

# print(frutas[1:])

# if 'Manzana' in frutas: #Si un if es verdadero se ejecuta el código
#     print('La manzana está dentro de las frutas')
# Indice       0       1     2
vehiculos = ['Auto','Moto','Avión']

# Metodos
# Append (agrega un elemento al final de la lista)
vehiculos.append('Batimovil')
print(vehiculos)

# Insert (agrega un elemento en una posición específica)  [No lo reemplaza, lo inserta]
vehiculos.insert(1,'Rocinante')
print(vehiculos)

# Remove (elimina un elemento)
vehiculos.remove('Auto')
print(vehiculos)

# Pop (elimina un elemento en una posición específica)
vehiculos.pop(1)
print(vehiculos)

# Sort (ordena la lista) en orden alfabético
vehiculos.sort()
print(vehiculos)

#Reverse (ordena la lista) en orden inverso
vehiculos.reverse()
print(vehiculos)

# Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2 #+ en este caso une las listas
print(coleccion3)

coleccion1.extend(coleccion2) #extend une las listas de manera permanente
print(coleccion1)

