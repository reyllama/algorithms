def bears(x,s):
    tem = []
    i = 0
    while i < len(s)-1:
        if s[i] == 'B':
            if s[i+1] == '8':
                tem.append(s[i: i+2])
                i += 2
            else:
                i += 1
        elif s[i] == '8':
            if s[i+1] == 'B':
                tem.append(s[i:i+2])
                i += 2
            else:
                i += 1
        else:
            i += 1

    return ["".join(tem), len(tem) == x]
    #your code here




print(bears(3, '88Bifk8hB8BB8BBBB888chl8BhBfd'))
# x = '88Bifk8hB8BB8BBBB888chl8BhBfd'
# print(x[27:29])
