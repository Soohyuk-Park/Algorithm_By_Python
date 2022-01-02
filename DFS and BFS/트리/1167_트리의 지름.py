# https://www.acmicpc.net/problem/1167

import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    L = list(map(int,input().split()))
    for i in range(1, len(L)-2 , 2):
        graph[L[0]].append((L[i],L[i+1]))


def bfs(node):
    visited = [-1]*(n + 1)
    q = deque()
    q.append(node)
    visited[node] = 0
    F = [0, 0]
    while q:
        A = q.popleft()
        for x, y in graph[A]:
           if( visited[x] == -1):
               visited[x] = visited[A] + y
               q.append(x)
               if(F[0] < visited[x]):
                   F = visited[x], x
    return F


aa, bb = bfs(1) ##한쪽 방향으로 했다가, 반대로도 해주는 과정( 어느 방향이 최대인지 모름)
aa, bb = bfs(bb)
print(aa)
