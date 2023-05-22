#Palidrom za pomocą tablicy
'''
s = input()

for i in range(len(s)//2):
  if s[i] != s[len(s)-1-i]:
    exit("Nie jest")
exit("Jest")

#anagram za pomocą tablicy
# dama i adam

#anagram za pomocą funkcji

a = input()
b = input()

A = list(a)
B = list(b)

A.sort()
B.sort()

a = "".join(A)
b = "".join(B)

print(a,b)

if a == b:
  print("TAK")
else:
  print("NIE")

'''

