import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sum_gcd(num_list):
    sum=0
    n= num_list[0]
    numbers=num_list[1:]
    for i in range(n):
        for j in range(i + 1, n):
            sum += gcd(numbers[i], numbers[j])

    return sum


t=int(input())

for _ in range(t):
    num_list=list(map(int,input().split()))
    print(sum_gcd(num_list))

