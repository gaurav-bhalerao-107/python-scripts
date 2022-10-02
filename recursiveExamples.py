# Recursion Hell

def halvesEvensRecursive(newlist_1):
    if len(newlist_1) == 0:
        return newlist_1
    if newlist_1[0] % 2 == 0:
        newlist_1[0] = newlist_1[0] / 2
        return [int(newlist_1[0])] + halvesEvensRecursive(newlist_1[1:])
    return halvesEvensRecursive(newlist_1[1:])


#list_1 = [0, 2, 1, 7, 8, 56, 17, 18]

halvesEvensRecursive(list_1)
