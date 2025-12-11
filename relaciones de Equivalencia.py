# Definimos un conjunto A no vacío, el cual se relaciona con R                                               Python
A = {1, 2, 3, 4, 5} 

# Definimos una posible relación de equivalencia R
R = {(1, 1), (2, 2), (3, 3), 
     (4, 4), (5, 5), (1, 2), 
     (2, 1), (2, 3), (3, 2), 
     (1, 3), (3, 1)}  

# Creamos una función para verificar la reflexividad
# Para todo aEA, aRa
def es_reflexiva(A, R):
    for a in A:
        if (a, a) not in R: # Si no se encuentra aRa en R, NO es reflexiva
            return False
    return True

# Creamos una función para verificar la simetría
# Si aRb, entonces bRa
def es_simetrica(R):
    for (a, b) in R:
        if (b, a) not in R: # Si no se encuentra bRa en R, NO es simétrica 
            return False
    return True

# Creamos una función para verificar la transitividad
# Si aRb y bRc, entonces aRc
def es_transitiva(R):
    for (a, b) in R:
        for (x, y) in R:
            if b == x and (a, y) not in R: # Si no se encuentra aRc en R, NO es transitiva
                return False
    return True

# Comprobamos cada una de las propiedades de relaciones de equivalencia
print("Reflexiva:", es_reflexiva(A, R))
print("Simétrica:", es_simetrica(R))
print("Transitiva:", es_transitiva(R))

# Evaluamos si en cada una de las propiedades se cumple correctamente
if es_reflexiva(A, R) and es_simetrica(R) and es_transitiva(R):
    print("La relación R es una relación de equivalencia.") # Si se cumple todas

else:
    print("La relación R NO es una relación de equivalencia.") # No se cumple
