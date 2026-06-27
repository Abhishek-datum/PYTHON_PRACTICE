l=[10,20,30,30,40,50]
m=[40,50,60]
# o=[]
# for a in l:
#     for b in m:
#         if a==b:
#          o.append(a)
# print(o)

finallist=[]
for a in l:
    if a in m:
        finallist.append(a)
print(finallist)
