#https://www.acmicpc.net/problem/3665


import sys
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    degree = [0]*(N+1)
    ranking = list(map(int,input().split()))
    tree = [[] for _ in range(N+1)]
    q = deque()
    for i in range(N-1):
        for j in range(i+1,N):
            tree[ranking[i]].append(ranking[j])
            degree[ranking[j]] += 1
    m = int(input())
    for i in range(m):
        x,y = map(int,input().split())
        check = True
        for i in tree[x]:
          if( i == y):
             tree[x].remove(y)
             tree[y].append(x)
             degree[y] -=1
             degree[x] +=1
             check = False
        if check:
            tree[y].remove(x)
            tree[x].append(y)
            degree[x] -= 1
            degree[y] += 1
    result = 0
    result_list = []

    for i in range(1,N+1):
        if(degree[i] == 0):
            q.append(i)

    if not q:
        result = 1
    while q:
        if len(q) > 1:
            result = 1
            break
        a = q.popleft()
        result_list.append(a)
        for i in tree[a]:
            degree[i] -=1
            if degree[i] == 0:
                q.append(i)
            elif degree[i] < 0:
                result = 1
                break
    if result > 0 or len(result_list) < N:
        print("IMPOSSIBLE")
    else:
        print(*result_list)
