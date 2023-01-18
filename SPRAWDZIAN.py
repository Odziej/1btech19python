

#Zad 1

a = int(input("Podaj pierwszą cyfre hasła! "))
b = int(input("Podaj drugą cyfre hasła! "))
c = int(input("Podaj trzecią cyfre hasła! "))

if b - a == 1 or a - b == 1:
  print("Złe hasło")
else:
  if b - c == 1 or c - b == 1:
    print("Złe hasło")
  else:
    print("Dobre haslo")


#Zad 2

n = int(input("Ilość ułamków "))
góra = 2
dół = 1
dodatek = 3
suma = 0
for i in range(n):
  suma += góra / dół
  góra + 1
  dół + dodatek
  dodatek + 2
print(suma)



