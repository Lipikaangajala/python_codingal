def setnumber(number,n):

    if number &(1<<(n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")
number=int(input("Enter a number : "))
n=int(input("Enter bit number : "))
setnumber(number,n)        
               
