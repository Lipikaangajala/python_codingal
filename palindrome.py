number=int(input("Enter your number : "))
original_number=number
reversedNumber=0
while number > 0:
    digit = number % 10
    reversedNumber = reversedNumber * 10 + digit
    number//=10

if original_number == reversedNumber:
   print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")
