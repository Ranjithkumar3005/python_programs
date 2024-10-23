# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
val = list(map(int, input().split(" ")))
dum = sorted(val)
arr = []
while val != []:
    max1 = max(val)
    idx = dum.index(max1)
    idx1 = val.index(max1)
    if idx != idx1:
        if idx1 != 0:
            val = val[: idx1 + 1][::-1] + val[idx1:]
            arr.append(idx1 + 1)
        val = val[::-1]
        arr.append(idx + 1)
    val.remove(max1)
print(" ".join(map(str, arr)))
