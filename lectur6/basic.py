def showCompanyname():
    print("welcome to ws")

showCompanyname()
showCompanyname()
print("ws")
print("hello")

def addData():
    print(10+20)
addData()

def addData(num1,num2):
    print(num1+num2)

addData(25,30)
addData(10,100)
def minData(num1,num2):
    print(num1-num2)
minData(90,20)

def userInfo(name,age):
    print(name,age)
userInfo("abhishek",25)

def square(n):
    return n*n
print(square(4))

x=eval("20.5")
print(x)

def square(num):
    return(num*num)
print(square(18))

def addData(n=2,m=1):
    print(n+m)
addData()
def sumData(*x):
    print(x)

sumData(10,20,30,40,99)

def display():
    msg="welcome to ws"
    print(msg)
display()

x=10


def displayData1():
    global x
    x=20
    print(x)
def displayData2():
    print(x)


displayData1()
displayData2()

add=lambda a,b: a+b
print(add(2,3))

square=lambda x:x*x
print(square(10))

def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
print(factorial(11))