'''
#1
a = 0
for i in range(100,1000):
   a = i + a
print(a)

#2
a = 0
b = 0
for i in range(10,100):
  if i % 6 == 0:
    a = i + a
    b = b + 1

print("Suma = ",a)
print("ilość = ",b)

#3
import random
l = []
a = random.randint(1000,10000)
b = random.randint(1000,10000)
c = random.randint(1000,10000)
d = random.randint(1000,10000)
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.sort()
print(l)
print(l[-1])

#4
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
a = int(input())
print(getSum(a))

#5
a = input()
b = [*a]
b.sort
print(b[0])

#6
def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
liczba = int(input())
print(czy_pierwsza(liczba))

#7
def czy_złożona(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False
liczba = int(input())
print(czy_złożona(liczba))
#8
a = int(input())
b = 24

while b > 0:
    a, b = b, a%b

    temp = a
    a = b
    b = temp%b
if a == 1:
  print("Tak")
else:
  print("Nie")

#9
napis = input("Zakoduj cezarem ")
kod = ""

for i in range(len(napis)):
  kod = kod + chr(ord(napis[i])+3)
print(kod)

#10
#https://www.youtube.com/watch?v=4ZUP0cWm_fE
def NWD(a, b):
  while b:
    a, b = b, a%b
  return a

def suma(a, b, c, d):
  NWW = b * d // NWD(b, d)
  e = a * NWW // b + c * NWW // d
  f = NWW
  print(str(e) + "/" + str(f))

licznik_1 = int(input("Licznik 1: "))
mianownik_1 = int(input("Mianownik 1: "))
licznik_2 = int(input("Licznik 2: "))
mianownik_2 = int(input("Mianownik 2: "))

print("\n" + str(licznik_1) + "/" + str(mianownik_1) + " +", end=" ")
print( str(licznik_2) + "/" + str(mianownik_2) + " =", end=" ")
suma( licznik_1, mianownik_1, licznik_2, mianownik_2)

#11
a = int(input())
b = int(input())
nww = a * b

while b > 0:
  r = a % b
  a = b
  b = r
nww = nww // a
print(nww)

#12
a = input()
b = a.lower()
print(b.count("c"))


#13
def funkcja(wyraz):
  for i in range(1, len(wyraz)):
    if wyraz[i] < wyraz[i - 1]:
      return False
    return True
wyraz = input()
nierosnący = funkcja(wyraz)
if nierosnący:
  print("Tak")
else:
  print("Nie")

#14
a = [input(), input(), input()]
b = sorted(a , key=len)

print(b[-1])
'''
