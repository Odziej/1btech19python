# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, W, X, Y, Z
#Szyfr ( litera * 3 )
#Np. KOT = NSX / UNJX = PIES

#FUNKCJA ord() - Zwraca kod ASCII znaku
#NP. print(ord("A")) zwraca 65 a print(ord("Z")) - Zwraca 90

#Funkcja chr() - zwraca znak dla danego kodu znak np:
# print(chr(75)) - Zwróci "K" 

#Wypisz alfabet
'''
for i in range(65, 91):
  print(chr(i), end=" ")

napis = "SERS OF THE WORLDS"
print(napis[0], napis[1], napis[2])

for i in range(len(napis)):
  print(napis[i])
'''

napis = input("Zakoduj cezarem ")
kod = ""

for i in range(len(napis)):
  kod = kod + chr(ord(napis[i])+3)
print(kod)
