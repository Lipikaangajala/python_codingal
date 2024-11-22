def oddeven(n):
    if (n^1==n+1):
        return True
    
    else:
        return False
    
number=int(input("Enter a number : ") )  

if oddeven(number):
       print(number,"is even")
else:
    print(number,"is odd")    
def noofbits(n):
  count=0
  while (n):
        count += 1
        n >>=1

  return count

number = int(input("Enter your number :"))
print("total number of bits : ",noofbits(number))

num=10
num1=4

print("num and num1 =",num & num1)
print("/num | num1=",num | num1)
print("\n~num=",~num)
print("\nnum^num1=",num^num1)
print("num>>2=",num>>2)
print("num1<<2=",num1<<2)


