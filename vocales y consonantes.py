texto_usuario = input("Escribe una frase con vocales: ")

a = "a"
e = "e"
i = "i"
u = "u"
o = "o"

vocales_usuario = []


for item in texto_usuario:
    if item in a:
        vocales_usuario.append(a)
    elif item in e:
        vocales_usuario.append(e)
    elif item in i:
        vocales_usuario.append(i)
    elif item in u:
        vocales_usuario.append(u)
    elif item in a:
        vocales_usuario.append(o)

print("vocales de la frase son: {}".format(vocales_usuario))

