import string
import random

'''
for i in range(50, 100, 1):
  print(random.randint(1, 80), end=" ")
  print(i, end=" ")
'''
S = 10

ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
print("The randomly generated string is : " + str(ran)) # print the random data.





'''
print(random_line(Ser.txt))
'''