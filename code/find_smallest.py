def find_smallest_n(L,R):
        for N in range(R, L-1, -1): 
            valid = True
            for i in range(L, R):
                if N % i <= N % (i+1):
                    valid = False
                    break
            if valid:
                print(N)
                return
        print(-1)
        


T = int(input())
for i in range(T):
    L, R = map(int, input().split())
    find_smallest_n(L,R)

