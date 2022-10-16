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
'''

#Zad 4

print("Wpisz 4 różne liczby całkowite!")

a = int(input("Wpisz liczbę A. "))
b = int(input("Wpisz liczbę B. "))
c = int(input("Wpisz liczbę C. "))
d = int(input("Wpisz liczbę D. "))

if a < b:
  if a < c:
    print (a)
    else:
      print (c)
      elif b < c:
      print b
      else:
        print c
