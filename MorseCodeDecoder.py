################################# MORSE_CODE dictionary PRE-DEFINED #############################

def decodeMorse(morse_code):
    t = morse_code.strip().split('   ')
    s = [item.split() for item in t]
    words = []
    for word in s:
        words.append("".join([MORSE_CODE[item] for item in word]))
    return " ".join(words)
