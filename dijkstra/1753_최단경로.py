#https://www.acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
begin = int(input())
INF = sys.maxsize
visited = [False]*(n+1)
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    q = []
    distance[start]=0
    visited[start]=True
    heapq.heappush(q, (0, start))
    while q:
        w, c = heapq.heappop(q)
        for n_n, n_w in graph[c]:
            wei = n_w + w
            if( distance[n_n] > wei):
                distance[n_n] = wei
                heapq.heappush(q, [wei, n_n])
    return distance

L = dijkstra(begin)

for i in range(1,n+1):
    if(L[i] == INF ):
        print("INF")
    else:
        print(L[i])
