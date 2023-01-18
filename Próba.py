import string
import random

#Wersja 1
'''
for i in range(1, 2, 1):
  randóś =''.join(random.choices(string.digits, k = i))
  print("Wygenerowane liczby to:",str(randóś),end=" ",)
'''
 
#Próba udana

#Wersja 2

I = 1

hasło = ''.join(random.choices(string.digits, string.ascii_uppercase, I = k )

print(str(hasło))