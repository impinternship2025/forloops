#2.	Write a Python program to create a list of fruits and print the second and last elements.
#Change an Item in a List


def print_fruit_by_position(fruits, position):
    if position == "first":
        print("The first fruit is: ", fruits[0])
    elif position == "second":
        print("The second fruit is:", fruits[1])
    elif position == "third":
        print("The third fruit is:", fruits[2])
    elif position == "last":
        print("Last fruit:", fruits[-1])
    elif position == "last_but_one":
        print("Last but one fruit:", fruits[-2])
    else:
        print("Invalid position")


fruits = ["Orange", "Guava", "Apple", "Banana", "Watermelon"]

print_fruit_by_position(fruits, "third")
print_fruit_by_position(fruits, "last_but_one")
