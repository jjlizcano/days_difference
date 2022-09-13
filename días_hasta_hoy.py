
print("Éste programa dice cuantos días han pasado desde una fecha hasta otra (sin incluir el último día)")

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

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29
    return days[month - 1]

def days_in_year(year, month, day):
	days = 0
	for m in range(1, month):
		days += days_in_month(year, m)
	return days + day

def days_between_years(iyear, fyear):
    days = 0
    while iyear != fyear:
        days += days_in_year(iyear, 12, 31)
        iyear += 1
    return days

days_difference = days_between_years(iyear, fyear) + (days_in_year(fyear, fmonth, fday) - days_in_year(fyear, imonth, iday))

# output

print(days_difference)