def check(n):
    if n % 2 != 0 or ((n / 2) % 2) != 0:
        print("NO")
        return
    arr1 = []
    arr2 = []
    check = True
    for i in range(1, ((n) // 2) + 1):
        if check:
            arr1.append(i)
            arr1.append(n - i)
            check = False
        else:
            arr2.append(i)
            arr2.append(n - i)
            check = True
    print("YES")
    print(arr1)
    print(arr2)


T = int(input())
for i in range(T):
    L = int(input)
    check(L)
