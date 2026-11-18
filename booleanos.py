
# Boolean values

v = True
f = False

print(v)
print(f)
print(type(v))  # Salida: <class 'bool'>
print(type(f))  # Salida: <class 'bool'>


# Mayor o menor o igual que
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 3)  # True
print(5 <= 3)  # False


# Comparison operators
print(5 == 3)  # False
print(5 != 3)  # True


# Logical operators and, or, not
print((5 > 3) and (2 < 4))  # True
print((5 > 3) or (2 > 4))   # True

print(not(5 > 3))  # False
print(not(5 < 3))  # True


# Uso de operadores lógicos con variables booleanas

print(v and f)  # False
print(v or f)   # True

print(not v)  # False
print(not f)  # True


# Casteo a booleano
print(bool(1))          # True
print(bool(0))          # False
print(bool(-1))         # True
print(bool("Hola"))     # True
print(bool(""))         # False
print(bool([1, 2, 3]))  # True
print(bool([]))         # False
print(bool(None))       # False


# Verificar tipo de dato booleano con isinstance()
x = 123
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False
print(isinstance(v, bool))  # True
print(isinstance(f, bool))  # True
