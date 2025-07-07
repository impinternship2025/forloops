#Write a function that takes two lists and returns a list of common elements between them.

def common_items_in_2_lists(kitchenA, kitchenB):
    common_items = []

    for item in kitchenA:
        if item in kitchenB and item not in common_items:
            common_items.append(item)

    return common_items


kitchenA = ["Stove", "Spatula", "Basin", "Water Cooler"]
kitchenB = ["Stove", "Spoons", "Basin", "Fruits"]


print("The common items between kitchenA and kitchenB are:", common_items_in_2_lists(kitchenA, kitchenB))
