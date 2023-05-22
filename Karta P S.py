import random
for i in range(1, 300):
  a = random.randint(1, 10000)
  b = random.randint(1, 10000)
  sA = 0
  sB = 0
  for i in range(1, a):
    if a % i == 0:
      sA += i
  for f in range(1, b):
    if b % f == 0:
      sB += f
      
  if sB == a + 1 and sA == b + 1:
    print("Tak")
  else:
    print("Nie")
