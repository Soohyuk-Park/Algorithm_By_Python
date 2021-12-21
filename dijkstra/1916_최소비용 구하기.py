# https://www.acmicpc.net/problem/1916

import heapq
import sys
N = int(input())
M = int(input())
INF = sys.maxsize
graph =[[] for _ in range(N+1)]
visited = [False] *( N+1)
q = []
distance = [INF] * (N+1)
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        cost, p = heapq.heappop(q)
        if( visited[p] == False):
           visited[p] = True
           for i in graph[p]:
              A = cost + i[1]
              if( distance[i[0]] > A):
                  distance[i[0]] = A
                  heapq.heappush(q, (A,i[0]))
    return distance
v, w = map(int,input().split())
print(dijkstra(v)[w])