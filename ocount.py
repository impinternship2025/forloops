
# Counting the number of times the letter 'o' appears in a given sentence.

def count_o_in_sentence(sentence):
    """
    For loop is used to find the count of o in the sentence
    """
    try:
        count = 0
        for char in sentence:
            if char == 'o':
                count += 1
        return count
    except:
        print("Please provide a valid sentence (string).")
        return None

sentence = "Anush is at office today"
result = count_o_in_sentence(sentence)
if result is not None:
    print("The number of times 'o' appears:", result)
