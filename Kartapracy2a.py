import random
'''
#Zad 1

a = int(input())
b = int(input())

if a + b //2 == 0:
  print("Parzysta")
else:
  print("Nie parzysta")


#Zad 2

a = int(input())
b = int(input())

ŚA = (a+b)/2
ŚG = (a*b)**(1/2)

if ŚA > ŚG:
  print("Tak")
else:
  print("Nie")


#Zad 3

k = int(input())
l = int(input())
m = int(input())

if k == l:
  print("Tak",k,l)
else:
  print("Nie")
if k == m:
  print("Tak",k,m)
else:
  print("Nie")
if l == m:
  print("Tak",l,m)
else:
  print("Nie")


#Zad 4

print("Wpisz 4 różne liczby całkowite!")

a = int(input("Wpisz liczbę A. "))
b = int(input("Wpisz liczbę B. "))
c = int(input("Wpisz liczbę C. "))
d = int(input("Wpisz liczbę D. "))

if a<b<c<d:
  print(a)
else:
  if b<c<d:
    print(b)
  else:
    if c<d:
      print(c)
    else:
      print(d)




#Zad 5

a = int(input("Wpisz liczbę A. "))
b = int(input("Wpisz liczbę B. "))
c = int(input("Wpisz liczbę C. "))

if a < c and b < c and a + b > c:
  print("Tak")
else:
  if c < b and a < b and c + a > b:
    print("Tak")
  else:
    if c < a and b < a and c + b > a:
      print("Tak")
    else:
      print("Nie")


#Zad 6

a = int(input("Wpisz liczbę A. "))
b = int(input("Wpisz liczbę B. "))
c = int(input("Wpisz liczbę C. "))

if a**2 + b**2 == c**2:
  print("Trójkąt prostokątny")
else:
  if c**2 > a**2 + b**2:
    print("Trójkąt rozwartokątny")
  else:
    print("Trójkąt ostrokątny")
'''

