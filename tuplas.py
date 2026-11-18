# Tupla: Colección ordenada e inmutable de elementos que permiten duplicados

# Indice             0             1          2       3
tecnologias = ("Python", "Javascript", "Go", "Python")

print(tecnologias)
print(tecnologias[1])
print(type(tecnologias))


fruta = ("Manzana") ## fruta = ("Manzana",)

print(type(fruta))


tupla = ("Python", 5, True)

print(tupla)
print(type(tupla))


x, y, z = tupla

print(x)
print(y)
print(z)


tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2

print(tupla3)

print(tupla * 2)


for item in tupla:
    print(item)


print("------------------")

tuplaAModificar = ("Python", "Javascript", "Go")  # Tupla
listaComodin = list(tuplaAModificar)  # casteo de tupla a lista

# print(listaComodin)

listaComodin.append("ReactS")  # Metodo agregar registro a lista
tuplaAModificar = tuple(listaComodin)  # casteo de lista a tupla

print(tuplaAModificar)  # vemos resultado