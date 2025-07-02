
# Counting the number of times the letter 'o' appears in a given sentence.

def count_letters_in_sentence(sentence,letter_to_count):
    """
    For loop is used to find the count of o in the sentence
    """
    try:
        count = 0
        for letter in sentence:
            if letter == letter_to_count:
                count += 1
        return count
    except:
        print("Please provide a valid sentence (string).")
        return None

sentence = "Anush is at office today"
result = count_letters_in_sentence(sentence, 'o')
if result is not None:
    print("The number of times 'o' appears:", result)
