texto_usuario = input("dime una frase: ")

espacios = " "
puntos = "."
comas = ","

espacios_n = 0
comas_n = 0
puntos_n = 0

for item in texto_usuario:
    if item in espacios:
        espacios_n += 1
    if item in comas:
        comas_n +=1
    if item in puntos:
        puntos_n += 1
print("la cantidad de espacios en la frase es de: {}".format(espacios_n))
print("la cantidad de comas en la frase es de: {}".format(comas_n))
print("la cantidad de puntos en la frase es de: {}".format(puntos_n))
