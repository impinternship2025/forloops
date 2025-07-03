#Combine list1 = [1, 2, 3] and list2 = [4, 5, 6] into a new list and print the result.

numbers1 = [1,2,3]
numbers2 = [4,5,6]

for x in numbers2:
    numbers1.append(x)

print("The new combined list is:",numbers1)  