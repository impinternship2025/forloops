# Function to get all numbers that are multiples of 2 from a list
def get_multiples_of_2(number_list):
    multiples = [num for num in number_list if num % 2 == 0]
    print("The numbers that are multiples of 2 are:", multiples)


numbers = [10, 15, 20, 25, 30, 32, 34, 37, 40]

get_multiples_of_2(numbers)
