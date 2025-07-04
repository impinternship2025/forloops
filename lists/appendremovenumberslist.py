#Add and Remove Elements
#Start with an empty list. Add the numbers 1 through 5 using. append(), then remove the third element using .remove() or del.

def add_delete_numbers():
    numbers = []

    
    for i in range(1, 6):
        numbers.append(i)

    print("List after adding 1 to 5:", numbers)

    del numbers[2]

    print("List after removing the third element:", numbers)

add_delete_numbers()

