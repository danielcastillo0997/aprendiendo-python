print("'hola mundo'")

ingles = "i'm sergie"

multiplesLineas = """Hola
Mundo"""

print(ingles)
print(multiplesLineas)

palabra =  "murcielago"
print(len(palabra))

Texto = "Este Curso es de Fundamentos de Python"
estaincluida = "Python" in Texto

noEstaIncluida = "Javascript" not in Texto


print(estaincluida)
print(noEstaIncluida)

Mayuscula = Texto.upper()  #siempre toma ultimo comando
Minuscula = Texto.lower()  #tener cuidado con denominaciones

print(Mayuscula)
print(Minuscula)


espacios = "     este es un texto     "
sinEspacios = espacios.strip