#Changing the color from green to yellow

def change_color(color_list, new_color):
    color_list[1] = new_color
    print(f"The new list after changing the second color to '{new_color}': {color_list}")



colors = ["red", "green", "blue"]


change_color(colors, "yellow")
