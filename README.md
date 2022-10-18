# Díferencia de días entre dos fechas.

## Funciones definidas:

* `is_year_leap(year)`: Determina si un año es bisiesto.

* `days_in_month(year, month)`: Regresa la cantidad de días de un mes, hace uso de la función `is_year_leap(year)`.

* `days_in_year(year, month, day)`: regresa la cantidad de días desde el inicio de un año hasta un mes y un día, hace uso de la función `days_in_month(year, month)`.

* `days_between_years(iyear, fyear)`: regresa la cantidad de días entre distintos años, hace uso de la función `days_in_year(year, month, day)`.

Después de que se hayan recibido la fecha inicial y final, se le asigna a la variable `days_difference` la diferencia de los días entre las dos fechas, para esto, se suma la cantidad de días entre los dos años, con la cantidad de días de la fecha y se les resta la cantidad de días del año inicial.

Puesto de otra manera:

`days_difference = days_between_years(iyear, fyear) + (days_in_year(fyear, fmonth, fday) - days_in_year(iyear, imonth, iday))`

siendo `fyear`, `fmonth` y `fday` el año, mes y día finales, y `iyear`, `imonth` y `iday` el año, mes y día iniciales.