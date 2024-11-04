def binary_to_decimal(): 
   
     binary_code = input("Enter the binary code (only 0s and 1s): ") 
    
     try:
          
        decimal_value = int(binary_code, 2)
        print(f"The decimal value is: {decimal_value}") 
     except ValueError: 
          print("Invalid binary code! Please enter only 0s and 1s.") 

binary_to_decimal()
