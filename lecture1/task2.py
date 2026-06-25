# swap values of two variable and print before and after
# a=10
# b=20
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)
'''
x=10
y=20
x=x+y
y=x-y
x=x-y
print("x",x)
print("y",y)
'''
x=10
y=20
x,y = y,x
print("x",x)
print("y",y)