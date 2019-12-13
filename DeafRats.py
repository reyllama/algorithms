################################## MY ANSWER _ INCOMPLETE ##########################################

def count_deaf_rats(town):
    l = ["".join(item).strip() for item in town.split('P')]
    s0 = l[0].split("~O")
    s1 = l[1].split("O~")
    # t = [[s[i:i+2] for i ]]
    t0 = [len(item.strip()) >=1 for item in s0]
    t1 = [len(item.strip()) >=1 for item in s1]
    deaf = sum([len(item.strip()) >=1 for item in s0]) + sum([len(item.strip()) >=1 for item in s1])
    return deaf

######################################################################################################

def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')

######################################################################################################

ex1 = "~O~O~O~O P"
ex2 = "P O~ O~ ~O O~"
ex3 = "~O~O~O~OP~O~OO~"
print(count_deaf_rats(ex1))
print(count_deaf_rats(ex2))
print(count_deaf_rats(ex3))
# print(len(ex1))

# print(ex1.split('~'))
