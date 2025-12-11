"""Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo."""

def is_year_leap(year):
    if type(year)==int and year>=0:
        if year%100==0 and year%400!=0:
            return False
        elif year%4==0:
            return True
        else:
            return False
    else:
          return print("el año",year,"no es valido")

def days_in_month(year, month):
    if type(month)==int and month>=0 and month <=31:
        months={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if month in months.keys(): return months[month]
        if month == 2 and is_year_leap(year):
            if is_year_leap(year): return 29
        else: return 28
    else: return print("No existe el mes",month,"en el año",year)

def day_of_year(year, month, day):
    if type(year)==int and type(month)==int and type(day)==int and month<=12 and month>=1 and year>=0:
        if day <= (days_in_month(year,month)) and day>0:
            if month==1: return day
            else:   
                months={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                day_total=0
                for meses_completados in range(1,month): day_total+=days_in_month(year,meses_completados)
                day_total+=day
                return day_total
        else: return None
    else: return None

print(is_year_leap(2024)) #true 
print(days_in_month(2024, 12)) # 31""
print(day_of_year(2024, 12, 31)) # 366
