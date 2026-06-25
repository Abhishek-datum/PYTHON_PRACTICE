print('''
      + add
      - sub
      * multiply
      / division
      ''')
num1=eval(input("Enter the value 1:-"))
num2 = eval(input("Enter the value2:-"))
opr =input("enter the user choice-")
match opr:
    case '+':
        print (num1+num2)
    case '-':
        print(num1-num2)
        print(num1/num2)
    case _:
        print("invalid character")