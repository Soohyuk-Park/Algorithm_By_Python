#https://www.acmicpc.net/problem/21610
#기존 구름이 있는데, 처음에 나는 이동한 좌표를 new_cloud라는 새로운 덱에 저장했다.
# 그러니까 시간초과가 떴고 뭔가 잘못돼서 줄여야함을 느꼈다.
# 그래서 다른 코드를 조금 참고해서, new_cloud를 없애고
# 구름에서 하나씩 빼면서 그게 이동한 좌표를 new_cloud로 넣어줬더니 해결됐다.

import sys
input = sys.stdin.readline

from collections import deque
n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
D = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

cloud = deque()

def move(cloud,d,s):
    for _ in range(len(cloud)):
        x,y = cloud.popleft()
        x_n, y_n = (x+D[d-1][0]*s)% n, (y+D[d-1][1]*s)%n
        cloud.append((x_n,y_n))
        visited[x_n][y_n] = True
    return cloud

def copy(new_cloud):
    F = [(-1,-1),(1,1),(-1,1),(1,-1)]
    for i in new_cloud:
        cnt = 0
        x,y = i[0],i[1]
        for j in F:
            x_n,y_n = x+j[0],y+j[1]
            if(0<=x_n<n and 0<=y_n<n and L[x_n][y_n]!=0 ):
                cnt += 1
        L[x][y] += cnt
    return

cloud = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

for i in range(m):
    visited = [[False] * n for _ in range(n)]
    d,s = map(int,input().split())
    cloud = move(cloud,d,s)
    for i in cloud:
        L[i[0]][i[1]] += 1
    copy(cloud)
    cloud = deque()
    for i in range(n):
        for j in range(n):
            if( visited[i][j] == False and L[i][j] > 1):
                L[i][j] -=2
                cloud.append((i,j))

print(sum(sum(b) for b in L))