##################### MY SOLUTION ##################################

def duplicate_count(text):
     x = [text.lower()[i] for i in range(len(text))]
     return sum([x.count(item)>=2 for item in set(x)])

####################################################################

def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

######################################################################

print(duplicate_count('indivisibility'))
