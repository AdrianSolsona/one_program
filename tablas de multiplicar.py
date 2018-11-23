numero_usuario = int(input("Dime un numero para realizar su tabla: "))

for multiplo in reversed(range(1, 16)):
        print(" {} * {} = {}".format(numero_usuario, multiplo, numero_usuario * multiplo))