def race(v1, v2, g):
    if v1>=v2:
        return None
    else:
        duration = g/(v2-v1)
        hour = int(duration)
        minute = int(duration*60 % 60)
        second = int(duration*3600 % 60)
        return [hour, minute, second]
