# Replace the letter 'a' with 'X' in the string

def replace_a_with_X(sentence):
    """
    This function replaces all the occurences of letter 'a' with the letter 'X'. It uses a for loop
    to iterate over each character in the string and checks if it's 'a'. If it is 'a', it replaces 'a' with 'X'
    
    """
    try:
        result = ""
        for ch in sentence:
            if ch == 'a':
                result += 'X'
            else:
                result += ch
        return result
    except:
        print(" Please provide a valid sentence (string).")
        return None
    
sentence = "Anush is at office today"
result = replace_a_with_X(sentence)
if result is not None:
    print("The replaced sentence is:", result)
    