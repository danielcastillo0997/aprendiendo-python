from platform import python_branch


if 5>3:
    print("5 es mayor a 3")# realiza el print

if 2>3:
    print("5 es mayor a 3")# no realiza el print

x = 5
y = 3
z = 1

if x>y and x>z:
    print("x es mayor a y y x es mayor a y")
elif x==y:
    print("x es igual a y")
else:
    print("ninguna de las condiciones se cumple")

a ="python"
b ="javascript"
c ="python"

if a==c:
    if a != b:
        print("a es igual a c pero distinto de b") # se pueden anidar condiciones pero deben ser distintas
else:
    print("a no es igual a c")

e = 10
f = 10

if e == f:
    pass # para ignorar la estructura del if hasta tanto definamos que el comportamiento termina