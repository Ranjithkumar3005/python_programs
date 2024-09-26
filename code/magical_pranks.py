# cook your dish here
T = int(input())

for i in range(T):
    val = int(input())
    str1 = input()
    check = False
    if str1[0] == "B":
        check = True
    b = 0
    w = 0
    for j in range(0, len(str1)):
        if check and str1[j] == "B":
            b += 1
            check = False
        elif not check and str1[j] == "W":
            w += 1
            check = True
    print(min(b, w))
