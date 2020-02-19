def dirReduc(arr):
    cnt = [arr.count(dir) for dir in sorted(set(arr))]
    return ['EAST']*(cnt[0]>cnt[3])*(cnt[0]-cnt[3])+['NORTH']*(cnt[1]>cnt[2])*(cnt[1]-cnt[2])+['SOUTH']*(cnt[2]>cnt[1])*(cnt[2]-cnt[1])+['WEST']*(cnt[3]>cnt[0])*(cnt[3]-cnt[0])


def dirReduc(arr):
    if len(arr) <= 1:
        return arr
    if (arr[0], arr[1]) in (("WEST", 'EAST'), ("NORTH", 'SOUTH'), ("EAST", "WEST"), ("SOUTH", "NORTH")):
        del arr[0], arr[1]
        return dirReduc(arr)
    else:
        return [arr[0]] + dirReduc(arr[1:])

def dirReduc(arr):
    if len(arr) <= 1:
        return arr
    i = 0
    while True:
        print(i, len(arr))
        print(arr)
        if i >= len(arr):
            break
        try:
            if arr[i]+arr[i+1] in ('SOUTHNORTH', 'NORTHSOUTH', 'EASTWEST', 'WESTEAST'):
                arr.remove(arr[i])
                arr.remove(arr[i])
        except:
            pass
        try:
            if arr[i]+arr[i-1] in ('SOUTHNORTH', 'NORTHSOUTH', 'EASTWEST', 'WESTEAST'):
                arr.remove(arr[i])
                arr.remove(arr[i-1])
        except:
            pass
        else:
            i += 1
    return arr

def dirReduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST':'EAST'}
    shortcut = []
    for dir in arr:
        if shortcut and shortcut[-1] == opposite[dir]:
            shortcut.pop()
        else:
            shortcut.append(dir)
    return shortcut


arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# arra = [word.upper() for word in arr]
print(dirReduc(arr))
