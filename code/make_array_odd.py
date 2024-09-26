# cook your dish here
def check(val, R):
    eve = 0
    odd = 0
    for i in val:
        if i % 2 == 0:
            eve += 1
        else:
            odd += 1
    if R % 2 == 0:
        if odd > 0:
            print(eve)
        else:
            print(-1)
    else:
        val1 = eve // 2
        if eve % 2 != 0:
            print(val1 + 1)
        else:
            print(val1)


T = int(input())
for i in range(T):
    L, R = map(int, input().split())
    val = list(map(int, input().split()))
    check(val, R)
