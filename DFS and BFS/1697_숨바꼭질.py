#https://www.acmicpc.net/problem/1697#

from collections import deque

def dfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft() #일단 시작하는거 뽑아서
        if x == k: #뽑은게 도착점이랑 같으면 프린트 해주면 되겠지요.
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2): # 그거 기준으로 갈 수 있으면 1씩 더해줍시다.
            if 0<= nx <= MAX and not dist[nx]: # not dist를 통해서 Dist가 0인 경우만 탐색하게 한다.
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10 ** 5
dist = [0] *(MAX + 1)
n, k = map(int, input().split())

dfs()