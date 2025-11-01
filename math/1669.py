import math

x, y = map(int, input().split())
d = y - x

if d == 0:
    print(0)
else:
    n = int(math.isqrt(d))  # n = floor(sqrt(d))
    if d == n * n:
        print(2 * n - 1)
    elif d <= n * n + n:
        print(2 * n)
    else:
        print(2 * n + 1)
