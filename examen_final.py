
#------------------------------------------------------QUESTION 1-------------------------------------------------------------(LISTAS)(FALSE=0, TRUE=1)

"""
list = [False, True, "2", 3, 4, 5]

A. b = 0 not in list
#¿EXISTE EL INDICE CERO? R/ FALSE

B. b = list[0]
#MUESTRA EL INDICE CERO R/ FALSE

C. b = 0 in list Most Voted >>Most Voted<<
#¿EXISTE EL INDICE CERO? R/ TRUE

D. b = False
#MUESTRA EL VALOR R/ FALSE

print(b)
"""

#------------------------------------------------------QUESTION 2-------------------------------------------------------------(TUPLAS)(REEMPLAZAR UN VALOR DE TUPLA)

"""
my_tupla = 1,2,3

my_tupla[1]=my_tupla[1]+my_tupla[0]

#A. is illegal >>Most Voted<<
#B. may be illegal if the tuple contains strings
#C. can be executed if and only if the tuple contains at least two elements
#D. is fully correct
"""

#------------------------------------------------------QUESTION 3-------------------------------------------------------------(LISTAS)(.INSET(POSICION, VALOR))

"""
x = [0, 1, 2]
x.insert(0, 1)
del x[1]
print(sum(x))

#A. 2
#B. 4 >>Most Voted<<
#C. 5
#D. 3
"""

#------------------------------------------------------QUESTION 4-------------------------------------------------------------(LISTAS)(2 NAMES != ACCEDER MISMA LISTA)

"""
lista1 = [1, 3]
lista2 = lista1
lista1[0] = 4
#SON DOS NOMBRES DISTINTOS PARA ACCEDER A LA MISMA LISTA 

print(lista1)
print(lista2)

#A. [1, 3]
#B. [1, 4]
#C. [4, 3] >>Most Voted<<
#D. [1, 3, 4]
"""

#------------------------------------------------------QUESTION 5-------------------------------------------------------------(LISTAS)(INDICES[:])

"""
data = ["Peter", 404, 3.03, "wallert", 33.3]
print(data[1:3])

#A. ['Peter', 404, 3.03, 'Wellert', 33.3]
#B. None of the above.
#C. [404, 3.03] >>Most Voted<<
#. ['Peter', 'Wellert']
"""

#------------------------------------------------------QUESTION 6-------------------------------------------------------------(LISTAS)(2 NAMES != ACCEDER MISMA LISTA)

"""
nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(nums, vals)

#A. nums is longer than vals
#B. nums and vals are of the same length >>Most Voted<<
#C. vals is longer than nums
#D. nums and vals refer to the same list >>Most Voted<<
"""

#------------------------------------------------------QUESTION 7-------------------------------------------------------------(DICCIONARIOS)(OBTENER CLAVE-VALOR)

"""
dyctionary = {}
dyctionary["1"] = (1, 2)
dyctionary["2"] = (2, 1)
# ENTRA CON LA PALABRA CLAVE 1 Y 2 Y DESPUES ELIGE EL INDICE DE LA TUPLA (1,2) Y (2,1) RESPECTIVAMENTE

for x in dyctionary.keys():
    print(dyctionary[x][1], end="")

#A. 12
#B. (2, 1)
#C. (1, 2)
#D. 21 >>Most Voted
"""

#------------------------------------------------------QUESTION 8-------------------------------------------------------------(LISTAS)(ITERAR LETRAS DE UNA PALABRA)

"""
valor_sospechoso = list("hello")
print(valor_sospechoso)

#A. hello
#B. [h, e, l, l, o]
#C. ['h', 'e', 'l', 'l', 'o'] >>Most Voted<<
#D. ['h' 'e' 'l' 'l' 'o']
#E. None of the above.
"""

#------------------------------------------------------QUESTION 9-------------------------------------------------------------(LISTAS)(AUMENTA EN DOS [::2])

"""
a = [1,2,3,4,5,6,7,8,9]
print(a[::2])

#A. [1, 3, 5, 7, 9] >>Most Voted<<
#B. [8, 9]
#C. [1, 2, 3]
#D. [1, 2]
"""

#------------------------------------------------------QUESTION 10-------------------------------------------------------------(DICCIONARIOS)(OBTENER-CLAVE VALOR)

"""
dic = {}
dic[1] = 1
dic["1"] = 2
dic[1] += 1

#print(dic)
sum = 0
for k in dic:
    #print(type(k),k)
    sum += dic[k]
    #print(dic)

#A. 3
#B. 2
#C. 4 >>Most Voted<<
#D. 1
"""

#------------------------------------------------------QUESTION 11-------------------------------------------------------------(DICCIONARIOS)

"""
dictionary = {"one":"two","three":"one","two":"three"}
v = dictionary["one"]
#print(v)

for k in range(len(dictionary)):
#    print(k,dictionary[v])
    v = dictionary[v]

print(v)

#A. two >>Most Voted<<
#B. one
#C. (‘one’, ‘two’, ‘three’)
#D. three
"""

#------------------------------------------------------QUESTION 12-------------------------------------------------------------(LISTAS)

"""
nums = [3,4,5,6,7,8,9,1,2]
nums.pop(1)
print(nums)

A. [3, 1, 25, 5, 20, 5, 4]
B. [1, 3, 4, 5, 20, 5, 25]
C. [3, 5, 20, 5, 25, 1, 3] >>Most Voted<<
D. [1, 3, 3, 4, 5, 5, 20, 25]
E. [3, 4, 5, 20, 5, 25, 1, 3]
"""

#------------------------------------------------------QUESTION 13-------------------------------------------------------------(VARIABLES)

"""
str1 = "papaya"
str2 = str1[:]
print(str1,str2)

#A. str1 and str2 are different (but equal) strings. >>Most Voted<<
#B. str1 and str2 are different names of the same strings.
#C. str1 is longer than str2
#D. str2 is longer than str1
"""

#------------------------------------------------------QUESTION 14-------------------------------------------------------------(LECTURAS)

"""
The fact that tuples belong to sequence types means:

A. they can be modified using the del instruction
B. they can be extended using the .append() method
C. they are actually lists
D. they can be indexed and sliced like lists >>Most Voted<<
"""

#------------------------------------------------------QUESTION 15-------------------------------------------------------------(LISTAS)

"""
lista_1 = [3,1,-1]
lista_1[-1] = lista_1[-2]
print(lista_1)

#A. [1, 1, 1]
#B. [3, -1, 1]
#C. [3, 1, 1] >>Most Voted<<
"""

#------------------------------------------------------QUESTION 16-------------------------------------------------------------(TUPLAS)

"""
data = ((1,2),) * 7
print(len(data[3:8]))
print(type(data),data)

A. The code is erroneous.
B. 6
C. 5
D. 4 >>Most Voted<<
"""

#------------------------------------------------------QUESTION 17-------------------------------------------------------------(DICCIONARIOS)

"""
data = {"Peter":30,"Paul":31}
print(list(data.keys()))
#A. ('Peter': 30, 'Paul': 31)
#B. ('Peter', 'Paul')
#C. ['Peter': 30, 'Paul': 31]
#D. ['Peter', 'Paul'] >>Most Voted<<
"""

#------------------------------------------------------QUESTION 18-------------------------------------------------------------(TUPLAS)

"""
tup = (1,) + (1, )
tup = tup + tup
print(len(tup))

#A. 2
#B. 4 >>Most Voted<<
#C. The snippet is erroneous (invalid syntax)
"""

#------------------------------------------------------QUESTION 19-------------------------------------------------------------(TUPLAS)

"""
data = (1, 2, 4, 8)
data = data[-2:-1]
data = data[-1]
print(data)

#A. (4)
#B. 4 >>Most Voted<<
#C. (4,)
##D. 44
"""

#------------------------------------------------------QUESTION 20-------------------------------------------------------------(LISTAS)

"""
my_list = [1,2]

for v in range(2):

    my_list.insert(-1,my_list[v]) #LO AGREGA EN LA POSICION PERO NUNCA AL FINAL
    #[1,2]   -> [1, *1 nuevo*, 2]
    #[1,1,2] -> [1, 1, *1 nuevo*, 2]
    #[1,1,1,2]
    
print(my_list)

#A. [1, 1, 2, 2]
#B. [1, 1, 1, 2] >>Most Voted<<
#C. [1, 2, 1, 2]
#D. [1, 2, 2, 2]
"""

#------------------------------------------------------QUESTION 21-------------------------------------------------------------(LISTAS)

"""
data = [1,2,3,None,(),[],]
print(len(data))

#A. 4
#B. 6 >>Most Voted<<
#C. 5
#D. 3
"""

#------------------------------------------------------QUESTION 22-------------------------------------------------------------(LECTURAS)

"""
#A data structure described as LIFO is actually a:

#A. stack >>Most Voted<<
#B. tree
#C. list
#D. heap
"""

#------------------------------------------------------QUESTION 23-------------------------------------------------------------(DICCIONARIOS)

"""
#How would you remove all the items from the d dictionary? Expected output: {}

d = {"1":"A","2":"B","3":"C"}
#A. d.del()
#B. d.remove()
#C. del d
#D. d.clear() >>Most Voted<<
print(d)
"""

#------------------------------------------------------QUESTION 24-------------------------------------------------------------(DICCIONARIOS)

"""
data = {"one":"two","three":"one","two":"three"}
res = data["three"]

for _ in range(len(data)):
    res = data[res]
print(res)

#A. three
#B. ('one', 'two', 'three')
#C. two
#D. one >>Most Voted<<
"""

#------------------------------------------------------QUESTION 25-------------------------------------------------------------(DICCIONARIOS)

"""
data = {"edad":"juan","años":"11"}
person = data.copy()

my_lits1 = [1,2,3,4]
my_lits2 = my_lits1

print(id(data)==id(person)) #DISTINTO LUGAR DE MEMORIA
print(id(my_lits1)==id(my_lits2)) #MISMO LUGAR DE MEMORIA

#A. False >>Most Voted<<
#B. 1
#C. 0
#D. True
"""

#------------------------------------------------------QUESTION 26-------------------------------------------------------------(LISTAS)

"""
my_list = [1,2,3,4,"A"]

#CODIGO AQUI

print(my_list)

#A. reverse(list)
#B. list.reversed()
#C. list.reverse() >>Most Voted<<
#D. reversed(list)
"""

#------------------------------------------------------QUESTION 27-------------------------------------------------------------(TUPLAS)

"""
data1 = "1", "2"
data2 = ("3","4")
print(data1+data2)

#A. ['1', '2', '3', '4']
#B. (1, 2, 3, 4)
#C. ('1', '2', '3', '4') >>Most Voted<<
#D. The code is erroneous.
"""

#------------------------------------------------------QUESTION 28-------------------------------------------------------------(TUPLAS)

"""
data = (1,2,4,8)
data = data[1:-1]
data = data[0]
print(data)

#A. (2)
#B. (2,)
#C. 2 >>Most Voted<<
#D. The code is erroneous.
"""

#------------------------------------------------------QUESTION 29-------------------------------------------------------------(LISTAS)

"""
my_list = [3,1,-2]
print(my_list[my_list[-1]])

#A. -2
#B. 3
#C. -1
#D. 1 >>Most Voted<<
"""

#------------------------------------------------------QUESTION 30-------------------------------------------------------------(LECTURAS)

"""
#An alternative name for a data structure called a stack is:

#A. LIFO >>Most Voted<<
#B. FIFO
#C. FOLO
"""

#------------------------------------------------------QUESTION 31-------------------------------------------------------------(LISTAS)

"""
w = [1,2,3,4,5]
a = w[1:]
b = a[1:]
y = w

b[0] = 0 #SIN CONECTAR
y[1] = 0 #CON CONEXION
print(w)

#A. [7, 3, 23, 42]
#B. [7, 20, 23, 42] >>Most Voted<<
#C. [10, 20, 42]
#D. [10, 20, 23, 42]
"""

#------------------------------------------------------QUESTION 32-------------------------------------------------------------(LISTAS)

"""
nums1 = []
nums2 = nums1
nums2.append(1)

#A. vals is longer than nums
#B. nums and vals are of the same length >>Most Voted<<
#C. nums is longer than vals
"""

#------------------------------------------------------QUESTION 33-------------------------------------------------------------(DICCIONARIOS)

"""
data = {"a":1,"b":2,"c":3}
print(data["a","b"])

#A. (1, 2)
#B. The code is erroneous. >>Most Voted<<
#C. {'a':1, 'b':2}
#D. [1,2]
"""

#------------------------------------------------------QUESTION 34-------------------------------------------------------------(FOR)

"""
elements = [i for i in range(-1,-2)]
print(len(elements))

# A. one
# B. two
# C. three
# D. zero >>Most Voted<<
"""

#------------------------------------------------------QUESTION 35-------------------------------------------------------------(LISTAS)

"""
my_list = [0,1,2,3]
x=1

for element in my_list:
    x *=element
print(x)

# A. 1
# B. 0 >>Most Voted<<
# C. 6
"""

#------------------------------------------------------QUESTION 36-------------------------------------------------------------(LISTAS)

"""
num = [1,2,3]
data = ("peter",) * (len(num)-num[::-1][0])
print(data)

#A. ('Peter', 'Peter',)
#B. PeterPeter
#C. The code is erroneous.
#D. ('Peter')
#E. () >>Most Voted<<
"""

#------------------------------------------------------QUESTION 37-------------------------------------------------------------(TUPLAS)

"""
t1 = (1,2,3)
t2 = ("A","D","Z")
t3 = (True,False,None)
t4 = (5.0, 7.5, 9.9)

t1, t3 = t2, t4
print(t1)

#A. The program will cause an error.
#B. (1, 4, 9)
#C. ('A', 'D', 'Z') >>Most Voted<<
#D. (5.0, 7.5, 9.9)
"""

#------------------------------------------------------QUESTION 38-------------------------------------------------------------(METODOS)

"""
data = ()
print(data.__len__() == len(data))

#A. The code is erroneous.
#B. 1
#C. 0 >>Most Voted<<
#D. None
"""

#------------------------------------------------------QUESTION 39-------------------------------------------------------------(LISTAS)

"""
fruits1 = ["Apple","Pear","Banana"]
fruits2 = fruits1
fruits3 = fruits1[:]

fruits2[0]="Cherry"
fruits3[1]="Orange"

res = 0

for i in (fruits1,fruits2,fruits3):
    if i[0]=="Cherry":
        res +=1
    if i[1]=="Orange":
        res+=10
print(res)

#A. 22
#B. 12 >>Most Voted<<
#C. 0
#D. 11
"""

#------------------------------------------------------QUESTION 40-------------------------------------------------------------(TUPLAS)

"""
data = (1,) * 3
data[0] = 2
print(data)

#A. (2, 1, 1)
#B. (1, 1, 1)
#C. (2, 2, 2)
#D. The code is erroneous. >>Most Voted<<
"""

#------------------------------------------------------QUESTION 41-------------------------------------------------------------(LISTAS)

"""
list = [6,7,8,3]
print(list.sort(),end=" == ") #MODIFICA LA LISTA ORIGINAL

list = [6,7,8,3]
print(sorted(list)) #ORDENA SIN MODIFICAR LA LISTA ORIGINAL >>Most Voted<<
"""

#------------------------------------------------------QUESTION 42-------------------------------------------------------------(LISTAS)

"""
#Which of the following sentences are true about the code? (Choose two.)

nums = [1,2,3]
vals = nums

#A. nums and vals are different lists
#B. vals is longer than nums
#C. nums and vals are different names of the same list >>Most Voted<<
#D. nums and vals have the same length >>Most Voted<<
"""

#------------------------------------------------------QUESTION 43-------------------------------------------------------------(LISTAS)

"""
vals = [1,2,3]
vals[0],vals[1]=vals[1],vals[2]

#A. extends the list
#B. doesn't change the list's length >>Most Voted<<
#C. shortens the list
"""

#------------------------------------------------------QUESTION 44-------------------------------------------------------------(LISTAS)

"""
data = ["abc","def","abcde","efg",]
print(max(data))

#A. efg >>Most Voted<<
#B. abc
#C. def
#D. The code is erroneous.
#E. abcde
#F. None of the above.
"""

#------------------------------------------------------QUESTION 45-------------------------------------------------------------(FUNCIONES)

"""
#Which function does in-place reversal of objects in a list?

#A. list.sort([func])
#B. list.pop(obj=list[-1])
#C. list.remove(obj)
#D. list.reverse() >>Most Voted<<
"""

#------------------------------------------------------QUESTION 46-------------------------------------------------------------(LISTAS)

"""
my_list1 = [1,2,3]
my_list2 = []

for v in my_list1:
    my_list2.insert(0,v)
print(my_list2)

#A. [1, 2, 3]
#B. [3, 3, 3]
#C. [3, 2, 1] >>Most Voted<<
#D. [1, 1, 1]
"""

#------------------------------------------------------QUESTION 47-------------------------------------------------------------(FNCIONES)

"""
def find_high_low(nums): >>Most Voted<<
    nums.sort()
    return nums[-1], nums[0]

data = [8,6,7,4,2,3,5,1,10,9]
high, low = find_high_low(data)

print(high,low)
"""

#------------------------------------------------------QUESTION 48-------------------------------------------------------------(LISTAS)

"""
my_list = ["A","B","C","D","E"]

def my_list(my_list):
    del my_list[3]
    my_list[3] = "ram"

print(my_list(my_list))

#A. ['Mary', 'had', 'a', 'little', 'lamb']
#B. ['Mary', 'had', 'a', 'lamb']
#C. ['Mary', 'had', 'a', 'ramb']
#D. No output, the snippet is erroneous >>Most Voted<<
"""

#------------------------------------------------------QUESTION 49-------------------------------------------------------------(LISTAS)

"""
data = ["peter","paul","mary"]
print(data[int(-1/2)])

#A. Paul
#B. Mary
#C. The code is erroneous.
#D. None of the above.
#E. Peter >>Most Voted<<
"""

#------------------------------------------------------QUESTION 50-------------------------------------------------------------(TUPLAS)

"""
data = 1,2,3,4
data = data[-2:-1]
data = data[-1]
print(data)

#A. 1
#B. 4
#C. 3 >>Most Voted<<
#D. 2
"""

#------------------------------------------------------QUESTION 51-------------------------------------------------------------(DICCIONARIOS)(.VALUES)

"""
dicy = {"1":"0","0":"1"}

for d in dicy.vals(): #.VALUES
    print(d, end=" ")

#A. 0 1
#B. 1 0
#C. The code is erroneous. >>Most Voted<<
#D. 0 0
"""

#-----------------------------------------------------------FINAL----------------------------------------------------------------

"""
a=1
b=2
c=3
d=4
print(a+b*c-d)
"""