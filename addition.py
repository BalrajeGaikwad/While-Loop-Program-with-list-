number = 12345 
sum_of_digits = 0


for i in range(5): 
    digit = number % 10  
    sum_of_digits += digit  
    number = number // 10  

print(f"The sum of digits is {sum_of_digits}")
