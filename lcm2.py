num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))



def find_lcm(a,b):
    def gcd(c,d):
        while d:
            c,d=d,c%d
        return c
    return abs(a*b)//gcd(a,b)



lcm=find_lcm(num1,num2)

print("The LCM of ",num1,"and",num2,"is : ",lcm)
