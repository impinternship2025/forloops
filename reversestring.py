# Print a given reverse string

def reverse_sentence(sentence):
    """
    For loop is used to reverse the sentence
    """
    try:
        reversed_str = ""
        for ch in sentence:
            reversed_str = ch + reversed_str
        return reversed_str
    except:
        print("Please provide a valid sentence (string).")
        return None
    
sentence = "Anush is at office today"
result = reverse_sentence(sentence)
if result is not None:
    print("The reversed sentence is :", result)    