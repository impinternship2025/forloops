#Add and Remove Elements
#Start with an empty list. Add the numbers 1 through 5 using. append(), then remove the third element using .remove() or del.

numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

print(f"List after adding numbers 1 to 5: {numbers}")

numbers.remove(3)

print(f"List after removing the number 3: {numbers}")