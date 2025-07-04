#list comprehension
#leave the alternate number in the list and return the remaining.
#[1,2,3,4,5,6]

numbers = [1, 2, 3, 4, 5, 6]
kept = numbers[::2]

remaining = [num for num in numbers if num not in kept]

print("The remaining numbers after removing alternates are:", remaining)
