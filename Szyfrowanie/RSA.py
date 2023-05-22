#Komenda na NWD
'''
from math import gcd
print(gcd(20,15))
'''

#a)
p = 163
q = 241
print(p,q)

#b)
n = p * q
F = (p-1)*(q-1)
print(n)
print(F)

#c)
from math import gcd
for i in range(2,F):
  if gcd(i,F) == 1:
    e = i
    break
print(e,n)

#d)
for j in range(2,F):
  if ((j*e) % F) == 1:
    d = j
    break
print(d,n)

#e)
m = input()
for i in m:
  print((ord(i)**e)%n)