from colorama import Fore, Style 
import time

#print("    ######################################################################## HAY ERROR EN LA FILA ",fil)
#Fore.GREEN + "" + Style.RESET_ALL
def Elim_Nume_List():#ELIMINA NUMEROS MAYORES DEL TOTAL DE FIL Y COL => CORRECTO // NO RETORNA
    for fil in range(n):
        for col in range(n):
            if lista_final[fil][col] > lista_final[fil][n]:
                print(Fore.RED + "Eliminamos", lista_final[fil][col], ">", lista_final[fil][n], end="; " + Style.RESET_ALL)
                lista_final[fil][col] = -1 #Horizontal
    else:print("FILA")
    for col in range(n):
        for fil in range(n):
            if lista_final[fil][col] > lista_final[n][col]:
                print(Fore.RED + "Eliminamos", lista_final[fil][col], ">", lista_final[n][col], end="; " + Style.RESET_ALL)
                lista_final[fil][col] = -1 #Vertical
    else:print("COLUMNA")
    return None

def Most_List(lista):#MUESTRA LISTA Y CAMBIA COLORES => CORRECTO // NO RETORNA
    print("\n")
    for i in lista:
        print("+-----" * len(i) + "+")
        for j in i:# Si el valor es 0, lo imprime en azul
            if int(j) <= -1: 
                print("| " + Fore.RED + f"{j:03}" + Style.RESET_ALL + " ", end="")#MAL
            elif int(j) == 0:
                print("| " + Fore.GREEN + f"{j:03}" + Style.RESET_ALL + " ", end="")#BIEN
            else:
                print("| " + Fore.BLUE + f"{j:03}" + Style.RESET_ALL + " ", end="")#NEUTRO
        print("|")
    print("+-----" * len(lista[0]) + "+\n")
    return None

def Agre_Nume_List():#AGREGA NUEMOS A LISTA CREADA => CORRECTO // NO RETORNA
    for fil in range(n):       #fila
        for col in range(n):   #columna
            a = int(input("ingresa un valor en la fila " + str(fil+1) + " y columna " + str(col+1) + " >> "))
            lista_final[fil][col]= a
            Most_List(lista_final)
        else:
            a = int(input("ingresa un valor en la fila " + str(fil+1) + " y columna " + str(col+2) + " >> "))
            lista_final[fil][col+1]= a
            Most_List(lista_final)
    for col in range(n):
        a = int(input("ingresa un valor en la fila " + str(fil+2) + " y columna " + str(col+1) + " >> "))
        lista_final[fil+1][col]= a
        Most_List(lista_final)
    else:
        lista_final[fil+1][col+1]= f"{-1:03}"
        Most_List(lista_final)
    return None

def Encuentra_Bien_lista(lista):#ENCUENTRA SI UNA FILA O COLUMNA ESTA INCOMPLETA O COMPLETA => CORRECTO // NO RETORNA
    contador_fallas = 0
    for fil in range(n):#LEYENDO EN IZQUIERDA A DERECHA
        suma_total_interna = 0
        for col in range(n):
            if lista[fil][col]>=0:
                suma_total_interna += lista[fil][col]
        else:
            if suma_total_interna == lista[fil][n]:#LLAMA PARA ELIMINAR FILAS
                print(Fore.GREEN + "ESTA COMPLETA FILA ",fil,"" + Style.RESET_ALL)
                Restar_Fila_A_Columna(fil)
            elif suma_total_interna > lista[fil][n]:
                print(Fore.BLUE + "    ESTA INCOMPLETA FILA ",fil,"" + Style.RESET_ALL)
                contador_fallas += 1
            else:
                print("    ######################################################################## HAY ERROR EN LA FILA ",fil)
    print("\n")
    
    for col in range(n):#LEYENDO DE ARRIBA HACIA ABAJO
        suma_total_interna = 0
        for fil in range(n):
            if lista[fil][col]>=0:
                suma_total_interna += lista[fil][col]
        else:
            if suma_total_interna == lista[n][col]:#LLAMA PARA ELIMINAR COLUMNAS
                print(Fore.GREEN + "ESTA COMPLETA COLUMNA ",col,"" + Style.RESET_ALL)
                Restar_Columna_A_Fila(col)
            elif suma_total_interna > lista[n][col]:
                print(Fore.BLUE + "    ESTA INCOMPLETA COLUMNA ",col,"" + Style.RESET_ALL)
                contador_fallas += 1
            else:
                print("    ######################################################################## HAY ERROR EN LA COLUMNA ",col)
                
    if contador_fallas == 0:
        return True
    return False
    
def Restar_Fila_A_Columna(fila_completa):#INGRESAS LA FILA == TOTAL DE LA FILA Y DISMINUYE EL TOTAL H, V Y SU PROPIO VALOR => CORRECTO // NO RETORNA
    for col in range(n):
        if lista_final[fila_completa][col] > 0 and lista_final[fila_completa][col] > 0:
            
            lista_final[fila_completa][n] -= lista_final[fila_completa][col] #RESTA FINAL H
            lista_final[n][col] -= lista_final[fila_completa][col] #RESTA FINAL V
            lista_final[fila_completa][col] -= lista_final[fila_completa][col] #RESTA VALOR
    Elim_Nume_List()
    return None

def Restar_Columna_A_Fila(columna_completa):#INGRESAS LA COLUMNA == TOTAL DE LA FILA Y DISMINUYE EL TOTAL H, V Y SU PROPIO VALOR => CORRECTO // NO RETORNA
    for fil in range(n):
        if lista_final[fil][columna_completa] > 0 and lista_final[fil][columna_completa] > 0:
            
            lista_final[fil][n] -= lista_final[fil][columna_completa] #RESTA FINAL H
            lista_final[n][columna_completa] -= lista_final[fil][columna_completa] #RESTA FINAL V
            lista_final[fil][columna_completa] -= lista_final[fil][columna_completa] #RESTA VALOR
    Elim_Nume_List()
    return None

def Restar_Fila_Columna_Valor_Correcto(fil,col):#USALO CUANDO TENGA UN NUMERO QUE ESTES 100% SEGURO, INGRESA FILA Y COLUMNA DE LA UBICAION => CORRECTO // NO RETORNA
    lista_final[fil][n] -= lista_final[fil][col] #RESTA FINAL H
    lista_final[n][col] -= lista_final[fil][col] #RESTA FINAL V
    lista_final[fil][col] -= lista_final[fil][col] #RESTA VALOR
    Elim_Nume_List()
    return None

def Encuentra_Combinatoria_Fila_Columna(fila_mayor_a_menor,num_total_fila):#ENCUENTRA UNA COMBINATORIA EN UNA FILA CON SU TOTAL => CORRECTO // RETONA TRUE OR FALSE

    numeros_combinatoria_total = []

    #print(fila_mayor_a_menor,num_total_fila)
    
    for primero in range(0,n):
        salir = False
        fila_mayor_a_menor_borrador = fila_mayor_a_menor[:]
        for i in range(0,n):
            numeros_combinatoria_temporal = []
            total_fila_borrador = num_total_fila
            indice_lista = []
            
            #print("\n\nINTENTO NUMERO",i)
            
            indice1 = primero
            while indice1 < n:
                indice2 = indice1
                #print("\n-------------------------------------------------",indice2,fila_mayor_a_menor_borrador,numeros_combinatoria_temporal)
                while indice1 < n:
                    valor = fila_mayor_a_menor_borrador[indice2]
                    #print("INCDICE: ",indice2," VALOR:",valor," TOTAL RESTA: ",total_fila_borrador," COMBINATORIA TOTAL: ",numeros_combinatoria_total,)
                    
                    if valor == num_total_fila:
                        #print("ENTROO")
                        #print(total_fila_borrador,"-",valor,"=")
                        ultimo_valor = valor
                        total_fila_borrador -= ultimo_valor
                        #print("GUARDAR VALOR:", ultimo_valor)
                        indice_lista.append(indice2)
                        numeros_combinatoria_temporal.append(valor)
                        #print("QUEDO FALTANDO",total_fila_borrador)
                        #fila_mayor_a_menor_borrador[indice2]=0
                        
                        if total_fila_borrador == 0:
                            numeros_combinatoria_total += numeros_combinatoria_temporal
                            #print("/////////////////////////GUARDAR A LA COMBINATORIA", numeros_combinatoria_temporal,numeros_combinatoria_total)
                            indice1+=1
                            salir = True
                            break
                    
                    else:
                        if valor > 0 and valor <= total_fila_borrador and (total_fila_borrador-valor) >= 0:
                            #print(total_fila_borrador,"-",valor,"=")
                            ultimo_valor = valor
                            total_fila_borrador -= ultimo_valor
                            #print("GUARDAR VALOR:",ultimo_valor)
                            indice_lista.append(indice2)
                            numeros_combinatoria_temporal.append(ultimo_valor)
                            #print("QUEDO FALTANDO",total_fila_borrador)
                            
                            if total_fila_borrador == 0:
                                numeros_combinatoria_total += numeros_combinatoria_temporal
                                #print("/////////////////////////GUARDAR A LA COMBINATORIA", numeros_combinatoria_temporal,numeros_combinatoria_total)
                            indice1+=1
                            break
                    indice1+=1
                    indice2 = indice1
                if salir:
                    break
                else:
                    None   
            if salir:
                break      
            else:
                #print("\n-------------------------------------------------",indice1,fila_mayor_a_menor_borrador)
                #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",total_fila_borrador,indice_lista)
                #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nRESPUESTA FINAL:",numeros_combinatoria_temporal,numeros_combinatoria_total,ultimo_valor,fila_mayor_a_menor_borrador.index(ultimo_valor),indice_lista)
                
                if total_fila_borrador >= 0 and len(indice_lista) >= 2:
                    #fila_mayor_a_menor_borrador[fila_mayor_a_menor_borrador.index(ultimo_valor)] = 0
                    #print("\n       ELIMINASTE EL",fila_mayor_a_menor_borrador[indice_lista[1]],indice_lista[1])
                    fila_mayor_a_menor_borrador[indice_lista[1]] = 0
        
    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n    RESPUESTA FINAL:",numeros_combinatoria_temporal,numeros_combinatoria_total,ultimo_valor,fila_mayor_a_menor_borrador.index(ultimo_valor),indice_lista)
    return numeros_combinatoria_total

def Conteo_Repetidos(lista_combinatoria):#SACA LOS NUMEROES DE LA LISTA NUMEROS => CORRECTO // RETORNA UN DICCIONARIO, CLAVE ES EL NUMERO Y EL VALOR LAS REPETICIONES
    conteo = {}
    for num in lista_combinatoria:
        conteo[num] = conteo.get(num, 0) + 1
    repetidos = {num: count for num, count in conteo.items() if count > 1}
    return repetidos

def Fila_Organizar_Saca_Mayor_Sin_Repetir(fila_sin_repetidos): #Primero se ejecuta => Encuentra_repetidos_fila y esta en una fila sin repeticiones => CORRECTO // NO RETORNA
    #lista = lista_final #Hace una copia de borrador
    fila_copiada = lista_final[fila_sin_repetidos][:-1]  # Hacer una copia de la fila sin repeticiones
    fila_ordenada = sorted(fila_copiada, reverse=True)  # Ordenar la fila sin repeticiones de mayor a menor
    total_interno = 0
    
    for i in range(1,n):#Suma todos los numeros excepto el primero en total resto
        if fila_ordenada[i] > 0:
            total_interno += fila_ordenada[i]
                
    if total_interno < lista_final[fila_sin_repetidos][n]:#El primer grande numero es necesario para llegar al total
        indice = fila_copiada.index(fila_ordenada[0])
        print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA: ",fila_sin_repetidos," COLUMNA: ",indice, " y es necesario: ",fila_ordenada[0],"\n" + Style.RESET_ALL)
        Restar_Fila_Columna_Valor_Correcto(fila_sin_repetidos,indice)
    
    elif total_interno >= lista_final[fila_sin_repetidos][n]:#No sabemos el numero correcto
        lista_numeros_combinatoria = [] 
        total_fila_borrador = lista_final[fila_sin_repetidos][n]#ultimo numero de lista_final
        
        lista_numeros_combinatoria += Encuentra_Combinatoria_Fila_Columna(fila_ordenada,total_fila_borrador)#Encontraste una combinatoria
        #print(numeros_combinatoria)#MUESTRA NUMEROS POSIBLES
            
        if len(lista_numeros_combinatoria) == 0: 
            print("    ######################################################################## HAY ERROR EN LA FILA:",fila_sin_repetidos) 
            
        suma=0
        for numero in lista_numeros_combinatoria:
            suma += numero
        else:
            combinaciones=suma//total_fila_borrador
            
        diccionario_repetidos = Conteo_Repetidos(lista_numeros_combinatoria)
        
        print("AAAAAAAAAAAAAAAAAAAAAAAAH",fila_ordenada[0], "==" ,lista_numeros_combinatoria[-1])
        if fila_ordenada[0] == lista_numeros_combinatoria[-1]:
            print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ", fila_sin_repetidos," COLUMNA ",indice," y es igual al total: ",fila_ordenada[0],"" + Style.RESET_ALL)
            Restar_Fila_Columna_Valor_Correcto(fila_sin_repetidos,indice)
            return None
        
        if diccionario_repetidos:
            for numero, repeticiones in diccionario_repetidos.items():
                print(f"Número {numero} se repite {repeticiones} veces con posibles combinaciones de {combinaciones}")
                
                if repeticiones == combinaciones:
                    indice = fila_copiada.index(numero)   
                    print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ",fila_sin_repetidos," COLUMNA ",indice, " y es de combinaciones: ",numero,"\n" + Style.RESET_ALL)
                    Restar_Fila_Columna_Valor_Correcto(fila_sin_repetidos,indice)
                    return None
                else:
                    print(Fore.BLUE + "    MUCHAS COMBINACIONES, IMPOSIBLE" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "    NINGUN NUMERO EN COMUN EN COMBINACIONES" + Style.RESET_ALL)
        
    return None

def Columna_Organizar_Saca_Mayor_Sin_Repetir(columna_sin_repetidos):#Primero se ejecuta => Encuentra_repetidos_columna y esta en una columna sin repeticiones => CORRECTO // NO RETORNA
    columna_copiada = [fila[columna_sin_repetidos] for fila in lista_final[:-1]]  # Hacer una copia de la fila sin repeticiones
    columna_ordenada = sorted(columna_copiada, reverse=True)  # Ordenar la fila sin repeticiones de mayor a menor
    total_interno = 0 
    
    for i in range(1,n):#Suma todos los numeros excepto el primero en total resto
        if columna_ordenada[i] > 0:
            total_interno += columna_ordenada[i]
           
    if total_interno < lista_final[n][columna_sin_repetidos]:#El primer grande numero es necesario para llegar al total
        indice = columna_copiada.index(columna_ordenada[0])
        print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ", indice," COLUMNA ",columna_sin_repetidos," y es necesario: ",columna_ordenada[0],"" + Style.RESET_ALL)
        Restar_Fila_Columna_Valor_Correcto(indice,columna_sin_repetidos)
    
    elif total_interno >=lista_final[n][columna_sin_repetidos]:#No sabemos el numero correcto
        lista_numeros_combinatoria = [] 
        total_columna_borrador = lista_final[n][columna_sin_repetidos]#ultimo numero de lista_final
        
        lista_numeros_combinatoria += Encuentra_Combinatoria_Fila_Columna(columna_ordenada,total_columna_borrador)#Encontraste una combinatoria
        #print(numeros_combinatoria)#MUESTRA NUMEROS POSIBLES
        
        if len(lista_numeros_combinatoria) == 0:
            print("    ######################################################################## HAY ERROR EN LA COLUMNA:",columna_sin_repetidos)
        suma=0
        for numero in lista_numeros_combinatoria:
            suma += numero
        else:
            combinaciones=suma//total_columna_borrador
            
        diccionario_repetidos = Conteo_Repetidos(lista_numeros_combinatoria)
        
        print("AAAAAAAAAAAAAAAAAAAAAAAAH",columna_ordenada[0], "==" ,lista_numeros_combinatoria[-1])
        if columna_ordenada[0] == lista_numeros_combinatoria[-1]:
            print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ", indice," COLUMNA ",columna_sin_repetidos," y es igual al total: ",columna_ordenada[0],"" + Style.RESET_ALL)
            Restar_Fila_Columna_Valor_Correcto(indice,columna_sin_repetidos)
            return None
                
        diccionario_repetidos = Conteo_Repetidos(lista_numeros_combinatoria)
        
        if diccionario_repetidos:
            for num, count in diccionario_repetidos.items():
                print(f"Número {num} se repite {count} veces con posibles combinaciones de {combinaciones}")
                if count == combinaciones:
                    indice = columna_copiada.index(num)   
                    print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ", indice," COLUMNA ",columna_sin_repetidos, " y es de combinaciones: ",num,"\n" + Style.RESET_ALL)
                    Restar_Fila_Columna_Valor_Correcto(indice,columna_sin_repetidos)
                    return None
                else:
                    print(Fore.BLUE + "    MUCHAS COMBINACIONES" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "    NINGUN NUMERO EN COMUN EN COMBINACIONES" + Style.RESET_ALL)
            
    return None

def Encuentra_repetidos_fila():#DETERMINA LA CANTIDAD DE REPETICIONES EN CADA FILA => CORRECTO // NO RETORNA
    for fil in range(n):
        if lista_final[fil][n] > 0:
            
            contador_lento_primer_indice, contador_Rapido_segundo_indice, repetidos = 0, 0, 0
            
            while contador_lento_primer_indice < n and repetidos >= 0:#HACE COMBINACIONES EN TODA LA FILA Y CUENTA REPETICIONES
                contador_Rapido_segundo_indice = contador_lento_primer_indice + 1
                #print(contador_lento_primer_indice,contador_Rapido_segundo_indice,repetidos)
                while contador_Rapido_segundo_indice < n and repetidos >= 0:
                    if lista_final[fil][contador_lento_primer_indice] > 0 and lista_final[fil][contador_Rapido_segundo_indice]> 0 and lista_final[fil][contador_lento_primer_indice] == lista_final[fil][contador_Rapido_segundo_indice]:
                        repetidos += 1
                    contador_Rapido_segundo_indice += 1
                    #print(contador_lento_primer_indice,contador_Rapido_segundo_indice,repetidos)
                contador_lento_primer_indice += 1
            print("\nFILA: ",fil," REPETIDOS: ",repetidos)
            
            if repetidos == 0:
                print(Fore.BLUE + "    SIN REPETIR\n" + Style.RESET_ALL)
                Fila_Organizar_Saca_Mayor_Sin_Repetir(fil)
            elif repetidos == 1:
                print(Fore.BLUE + "    UNA REPETICION\n" + Style.RESET_ALL)
                Elimina_Numeros_Fila_Repetida(fil)
            else: #MUCHOS REPEIDOS
                print(Fore.BLUE + "    MUCHOS REPETIDOS, IMPOSIBLE SABER\n" + Style.RESET_ALL)
            
        elif lista_final[fil][n] == 0:
            print(Fore.GREEN + "FILA: ",fil,"\n    ESTA COMPLETADA\n" + Style.RESET_ALL)
        else:
            print("    ######################################################################## HAY ERROR EN LA FILA ",fil)
    return None

def Encuentra_repetidos_columna():#DETERMINA LA CANTIDAD DE REPETICIONES EN CADA COLUMNA => CORRECTO // NO RETORNA
    for col in range(n):
        if lista_final[n][col] > 0:
            
            contador_lento_primer_indice, contador_Rapido_segundo_indice, repetidos = 0, 0, 0
            
            while contador_lento_primer_indice < n and repetidos >= 0:
                contador_Rapido_segundo_indice = contador_lento_primer_indice + 1
                while contador_Rapido_segundo_indice < n and repetidos >= 0:
                    if lista_final[contador_lento_primer_indice][col]>0 and lista_final[contador_Rapido_segundo_indice][col]>0 and lista_final[contador_lento_primer_indice][col] == lista_final[contador_Rapido_segundo_indice][col]:
                        repetidos += 1
                    contador_Rapido_segundo_indice += 1
                contador_lento_primer_indice += 1
            print("COLUMNA: ",col," REPETIDOS: ",repetidos)

            if repetidos == 0:
                print(Fore.BLUE + "    SIN REPETIR" + Style.RESET_ALL)
                Columna_Organizar_Saca_Mayor_Sin_Repetir(col)
            elif repetidos == 1:
                print(Fore.BLUE + "    UNA REPETICION" + Style.RESET_ALL)
                Elimina_Numeros_Columna_Repetida(col)
            else: #MUCHOS REPEIDOS
                print(Fore.BLUE + "    MUCHOS REPETIDOS, IMPOSIBLE SABER" + Style.RESET_ALL)
            
        elif lista_final[n][col] == 0:
            print(Fore.GREEN + "COLUMNA: ",col,"\n    ESTA COMPLETADA" + Style.RESET_ALL)
        else:
            print("    ######################################################################## HAY ERROR EN LA COLUMNA ",col)
    return None

def Elimina_Numero_Sin_Modificar(fil,col):#PERFECTO :) // NO RETORNA
    print(Fore.RED + "\nEliminamos", lista_final[fil][col]," No pertenece a la combinacion\n " + Style.RESET_ALL)
    lista_final[fil][col] = -1
    Elim_Nume_List()
    return None
    
def Elimina_Numeros_Fila_Repetida(fila_con_repetidos):#PERFECTO :) // NO RETORNA
    #lista = lista_final #Hace una copia de borrador
    fila_copiada = lista_final[fila_con_repetidos][:-1]  # Hacer una copia de la fila con repeticiones
    fila_ordenada = sorted(fila_copiada, reverse=True)  # Ordenar la fila con repeticiones de mayor a menor
    total_interno = 0
    
    for i in range(1,n):#Suma todos los numeros excepto el primero en total resto
        if fila_ordenada[i] > 0:
            total_interno += fila_ordenada[i]
                
    if total_interno < lista_final[fila_con_repetidos][n]:#El primer grande numero es necesario para llegar al total
        indice = fila_copiada.index(fila_ordenada[0])
        print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA: ",fila_con_repetidos," COLUMNA: ",indice, " y es necesario: ",fila_ordenada[0],"\n" + Style.RESET_ALL)
        Restar_Fila_Columna_Valor_Correcto(fila_con_repetidos,indice)
    
    elif total_interno >= lista_final[fila_con_repetidos][n]:#No sabemos el numero correcto
        numeros_combinatoria = [] 
        total_fila_borrador = lista_final[fila_con_repetidos][n]#ultimo numero de lista_final
        
        numeros_combinatoria += Encuentra_Combinatoria_Fila_Columna(fila_ordenada,total_fila_borrador)#Encontraste una combinatoria
        #print(numeros_combinatoria)#MUESTRA NUMEROS POSIBLES
            
        if len(numeros_combinatoria) == 0: 
            print("    ######################################################################## HAY ERROR EN LA FILA:",fila_con_repetidos) 
        suma=0
        for numero in numeros_combinatoria:
            suma += numero
        else:
            combinaciones=suma//total_fila_borrador
    
        print(fila_ordenada,combinaciones,"COMBINACIONES",numeros_combinatoria,total_fila_borrador)
        
        if len(numeros_combinatoria) >=1:
                for i in range(0,n):#Suma todos los numeros excepto el primero en total resto
                        if fila_ordenada[i] > 0 and fila_ordenada[i] not in numeros_combinatoria:
                            #print("##################",fila_ordenada[i],fila_con_repetidos,fila_copiada.index(fila_ordenada[i]))
                            Elimina_Numero_Sin_Modificar(fila_con_repetidos,fila_copiada.index(fila_ordenada[i]))
                            
    return None

def Elimina_Numeros_Columna_Repetida(columna_con_repetidos):#
    
    columna_copiada = [fila[columna_con_repetidos] for fila in lista_final[:-1]]  # Hacer una copia de la fila sin repeticiones
    columna_ordenada = sorted(columna_copiada, reverse=True)  # Ordenar la fila sin repeticiones de mayor a menor
    total_interno = 0 
    
    print(columna_copiada,columna_ordenada,total_interno)
    
    for i in range(1,n):#Suma todos los numeros excepto el primero en total resto
        if columna_ordenada[i] > 0:
            total_interno += columna_ordenada[i]
    
    if total_interno < lista_final[n][columna_con_repetidos]:#El primer grande numero es necesario para llegar al total
        indice = columna_copiada.index(columna_ordenada[0])
        print(Fore.GREEN + "\n>>>ENCONTRAMOS UNO CORRECTO EN LA FILA ", indice," COLUMNA ",columna_con_repetidos," y es necesario: ",columna_ordenada[0],"" + Style.RESET_ALL)
        Restar_Fila_Columna_Valor_Correcto(indice,columna_con_repetidos)
    
    elif total_interno >=lista_final[n][columna_con_repetidos]:#No sabemos el numero correcto
        numeros_combinatoria = [] 
        total_columna_borrador = lista_final[n][columna_con_repetidos]#ultimo numero de lista_final
        
        numeros_combinatoria += Encuentra_Combinatoria_Fila_Columna(columna_ordenada,total_columna_borrador)#Encontraste una combinatoria
        #print(numeros_combinatoria)#MUESTRA NUMEROS POSIBLES
        
        if len(numeros_combinatoria) == 0:
            print("    ######################################################################## HAY ERROR EN LA COLUMNA:",columna_con_repetidos)
        suma=0
        for numero in numeros_combinatoria:
            suma += numero
        else:
            combinaciones=suma//total_columna_borrador
    
        print(columna_ordenada,combinaciones,"COMBINACIONES",numeros_combinatoria,total_columna_borrador)


print("\n-----------------------INICIO-------------------------\n")

#n=int(input("ingresa el numero de filas y columnas de adentro"+"\n"))
n=6

lista_final = [[(str(filas)+str(columnas)) for columnas in range(1,n+2)] for filas in range (1,n+2)]

print(lista_final)
Most_List(lista_final)
#Agre_Nume_List(n)
print(lista_final)

lista_final = [                  #6 36/36 con 4 intentos - MUY DIFICIL
    [8, 1, 5, 2, 5, 1, 18],      #
    [1, 9, 9, 8, 9, 9, 26],      #
    [2, 4, 1, 1, 9, 9, 14],      # 
    [4, 5,1, 2, 1, 2, 9],        #
    [5, 2, 8, 1, 1, 8, 14],      # EJERCICIO 8 6 5 5 3
    [3, 1, 3, 8, 2, 5, 14],      # EJERCICIO 6 5 5 1
    [13, 19, 13, 19, 6, 25, 95
     ]
]

lista_final1 = [[9,4,8,2,1,1,12],#6 36/36 con 3 intentos - REPETIDOS
               [9,4,5,9,9,9,22],
               [1,9,8,7,7,9,32],
               [4,4,1,2,5,4,9],
               [7,8,6,3,7,2,21],
               [2,9,8,9,9,1,10],
               [5,29,23,25,14,10,99]]

lista_final1 = [[4,6,5,4,7,1,9],#6 36/36 con 2 intentos - VARIADOS
               [9,5,8,1,3,3,1],
               [1,5,3,3,3,3,15],
               [8,1,5,4,9,6,10],
               [1,5,8,6,2,3,9],
               [6,7,6,9,8,2,14],
               [7,6,16,18,3,8,99]]

lista_final1 = [                #6 36/36 con 2 intentos - VARIADOS
    [7, 3, 3, 9, 2, 8, 3],     #
    [4, 1, 3, 4, 6, 9, 18],    #
    [1, 3, 3, 6, 3, 2, 8],     # 
    [4, 9, 1, 8, 1, 6, 7],     #
    [5, 8, 3, 5, 8, 6, 16],    # EJERCICIO 8 6 5 5 3
    [6, 5, 5, 1, 5, 7, 6],     # EJERCICIO 6 5 5 1
    [9, 1, 15, 10, 9, 14, 99]
]

lista_final1 = [             #6 36/36 con 2 intentos - VARIADOS
    [4, 9, 1, 8, 1, 6, 7],   # Fila 0 igual
    [5, 8, 3, 5, 8, 6, 16],  # Antes era la fila 2, ahora es la fila 1
    [6, 5, 5, 1, 5, 7, 6],   # Antes era la fila 1, ahora es la fila 2
    [4, 1, 3, 4, 6, 9, 18], 
    [7, 3, 3, 9, 2, 8, 3], 
    [1, 3, 3, 6, 3, 2, 8], 
    [9, 1, 15, 10, 9, 14, 99]
]

lista_final1 = [[4,6,9,2,9,6,18],#6 36/36 con 1 intentos - REPETIDOS
               [6,1,5,6,6,6,12],
               [7,5,9,9,1,1,6],
               [1,5,2,9,7,6,3],
               [7,6,2,7,2,7,24],
               [7,9,6,6,6,4,22],
               [1,12,24,19,18,11,99]]

lista_final1 = [[1,4,7,2,8,8],#5 25/25 con 1 intentos
               [3,9,2,2,6,11],
               [6,2,3,8,4,8],
               [6,1,4,2,2,2],
               [2,2,1,4,9,5],
               [12,4,8,4,6,99]]

lista_final1 = [[5,5,3,6,3,8],#5 25/25 con 1 intentos
               [1,9,9,1,1,1],
               [2,7,4,5,9,9],
               [5,9,5,3,3,13],
               [3,6,1,3,9,1],
               [12,7,9,1,3,99]]

lista_final1 = [[9,3,1,9,1,5],#5 25/25 con 1 intentos
               [3,3,4,4,3,7],
               [5,4,1,8,1,7],
               [5,1,1,5,6,12],
               [1,5,2,2,8,7],
               [10,12,5,9,2,99]]

lista_final1 = [[7,2,1,6,2,2],#5 25/25 con 1 intentos
               [2,4,1,9,7,7],
               [4,4,6,1,9,6],
               [4,6,6,4,2,6],
               [6,7,1,5,4,11],
               [8,6,8,4,6,99]]

lista_final1 = [[9,7,5,6,5],#4 16/16 con 1 intentos
               [1,5,1,7,2],
               [7,6,1,1,2],
               [1,1,1,8,2],
               [1,1,8,1,99]]

lista_final1 = [[6,7,4,5,10],#4 16/16 con 3 intentos
               [4,5,7,4,4],
               [9,7,7,6,23],
               [4,7,5,7,12],
               [15,7,16,11,99]]

lista_final1 = [[7,1,1,2,9],#4 16/16 con 2 intentos
               [9,9,7,1,7],
               [8,9,9,7,16],
               [1,8,8,8,24],
               [7,17,15,17,99]]

tiempo_mostrar   =1  #MOSTRAR TABLAS ANTES DE CAMBIOS
tiempo           =0.1  #MOSTRAR TABLAS DESPUES DE CAMBIOS
tiempo_reiniciar =0  #REINICIAR CICLO
rango            =5  #CANTIDAD DE CICLOS

print("\n----------------------------TABLA-BASE------------------------------")
Most_List(lista_final)
time.sleep(tiempo_mostrar)  # Pausa de 1 segundo

dificultad = 1
while dificultad <= rango:
    
    print("\n----------------------ELIMAR-NUMEROS-MAYORES----------------------",dificultad)
    Most_List(lista_final)
    time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
    print("\n--------------------NUMEROS-MAYORES-ELIMINADOS--------------------",dificultad) #ELIMINA NUMEROS MUY GRANDES
    Elim_Nume_List()
    Most_List(lista_final)
    time.sleep(tiempo)  # Pausa de 1 segundo    

    print("\n------------------------BUSCANDO-COMPLETAS-----------------------",dificultad)
    Most_List(lista_final)
    time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
    print("\n------------------------COMPLETAS-LLENADAS-----------------------",dificultad) #ENCUENTRA FILAS Y COLUMNAS QUE ESTEN COMPLETAS
    if Encuentra_Bien_lista(lista_final):
        break#SALE DEL BLUCLE INFINITO
    Most_List(lista_final)
    time.sleep(tiempo)  # Pausa de 1 segundo
    
    print("\n------------------------FILAS-REPETIDAS------------------------",dificultad)
    Most_List(lista_final)
    time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
    print("\n---------------------FILAS-REPETIDAS-LLENADAS--------------------",dificultad) #ELIGE DECISIONES SEGUN LA CANTIDAD DE REPETICIONES EN UNA FILA
    Encuentra_repetidos_fila()
    Most_List(lista_final)
    time.sleep(tiempo)  # Pausa de 1 segundo
    
    print("\n-----------------------COLUMNAS-SIN-REPETIR----------------------",dificultad)
    Most_List(lista_final)
    time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
    print("\n-------------------COLUMNAS-SIN-REPETIR-LLENAS-------------------",dificultad) #ELIGE DECISIONES SEGUN LA CANTIDAD DE REPETICIONES EN UNA COLUMNA
    Encuentra_repetidos_columna()
    Most_List(lista_final)
    time.sleep(tiempo)  # Pausa de 1 segundo
    
    print("\n------------------------BUSCANDO-COMPLETAS-----------------------",dificultad)
    Most_List(lista_final)
    time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
    print("\n------------------------COMPLETAS-LLENADAS-----------------------",dificultad) #ENCUENTRA FILAS Y COLUMNAS QUE ESTEN COMPLETAS
    if Encuentra_Bien_lista(lista_final):
        break#SALE DEL BLUCLE INFINITO
    Most_List(lista_final)
    time.sleep(tiempo)  # Pausa de 1 segundo
    
    print("\n--------------------------REINICIAR------------------------------",dificultad) #REINICIA
    time.sleep(tiempo_reiniciar)  # Pausa de 1 segundo
    dificultad += 1

print("\n--------------------------TERMINO-:)------------------------------",dificultad)
Most_List(lista_final)
time.sleep(tiempo_mostrar)  # Pausa de 1 segundo
