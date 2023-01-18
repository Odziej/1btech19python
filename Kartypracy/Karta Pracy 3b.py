'''
#Zad 1
for i in range(1,31,1):
  print(i,"listopada 2022")


#Zad 2

a = 1
while True:
  print(a**2)
  a += 2


#Zad 3

for i in range(1137, 10000, 379):
  print(i)

#Zad 4

for i in range(100, 1000):
  if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
    print(i)


#Zad 5
n = int(input("Podaj ilość liczb "))
liczba = 0
for i in range(n):
  liczba += int(input())
print(liczba)

#Zad 6
k = int(input())
liczba = 0
for i in range(2,2 * (k+1), 2):
  liczba += i
print(liczba)



#Zad 7
m = int(input())
liczba = 0
for i in range(11, 100, 2):
  liczba += i
print(liczba)

#Potem
'''
#Zad 9
n = int(input("n = "))
num = 0
for i in range(n):
    num += (100*i)+21
print(num)