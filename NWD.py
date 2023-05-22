'''
#2 algorytmy NWD

#odejmowanie
while a != b:
  if a > b: a = a - b
  if b > a: b = b - a
print(a)


#Modulo

while b > 0:
  a, b = b, a%b
print(a)

# Przyklad odejmowania
a = 36
b = 24
while a != b:
  if a > b: a = a - b
  if b > a: b = b - a
print(a)


#Przykład modulo
a = 34
b = 24
while b > 0:
  a, b = b, a%b
print(a)
'''

a = 36
b = 24
while b > 0:
  a, b = b, a%b
print(a)