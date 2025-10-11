import sys
from collections import defaultdict
import copy
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
edges = []

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edges.append((u, v))


def dfs(v, visited, graph):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, visited, graph)


def is_cut_vertex(graph, k):
    visited = [False] * (N + 1)
    visited[k] = True

    # k와 연결된 간선 제거
    for key in list(graph.keys()):
        if k in graph[key]:
            graph[key].remove(k)
    if k in graph:
        del graph[k]

    # 시작점이 k면 다른 노드에서 시작
    start = 1 if k != 1 else 2
    dfs(start, visited, graph)

    # 하나라도 방문 안 됐으면 단절점
    for i in range(1, N + 1):
        if not visited[i]:
            print("yes")
            return
    print("no")


def is_bridge(graph, k):
    visited = [False] * (N + 1)
    u, v = edges[k]

    # 간선 제거
    graph[u].remove(v)
    graph[v].remove(u)

    start = 1 if u != 1 else v
    dfs(start, visited, graph)

    for i in range(1, N + 1):
        if not visited[i]:
            print("yes")
            return
    print("no")


q = int(input())
for _ in range(q):
    graph_copy = copy.deepcopy(graph)
    t, k = map(int, input().split())
    if t == 1:
        is_cut_vertex(graph_copy, k)
    else:
        is_bridge(graph_copy, k)
