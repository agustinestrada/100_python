def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print(True)
            else:
                return print(False)
        else:
            return print(True)
    else:
        return print(False)
    
is_leap_year(int(input('Por favor introducir un año para saber si es biciesto\n')))