# Reverse each word and then put it in a sentence

def reverse_each_word(sentence):
    """
    This function takes a sentence , reverses each word in the sentence and then puts it back in a sentence.
    """
    try:
        words = sentence.split()
        reverse_words = []
        for word in words:
            reverse_word = ""
            for char in word:
                reverse_word = char + reverse_word
            reverse_words.append(reverse_word)

        return " ".join(reverse_words)
    except:
        print("Oops! Please provide a valid sentence (string).")
        return None

sentence = "Anush is at the office today"
result = reverse_each_word(sentence)
if result is not None:
    print("Sentence with each word reversed:", result)


