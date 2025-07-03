def multiply_numbers_by_2(numbers,multiplier_no):
    for num in numbers:
        print(num * multiplier_no)
        print(f"{num} x {multiplier_no} = {num * multiplier_no}")

numbers = [12,14,16]     
multiplier_no = 2   
multiply_numbers_by_2(numbers,multiplier_no) 
