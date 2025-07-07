#Write a program that checks if “apple” is in the list [“banana”, “cherry”, “apple”, “mango”] and prints an appropriate message.

def check_fruit_in_list(fruit_list,fruit_to_check):
    if fruit_to_check in fruit_list:
        print(fruit_to_check + " is in the list")
    else:
        print(fruit_to_check + " is not in the list")
        
fruit_list = ["banana","cherry","apple","mango"]
check_fruit_in_list(fruit_list,"apple")        


    