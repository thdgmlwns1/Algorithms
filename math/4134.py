import sys
import math
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

T = int(input())
out = []

for _ in range(T):
    n = int(input())
    while True:
        if is_prime(n):
            out.append(str(n))
            break
        n += 1

sys.stdout.write("\n".join(out))
