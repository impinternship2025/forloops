from ocount import count_o_in_sentence
from replaceletter import replace_a_with_X
from reverseword import reverse_each_word
from reversestring import reverse_sentence


sentence = "Anush is at office today"
result = count_o_in_sentence(sentence)
if result is not None:
    print("The number of times 'o' appears:", result)

sentence = "Anush is at office today"
result = replace_a_with_X(sentence)
if result is not None:
    print("The replaced sentence is:", result)
    
sentence = "Anush is at office today"
result = reverse_each_word(sentence)
if result is not None:
    print("Sentence with each word reversed:", result)

sentence = "Anush is at office today"
result = reverse_sentence(sentence)
if result is not None:
    print("The reversed sentence is :", result)    


