numeros_funcion = [5, 6, 7, 8, 9, 10]

def nombre(numeros_funcion):
    for item in numeros_funcion:
        if item %2 == 0:
            print(item)

print(nombre(numeros_funcion))
