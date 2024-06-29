n = int(input())
arr = map(int, input().split())
arr1=sorted(arr)
print(arr1)

for i in range(n-1,0,-1):
    if arr1[i]!=arr1[i-1]:
        print(arr1[i-1])
    