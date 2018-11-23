a = 34
b = 89
c = 50
def nombre(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print (nombre(a,b,c))