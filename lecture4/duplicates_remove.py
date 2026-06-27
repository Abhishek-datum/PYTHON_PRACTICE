l=[10,25,33,99,66,10,77,66,55,23]
unElement=[]
for a in l:
    if a not in unElement:
        unElement.append(a)

print(unElement)
print(sorted(unElement))