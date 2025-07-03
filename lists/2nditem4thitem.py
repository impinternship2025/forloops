# Printing 2nd and last item in a list

fruits = ["Orange","Guava","Apple","Banana","Watermelon"]

for i in range(len(fruits)):
    if i == 1:
        print("2nd fruit:",fruits[i])
    if i == len(fruits) - 1:
        print("Last fruit:",fruits[i])
