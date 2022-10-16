#Zad 1
'''
L= int(input("Wpisz liczbę aby sprawdzić czy dzieli się przez 3! "))

if L % 3 == 0:
  print("tak")
else:
  print("nie")

#Zad 2

L= int(input("Wpisz liczbę aby sprawdzić czy dzieli się przez 17! "))

if L % 17 == 0:
  print("tak")
else:
  print("nie")

#Zad 3

wiek= int(input("Wpisz swój wiek! "))

if wiek < 18:
  print("Nie masz dostępu byczku :/ ")
else:
  print("Spoko byczek, masz dostęp ;) ")


#Zad 4

MAX = 20

Waga = int(input("Wpisz wagę ciężarówki w tonach ! "))

if Waga > MAX:
  print("ZAKAZ WJAZDU NA MOST BYDLAKU!")
else:
  print("Gut tu goł")


#Zad 5

L1 = int(input("Wpisz liczbę 1. "))
L2 = int(input("Wpisz liczbę 2. "))
L3 = int(input("Wpisz liczbę 3. "))

if L1 > L2 and L2 < L3:
  print("TAK")
else:
  print("NIE")

#Zad 6

a = int(input("A "))
p = int(input("P "))

if (a**p-a) % p == 0:
  print("TAK")
else:
  print("NIE")
'''

#Zad 7
s = int(input())
p = int(input())
k = int(input())

if (s*3)+p >= k:
  print("TAK")
else:
  print("NIE")

