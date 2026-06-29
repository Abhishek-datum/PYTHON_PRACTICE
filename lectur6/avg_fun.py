def findavg(*args):
    total=0
    for num in args:
     total+=num
    average=total/len(args)
    return average
print(findavg(10,20,30,40,50))