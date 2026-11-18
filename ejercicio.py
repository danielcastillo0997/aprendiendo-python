def es_vocal(letra):
    return letra.lower() in ['a', 'e', 'i', 'o', 'u']

def primera_letra(lista):
    for elemento in lista:
        if isinstance(elemento, str) and elemento.isalpha and es_vocal(elemento):
            return elemento
    return "no Aplica"


Lista = [23, "2" , "a", "b", "c", "e", 3.5, True]

resultado = primera_letra(Lista)
print(resultado)