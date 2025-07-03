text = "Anush is at office today"

array_words = text.split(' ')

highest_length = 0
for word in array_words:    
    if len(word) > highest_length:
        print(len(word) > highest_length)
        highest_length = len(word)
        longest_word = word
    else:
        print(len(word) > highest_length)

print(highest_length)
print("The longest word is: ", longest_word)