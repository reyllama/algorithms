################################### MY SOLUTION #####################################################

def pig_it(text):
    t = text.split()
    pigged=[]
    for x in t:
        if x not in ['!', '.', ',', '?']:
            pigged.append(x[1:]+x[0]+'ay')
        else:
            pigged.append(x)
    return " ".join(pigged)

######################################################################################################

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

######################################################################################################




print(pig_it("Pig latin is cool"))
print(pig_it("This is my string"))
print(pig_it("This latin is cool !"))
