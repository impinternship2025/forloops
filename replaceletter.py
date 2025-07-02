# Replace the letter 'a' with 'X' in the string

def replace_letter_in_sentence(sentence,target_letter,replacement_letter):
    """
    This function replaces all the occurences of letter 'a' with the letter 'X'. It uses a for loop
    to iterate over each character in the string and checks if it's 'a'. If it is 'a', it replaces 'a' with 'X'
    
    """
    try:
        result = ""
        for letter in sentence:
            if letter == target_letter:
                result += replacement_letter
            else:
                result += letter
        return result
    except:
        print(" Please provide a valid sentence (string).")
        return None
    
sentence = "Anush is at office today"
result = replace_letter_in_sentence(sentence,'a','X')
if result is not None:
    print("The replaced sentence is:", result)
    