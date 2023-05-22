#Napisy (stringi) są "prawie listami"

# s = input()
#print(s)

# for x in s:
#   print(x)

# for i in range(len(s)):
#   print(s[i])

# L = [5,7,1,4]
# print(s, L)
# L.sort()
# print(s,L)
# s.sort() -> to nie działa, błąd
# print(s,L)

#Konwersja lista <-> napis (list(), )

s = input()
L = list(s)
print(s, L)
L.sort()
s = "" .join(L)
print(s, L)

s = input()
L = list(s)
R = list(s)
R.reverse()
if L == R:
  print("tak")
elif L != R:
  print("nie")