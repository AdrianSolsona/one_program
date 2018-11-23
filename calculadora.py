resultado = 0
numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce otro numero: "))

print("¿que operacion desea realizar? :")
print("a.- Sumar")
print("b.- Restar")
print("c.- Multiplicar")
print("d.- Dividir")

opcion = input("Elija una opcion: ")
if opcion == ("a"):
    resultado = numero1 + numero2
    print("calculando...")
    print("El resultado es: {0}".format(resultado))
elif opcion == ("b"):
    resultado = numero1 - numero2
    print("calculando...")
    print("El resultado es: {0}".format(resultado))
elif opcion == ("c"):
    resultado = numero1 * numero2
    print("calculando...")
    print("El resultado es: {0}".format(resultado))
elif opcion == ("d"):
    resultado = numero1 / numero2
    print("calculando...")
    print("El resultado es: {0}".format(resultado))
