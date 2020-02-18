################################# mY SOLUTION #################################

def order(sentence):
    temp = sentence.split()
    t = [''.join(sorted(word)) for word in temp]
    order = [word[0] for word in t]
    w_ord = [order[i]+temp[i] for i in range(len(temp))]
    return ' '.join([word[1:] for word in sorted(w_ord)])

s = "is2 Thi1s T4est 3a"
print(order(s))

################################# CLEVER #####################################

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

##############################################################################
