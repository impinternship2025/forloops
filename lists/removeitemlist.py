#Removing an item from a list using remove function

def remove_car_from_list(car_list, car_to_remove):
    if car_to_remove in car_list:
        car_list.remove(car_to_remove)
        print("The updated list is:", car_list)
    else:
        print(f"{car_to_remove} not found in the list.")


cars = ["Toyota", "Hyundai", "Nissan", "Mercedes"]

remove_car_from_list(cars, "Toyota")
