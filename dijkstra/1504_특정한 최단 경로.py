#https://www.acmicpc.net/problem/1504

import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
INF = 80000001
visited = [False]*(n+1)
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
v, w = map(int,input().split())
def dijkstra(start):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    q = []
    distance[start]=0
    visited[start]=True
    heapq.heappush(q, (0, start))
    while q:
        x, y = heapq.heappop(q)
        for i in graph[y]:
            if( distance[i[0]] < x):
                continue
            elif( distance[i[0]] > distance[y] + i[1]):
                distance[i[0]] = distance[y] + i[1]
                heapq.heappush(q, (distance[i[0]],i[0]))
    return distance
one = dijkstra(1)[v] + dijkstra(v)[w] + dijkstra(w)[n]
two = dijkstra(1)[w] + dijkstra(w)[v] + dijkstra(v)[n]

if m == 0:
    print(-1)
else:
    result = min(one,two)
    print(result if result < INF else -1)