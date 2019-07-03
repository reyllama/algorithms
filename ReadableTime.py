def make_readable(seconds):
    hour = str(int(seconds/3600)).zfill(2)
    minute = str(int((seconds % 3600)/60)).zfill(2)
    second = str(seconds %  60).zfill(2)
    return "{0}:{1}:{2}".format(hour, minute, second)
