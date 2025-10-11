import sys
input=sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000000)

N,P=map(int,input().split())
tree=defaultdict(list)

leaf=[]

for _ in range(N-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

visited=[False]*(N+1)

def dfs(v):
    visited[v]=True
    cut=0

    for i in tree[v]:
        if not visited[i]:
            dfs(i)
            cut=1

    if cut ==0:
        leaf.append(v)

dfs(1)

print(P/len(leaf))
    
