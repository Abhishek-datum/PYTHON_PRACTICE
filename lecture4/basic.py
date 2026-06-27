w="welcome"
print(w[-1])
print(w[0:3])
print(w[0: :1])
print(w[0: :2])
print(w[-1: :-1])
print(w[-4: : ])
print(w[-4: :-1])
t=len(w)
print(t)

for a in range(t):
    print(a,w[a])

for a in range(t-1,-1,-1):
     print(a,w[a]) 