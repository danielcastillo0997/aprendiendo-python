# Conjunto (Set): Colección no ordenada de elementos únicos (no se puede acceder por índice)

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("Manzana" in frutas)
print("Pera" not in frutas)

# Agregar
frutas.add("Pera")
print(frutas)

# Update
frutasTropicales = {"Piña", "Mango"}
frutas.update(frutasTropicales)
print(frutas)

# Eliminar
frutas.remove("Mango")
print(frutas)

frutas.discard("Pera")
print(frutas)

# Pop elimina un registro aleatorio
frutas.pop()
print(frutas)

# Clear
frutas.clear()
print(frutas)

print("-------------------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

c = a.union(b)
print(c)

familia = {
    "Padre" : {
    "nombre" : "paco" ,
    "edad" : "48"  
    },
    "Madre" : {
    "nombre" : "raquel" ,
    "edad" : "45"
    },
    "Hijo" : {
    "nombre" : "luis" ,
    "edad" : "20"
    }
    }
print(familia)