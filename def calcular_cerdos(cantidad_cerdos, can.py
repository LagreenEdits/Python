def calcular_cerdos(cantidad_cerdos, cantidad_years):
    assert isinstance (cantidad_cerdos, (int)), (cantidad_years, (int))
    assert cantidad_cerdos % 2 == 0, "El numero de cerdos por grupo es invalido, recuerda que solo son pares."
    assert cantidad_years > 0, "El numero de años es invalido, recuerda que solo se aceptan valores mayores o iguales a 0."
    return (cantidad_cerdos * (cantidad_years*9))/2

try:
    grupo_cerdos= int(input("Digite el numero de cerdos por grupo: "))
    años= int(input("Digite el numero años: "))
    resultado = calcular_cerdos (grupo_cerdos, años)
    print(f"Con {grupo_cerdos} cerdos la pobalcion aumentara a {round(resultado)} pasados {años} año(s)")
except AssertionError as error:
    print("\033[41m"+"Error detectado:"+"\033[0m"+"\033[31m"+f" {error}""\033[0m")
except ValueError:
    print("Caracter invalido")