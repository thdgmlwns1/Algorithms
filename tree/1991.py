import sys
from collections import defaultdict
input=sys.stdin.readline


graph=defaultdict(list)

N=int(input())

for _ in range(N):
    root,left,right=input().split()
    graph[root].append(left)
    graph[root].append(right)


# 전위순회 (Root - Left - Right)
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

# 후위순회 (Left - Right - Root)
def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

# 중위순회 (Left - Root - Right)
def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

preorder('A')
print()
inorder('A')
print()
postorder('A')
