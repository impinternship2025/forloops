#Count how many times “apple” appears in the list: [“apple”, “banana”, “apple”, “cherry”, “apple”].

fruits = ["Apple","Banana","Apple","Cherry","Apple"]
apple_count = 0

for fruit in fruits:
    if fruit == "Apple":
        apple_count += 1

print("The number of apples in this list are:",apple_count)
