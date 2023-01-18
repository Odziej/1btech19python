'''
#Zad 1
a = int(input())
b = int(input())
c = int(input())

# Arytmetyczny:

if b - a == c - b:
  print("Arytmetyczne")
# geometryczne
if b/a == c/b:
  print("Geometryczne")





#Zad 2
suma = 0

for i in range(100, 1000):
  if i % 8 == 0 and i % 16 != 0:
    suma = suma + i
print(suma)

#Zad 3
for i in range(99, 9,-1):
  if i % 7 == 0:
    wielość = i
    break

ilość = 0
for i in range(1000, 10000):
  if i % wielość == 0:
    ilość = ilość + 1
print(ilość)

#Zad 4
ilość = 0
for i in range(10, 100):
  cd = i // 10
  cj = i % 10
  if cd >= 2 * cj:
    ilość += 1
print(ilość)
'''






