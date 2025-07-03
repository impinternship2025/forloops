# Printing the 2nd and last fruit in the list

fruits = ["Orange", "Guava", "Apple", "Banana", "Watermelon"]

for i in range(len(fruits)):
    if i == 1:
        print(f"The second fruit in the list is: {fruits[i]}")
    if i == len(fruits) - 1:
        print(f"The last fruit in the list is: {fruits[i]}")
