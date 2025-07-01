string = "Anush is at the office today"

words = []
word = ""

for char in string:
    if char == ' ':
        words.append(word)
        word = ""
    else:
        word += char
words.append(word)  

result = ""

for i in range(len(words)):
    w = words[i]
    rev = ""
    for j in range(len(w)-1, -1, -1):
        rev += w[j]
    result += rev
    if i != len(words) - 1:
        result += " "

print(result)
