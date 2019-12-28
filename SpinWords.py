############################# MY SOLUTION ########################################

def spin_words(sentence):
    for word in sentence.split():
        if len(word) > 4:
            sentence = sentence.replace(word, word[::-1])
    return sentence

##################################################################################

def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

##################################################################################
