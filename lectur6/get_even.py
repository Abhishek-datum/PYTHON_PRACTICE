def getAllevenNumber(list):
    finalist=[ n for n in list if n%2==0 ]
    return finalist
    # for a in list:
    #     if a%2==0:
    #         finallist.append(a)
    # return finalist


output=getAllevenNumber([10,25,99,77,66,12,13,77,89,23])
print(output)