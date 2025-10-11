import sys
input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))
result = [[] for _ in range(N)]

def find(left, right,depth):
    if depth == N:
        return
    if left > right:
        return
    mid = (left + right) // 2
    result[depth].append(tree[mid])
    find(left, mid - 1,depth+1)
    find(mid + 1, right,depth+1)

find(0, len(tree) - 1,0)


for level in result:
    print(*level)