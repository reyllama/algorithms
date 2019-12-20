###################### MY SOLUTION ######################################

def digital_root(n):
    while n>=10:
        n = sum([int(str(n)[i]) for i in range(len(str(n)))])
    return n

##########################################################################

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

##########################################################################

def digital_root(n):
    return n%9 or n and 9

##########################################################################



print(digital_root(456))
