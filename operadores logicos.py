# operadores de comparación

x = 5 
y = 3
z = 5

print( x==y ) # si x es igual que y (False)
print(x != y) # si es distinto (True)

print(x>y) # si es mayor 
print(x<y) # si es menor
print(x>=z) # si es menor o igual

# Operadores Lógicos
## and
#     true      false
print(x > y and y > z) # ambas se deben cumplir para el true (false)
## or
#     true      false
print(x > y or y > z) # alguna se tiene que cumplir (false)

# negación 
v = True

print(not(v))