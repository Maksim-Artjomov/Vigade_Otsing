from math import *

print("Ruudu karakteristikud") 
a=float(input("Sisesta ruudu külje pikkus => ")) #Добавил float
S=float(a)**2 #Добавил float
print("Ruudu pindala", S)
P=4*float(a) #Добавил float
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) #Убрал *math.
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #Убрал лишнюю скобку
b=input("Sisesta ristküliku 1. külje pikkus => ")
c=input("Sisesta ristküliku 2. külje pikkus => ")
S=float(b)*float(c) #Добавил 2 float
print("Ristküliku pindala", S) #Поставил правильные ковычки
P=2*(float(b)+float(c)) #Добавил float
print("Ristküliku ümbermõõt", P)
di=sqrt(float(b)**2+float(c)**2) #Убрал math., добавил 2 раза float и 2 *.
print("Ristküliku diagonaal", round(di,1)) #Добавил скобку, правильно вписал команду round
print()
print("Ringi karakteristikud")
r=input("Sisesta ringi raadiusi pikkus => ") #Убрал лишнюю скобку, поставил правильные ошибки
d=2*float(r) #Добавил float и знак умножения
print("Ringi läbimõõt",d) #Добавил запятую
S=pi*float(r)**2 #Добавил float, убрал скобки у числа pi и добавил к знаку r
print("Ringi pindala",round(S,2)) #Правильно вписал команду round
C=2*pi*float(r) #Добавил float, убрал скобки у числа pi и добавил к знаку r
print("Ringjoone pikkus",round(C,2)) #Правильно вписал команду round