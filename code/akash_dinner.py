def check_min_time(N, K, A, B):
    category_min_time = {}
    for i in range(N):
        category = A[i]
        time = B[i]
        if category in category_min_time:
            category_min_time[category] = min(category_min_time[category], time)
        else:
            category_min_time[category] = time

    if len(category_min_time) < K:
        return -1

    min_times = sorted(category_min_time.values())

    return sum(min_times[:K])


T = int(input())  # Number of test cases
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(check_min_time(N, K, A, B))
