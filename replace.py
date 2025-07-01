string = "Anush is at office today"
old_letter = "a"
new_letter = "X"
result = " "

for char in string:
    if char == old_letter:
        result += new_letter
    else:
        result += char
        
print(result)

    
