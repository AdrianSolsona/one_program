numero_adivinar = int(input("Numero a adivinar: "))
numero_segundo = int(input("Adivina el numero: "))

while numero_adivinar != numero_segundo:
    numero_adivinar += 1
    input("Sigue probando: ")
else:
    print("Has acertado el numero")
