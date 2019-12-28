############################################# MY SOLUTION ###################################################################
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        from collections import Counter
        return True if (Counter(walk)['n'] == Counter(walk)['s']) & (Counter(walk)['e'] == Counter(walk)['w']) else False

##############################################################################################################################

def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

###############################################################################################################################
