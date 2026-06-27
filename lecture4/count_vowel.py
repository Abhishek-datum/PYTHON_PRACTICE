#Task count vowel in a  string.
text=input("Enter the text:-")
count=0
for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("The number of vowel is : ",count)
  