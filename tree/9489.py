import sys
input=sys.stdin.readline
from collections import defaultdict


while True:
    n,k=map(int,input().split())
    if [n,k]==[0,0]:
        break

    node=list(map(int,input().split()))
    parent=defaultdict(int)#노드별 부모를 저장

    index=0 #node 리스트에 부모가 되는 인덱스
    for i in range(1,n):
        parent[node[i]]=node[index]
        if i<n-1 and node[i]+1<node[i+1]:
            index+=1

    count=0
    if parent[parent[k]]: # 부모의 부모가 존재한다면
        for Node in node:
            if (parent[parent[k]] == parent[parent[Node]]) and parent[Node]!=parent[k]:
                count+=1
    print(count)