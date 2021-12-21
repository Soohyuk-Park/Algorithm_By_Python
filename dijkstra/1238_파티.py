# https://www.acmicpc.net/problem/1238

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
a,b,c = map(int,input().split())
graph = [[] for _ in range(a+1)]

for i in range(b):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    visited = [False] * (a + 1)
    distance = [INF] * (a + 1)
    visited[start]=True
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w,p = heapq.heappop(q)
        visited[p] = True
        for i in graph[p]:
            wei = w + i[1]
            if( distance[i[0]] > wei):
                distance[i[0]] = wei
                heapq.heappush(q, (wei,i[0]))
    return distance

max = -2
for i in range(1, a+1 ):
    if( i != c):
        if(dijkstra(c)[i] + dijkstra(i)[c] > max ):
            max = dijkstra(c)[i] +  dijkstra(i)[c]

print(max)
