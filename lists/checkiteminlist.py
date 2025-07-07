# Check if Item is present in list

def check_color_in_list(color_list, color_to_check):
    if color_to_check in color_list:
        print(f"Yes, {color_to_check} is present in the list")
    else:
        print(f"No, {color_to_check} is not present in the list")


colors = ["red", "yellow", "brown"]


check_color_in_list(colors, "green")
