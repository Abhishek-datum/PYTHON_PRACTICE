# manual driven claculator
print('''
      + add
      - sub
      * multiply
      / division
      ''')
num1=eval(input("Enter the value 1:-"))
num2 = eval(input("Enter the value2:-"))
userCh =input("enter the user choice-")
if userCh =='+':
   print(num1+num2)
elif userCh =='-':
    print(num1-num2)
elif userCh =='/':
     print(num1/num2)
elif userCh =='*':
    print(num1*num2)
else:
    print("Invalid operation")