import datetime

year = int(input("Dime un año: "))
month = int(input("Dime un mes: "))
day = int(input("Dime un dia: "))


manana_medianoche = datetime.datetime(year=year, month=month, day=day)

resultado = manana_medianoche - datetime.datetime.now()

print("Faltan {} dias y {} horas para el cumpleaños de aitana".format(resultado.days, int(resultado.seconds/3600)))



