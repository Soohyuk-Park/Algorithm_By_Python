# https://www.acmicpc.net/problem/1005

import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    building = [0] + list(map(int,input().split()))
    graph = [[]*(N+1) for _ in range(N+1)]
    b_deg = [0]*(N+1)
    dp = [0]*(N+1)
    for i in range(K):
        x,y = map(int,input().split())
        graph[x].append(y)
        b_deg[y] += 1

    q = deque()
    for i in range(1,N+1):
        if(b_deg[i] == 0):
            q.append(i)
            dp[i] = building[i]

    while q:
        w = q.popleft()
        for k in graph[w]:
            b_deg[k] -= 1
            dp[k] = max( dp[w] + building[k] , dp[k] )
            if( b_deg[k] == 0):
                q.append(k)
    V = int(input())
    print(dp[V])