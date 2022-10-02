# to use, change the n variable to the number of seconds to convert. The format of the result is hh:mm:ss.

def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

n = 23421
print(convert_seconds(n))
