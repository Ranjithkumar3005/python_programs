def nonRepeat(s):
    h = {}
    for i in s:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    for i in s:
        if h[i] == 1:
            return i
    return -1


print(nonRepeat("google"))
