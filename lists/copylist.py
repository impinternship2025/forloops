#Create a copy of the list students = [“Anjali”, “Ravi”, “Meera”] and modify the original list. 
# Show that the copy remains unchanged.
 

def copy_modify_list(original_list,item_to_add):
    copied_list = original_list.copy()
    
    original_list.append(item_to_add)

    print("Original list after modification:", original_list)
    print("Copied list (unchanged):", copied_list)   


students = ["Anjali","Ravi","Meera"]

copy_modify_list(students,"John")