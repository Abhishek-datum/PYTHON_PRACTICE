# Task 1. Aadhaar card 16 digit validation(using string condition only
userInput=input("Enter the aadhar card number (16 Digit):-")
if userInput.isdigit() and len(userInput)==16:
    print("valid aadhar car")
else:
    print("Invalid aadhar card number")
  