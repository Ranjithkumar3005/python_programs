def check(N, K):
    return 2 * N * K - (2 * K * (K + 1) - K)


T = int(input())
for i in range(T):
    L, R = map(int, input().split())
    check(L, R)
