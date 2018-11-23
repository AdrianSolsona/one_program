import datetime

year = int(input("Dime un año: "))
month = int(input("Dime un mes: "))
day = int(input("Dime un dia: "))

manana = datetime.datetime(year=year, month=month, day=day)

hora_pasadas = datetime.datetime(year=year, month=month, day=day) - datetime.datetime.now()

print("Han pasado {} segundos desde ese dia".format(hora_pasadas.seconds))





