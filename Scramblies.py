def scramble(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if len(s2) < 1:
        return True
    elif s2[0] in s1:
        return scramble(s1[1:], s2[1:])
    else:
        return False

def scramble(s1, s2):
    d = dict()
    for letter in set(s2):
        d[letter] = s2.count(letter)
    for k,v in d.items():
        if s1.count(k) < v:
            return False
    return True

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

ss = 'cedewaraaossoqqyt'
dd = 'codewars'

a = 'scriptingjava'
b = 'javascript'

print(scramble(a, b))
