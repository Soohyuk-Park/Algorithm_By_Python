import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
D = [(1,0),(-1,0),(0,1),(0,-1)]
L = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if L[i][j] == 9:
            x,y = i,j

def biteFish(x,y,size):
    cur_x, cur_y = x,y
    visited = [[False]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    temp = []
    q = deque()
    q.append((cur_x,cur_y))
    visited[cur_x][cur_y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for i in D:
            new_x = cur_x + i[0]
            new_y = cur_y + i[1]
            if 0<= new_x < n and 0<= new_y < n and visited[new_x][new_y] == False:
                if L[new_x][new_y] <= size:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
                    distance[new_x][new_y] += distance[cur_x][cur_y] + 1
                    if L[new_x][new_y] < size and L[new_x][new_y] != 0:
                        temp.append((new_x,new_y,distance[new_x][new_y]))
    return sorted(temp, key=lambda x : (-x[2],-x[0],-x[1] ))

size = 2
result = 0
cnt = 0
while 1:
    shark = biteFish(x,y,size)
    if len(shark) == 0:
        print(result)
        break
    n_x,n_y,dist = shark.pop()
    result += dist
    cnt += 1
    L[n_x][n_y], L[x][y] = 0,0
    x,y=n_x,n_y
    if cnt == size:
        size+=1
        cnt = 0




