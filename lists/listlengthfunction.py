#Write a function that returns the length of any given list

def get_list_length(lst):
    count = 0
    for i in lst:
        count += 1
    return count


my_list = ["Cherry", "Apple", "Banana", "Mango", "Pineapple","Strawberry"]
length = get_list_length(my_list)
print("Length of the list is:", length)
