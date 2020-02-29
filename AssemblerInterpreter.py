def simple_assembler(program):
    for line in program.splitlines():
        items = line.split()
        if items[0] == 'mov':
            items[1] = items[2]
        elif items[0] == 'inc':
            items[1] += 1
        elif items[0] == 'dec':
            items[1] -= 1

    return {}

def simple_assembler(program):
    ans = dict()
    lines = program.splitlines()
    for i in range(len(lines)):
        print(i)
        print(ans)
        items = lines[i].split()
        if items[0] == 'mov':
            ans[items[1]] = int(items[2])
            # items[1] = items[2]
        elif items[0] == 'inc':
            ans[items[1]] += 1
            # items[1] += 1
        elif items[0] == 'dec':
            ans[items[1]] -= 1
            # items[1] -= 1
        else:
            if ans[items[1]]  == 0:
                continue
            else:
                i = i - int(items[2]) -1
    return ans

def simple_assembler(program):
    ans = dict()
    i = 0
    while True:
        i += 1
        print(i)
        print(ans)
        if i > len(program):
            break
        items = program[i-1].split()
        if items[0] == 'mov':
            ans[items[1]] = items[2]
            ans[items[1]] = int(ans[items[1]])
            # items[1] = items[2]
        elif items[0] == 'inc':
            ans[items[1]] += 1
            # items[1] += 1
        elif items[0] == 'dec':
            ans[items[1]] -= 1
            # items[1] -= 1
        else:
            if ans[items[1]]  == 0:
                continue
            else:
                i = i + int(items[2]) -1
    return ans


code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
print(simple_assembler(code))
