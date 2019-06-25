def solution(roman):
    m = roman.count('M')
    d = roman.count('D')
    c = roman.count('C')
    l = roman.count('L')
    x = roman.count('X')
    v = roman.count('V')
    i = roman.count('I')
    num = 1000*m + 500*d + 100*c + 50*l + 10*x + 5*v + i
    if 'CM' in roman:
        num -= 200
    if 'CD' in roman:
        num -= 200
    if 'XC' in roman:
        num -= 20
    if 'XL' in roman:
        num -= 20
    if 'IX' in roman:
        num -= 2
    if 'IV' in roman:
        num -= 2
    return num
