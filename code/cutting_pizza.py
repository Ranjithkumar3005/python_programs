import math


def gcd_multiple(numbers):
    g = numbers[0]
    for num in numbers[1:]:
        g = math.gcd(g, num)
    return g


def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        angles = list(map(int, input().split()))

        differences = []
        for i in range(1, n):
            differences.append(angles[i] - angles[i - 1])
        differences.append(360 - angles[-1] + angles[0])
        g = gcd_multiple(differences)

        total_slices = 360 // g

        additional_cuts = total_slices - n

        print(additional_cuts)


solve()
