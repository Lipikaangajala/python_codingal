def noOfbits(n):
    one=0
    zero=0

    while(n):
        if(n&1==1):
            one+=1
        else:
            zero+=1

        n>>=1 
    print("\n\none=",one,"\nzero",zero) 
number=int(input("Enter your number : "))
noOfbits(number)               
