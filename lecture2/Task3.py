# Check if a number is divisible by both 3 and 5
number=eval(input("Enter the number:-"))
if(number%3==0 and number%5==0):
    print(number,"Divisible by both 3 and 5")
else:
    print(number,"Not divisible by both 3 and 5")