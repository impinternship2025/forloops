#Add an item to the list
def add_fruit(fruits, new_fruit):
    fruits.append(new_fruit)
    print(f"Updated fruit list after adding '{new_fruit}': {fruits}")

fruits = ["Apple", "Cherry", "Orange"]


add_fruit(fruits, "Strawberry")
