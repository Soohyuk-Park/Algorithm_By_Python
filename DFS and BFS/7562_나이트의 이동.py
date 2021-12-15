# https://www.acmicpc.net/problem/7562
# 16928 뱀과 사디리 문제하고 비슷한 풀이방식이 아래 코드
# 쭉쭉 탐색하는데, 방문한적이 없거나, 최단거리가 아니라면 지속적으로 갱신한다.

from collections import deque

t=int(input())
dx=[-2, -2, -1, -1, 1, 1, 2, 2]## 움직일 수 있는 좌표들 전부다 기록
dy=[-1, 1, -2, 2, -2, 2, -1, 1]

for i in range(t) :
    n=int(input())
    dist=[[-1]*n for _ in range(n)]
    x1, y1=map(int, input().split())
    x2, y2=map(int, input().split())
    dist[x1][y1]=0
    q=deque()
    q.append((x1, y1))
    while q:
        x, y=q.popleft()
        for i in range(8) :
            nx, ny=x+dx[i], y+dy[i]
            if(0<=nx<n and 0<=ny<n) :
                if(dist[nx][ny]==-1 or dist[nx][ny]>dist[x][y]+1) :
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx, ny))# 새로운 좌표는 q에 추가되기에 그 점을 기준으로 8방향 탐색을 다시 시작!
    print(dist[x2][y2])# 도착점에서의 값을 프린트 합시다.





## 다른분들 코드
import sys
from collections import deque

input = sys.stdin.readline

d = [(2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]

t = int(input())
for _ in range(t):
    n = int(input())
    kx, ky = map(int, input().split())
    ex, ey = map(int, input().split())
    visit = [[0] * n for _ in range(n)]
    visit[kx][ky] = 1
    q = deque([(kx, ky, 0)])
    while q:
        cx, cy, cost = q.popleft()
        if cx==ex and cy==ey:
            print(cost)
            break
        for dx, dy in d:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                q.append((nx, ny, cost+1))
                visit[nx][ny] = 1
                ## 비슷하지만 조금 다른느낌으로 cost를 함수로 설정해줬다.
                ## 방문한적이 있다면 안간다.( 또 가면 최단거리가 아닐테니까 )
                ## 개념은 똑같지만 이런 방식도 연습 ㄱㄱ 다양하게 할수록 머리 돌고 좋지지