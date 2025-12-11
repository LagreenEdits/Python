lista_final = [[(str(filas)+str(columnas)) for columnas in range(3)] for filas in range (4)]
print("---------------INICIO-----------------\n",lista_final)

a=0
for i in range(len(lista_final)):
    for j in range(len(lista_final[i])):
        a+=1
        lista_final[i][j]=a

print("---------------RESULTADO-----------------\n", lista_final)
