#Count how many times “apple” appears in the list: [“apple”, “banana”, “apple”, “cherry”, “apple”].

def count_fruit_in_list(fruit_list, fruit_to_count):
    count = 0
    for fruit in fruit_list:
        if fruit == fruit_to_count:
            count += 1
    print(f"The number of '{fruit_to_count}' in the list is:", count)


fruits = ["Apple", "Banana", "Apple", "Cherry", "Apple"]


count_fruit_in_list(fruits, "Apple")