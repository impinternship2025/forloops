def common_items_in_2_lists(numbers1, numbers2):
    common_items = []

    for item in numbers1:
        
        if item in numbers2 and item not in common_items:
            common_items.append(item)

    return common_items        

numbers1 = [12,14,17,19]
numbers2 = [12,18,17,21]
print("The common items in 2 lists are :",common_items_in_2_lists(numbers1, numbers2)) 


