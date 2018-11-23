from time import sleep
import random

lista = ["Hola que tal", "Aqui estamos wey", "Como te gusta", "Estamos ready", "Traeme un cafe"]



def item():
    lista = ["Hola que tal", "Aqui estamos wey", "Como te gusta", "Estamos ready", "Traeme un cafe"]
    frase_aleatoria = random.choice(lista)
    for frase_aleatoria in lista:
        while True:
            sleep(3)
            print("La frase es: {}".format(random.choice(lista)))

print(item())

