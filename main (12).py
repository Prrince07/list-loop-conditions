# List of numbers
numbers = [10, 25, 40, 55, 60, 75, 90]


for num in numbers:
   
    if num < 50:
        continue  
    
    # Conditional statement
    if num % 2 == 0:
        print(num, "→ Even number and greater than or equal to 50")
    else:
        print(num, "→ Odd number and greater than or equal to 50")
