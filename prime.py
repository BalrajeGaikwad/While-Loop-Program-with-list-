#Prime Numbers and Python While Loop
#Using a while loop, we will construct a Python program to verify if the given integer is a prime number or not.


num = [34, 12, 54, 23, 75, 34, 11]    

for number in num:
    condition = 0  
    iteration = 2  
    while iteration <= number / 2:  
        if number % iteration == 0:  
            condition = 1  
            break  
        iteration = iteration + 1  

    if condition == 0:  
        print(f"{number} is a PRIME number")  
    else:  
        print(f"{number} is not a PRIME number")


number = 23  

if number > 1: 
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a PRIME number")
            break
    else:
        print(f"{number} is a PRIME number")
else:
    print(f"{number} is not a PRIME number")



num = [34, 12, 54, 23, 75, 34, 11]

for number in num:
    if number > 1:  # Prime numbers are greater than 1
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a PRIME number")
                break
        else:
            print(f"{number} is a PRIME number")
    else:
        print(f"{number} is not a PRIME number")

