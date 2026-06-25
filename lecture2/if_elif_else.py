marks=eval(input("Enter the marks:-"))
if marks > 100 or marks<0:
    print("invalid number")
elif marks>=90:
    print('grade A')
elif marks >=75:
    print("grade b")
elif marks>=60:
    print("grade c")
else:
    print("Fail")