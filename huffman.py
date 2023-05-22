

W = "AAAAABBCCCCDDDEEEEEEEFGGG" # 5A2B4C3D7EF3G
ilość = 1
H = ""
W += "."
for i in range(len(W)):
  if W[i] == W[i+1]:
    ilość += 1
  else:
    if ilość > 1:
      H += str(ilość)
    H += W[i]
    ilość = 1
print(H)
'''
# NWD dla przykładowych liczb:
a = int(input())
b = int(input())
while(b>0):
  a, b = b, a%b
print(a)
'''
