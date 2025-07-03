#Multiplying numbers in a list by 2

def multiply_numbers_by_2(numbers,multiplier_no):
    for num in numbers:
        print(f"{num} x {multiplier_no} = {num * multiplier_no}")

numbers = [12,14,16]     
multiplier_no = 2   
print("The multiplied numbers are:",multiply_numbers_by_2(numbers,multiplier_no))
