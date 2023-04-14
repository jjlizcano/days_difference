# Díferencia de días entre dos fechas:

def is_year_leap(year): # determina si un año es bisiesto
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month): # regresa la cantidad de días de un mes
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29
    return days[month-1]

def days_in_year(year, month, day): # regresa la cantidad de días pasados en un año
	days = 0
	for m in range(1, month):
		days += days_in_month(year, m)
	return days + day

def days_between_years(iyear, fyear): # regresa la cantidad de días entre distintos años
    days = 0
    for y in range(iyear, fyear):
        days += days_in_year(y, 12, 31)
    return days

# input
print("-----Fecha inicial-----")
iday = int(input("Día: "))
imonth = int(input("Mes: "))
iyear = int(input("Año: "))

print("------Fecha final------")
fday = int(input("Día: "))
fmonth = int(input("Mes: "))
fyear = int(input("Año: "))

# processing
days_difference = days_between_years(iyear, fyear) + (days_in_year(fyear, fmonth, fday) - days_in_year(iyear, imonth, iday))

# output
print("Diferencia de días:", days_difference)
