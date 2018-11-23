texto_usuario = input("Dime una frase con mayusculas: ")

mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

mayusculas_n = 0

for item in texto_usuario:
    if item in mayusculas:
        mayusculas_n +=1
print("La cantidad de mayusculas en la frase es de: {}".format(mayusculas_n))