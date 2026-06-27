# Task2. PAN Card Number Validation(Using String Conditions Only)
# The PAN number must be excatly 10 character long.
# The first five characters must be alpha numeric
#The next four charater is digit
# The last character must be an uppercase English letter(A-Z)

pan=input("Enter the PAN number:-").upper()
if (len(pan)==10 and
    pan[:5].isalpha() and
    pan[5:9].isdigit()and
    pan[9].isalpha()
   ):
    print("valid PAN number")
else:
    print("Invalid PAN number")

            