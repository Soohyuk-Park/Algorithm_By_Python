from collections import deque
from itertools import combinations
n,m = map(int,input().split())
realMap = [list(map(int,input().split())) for _ in range(n)]
D = [(-1,0),(1,0),(0,1),(0,-1)]
distMap = [[-1]*n for _ in range(n)]

def virusPos(L):
    temp = []
    for i in range(n):
        for j in range(n):
            if L[i][j] == 2:
                temp.append((i,j))
    return temp

def move(virusList, MAP, distMap, K):
    visited =[[False]*n for _ in range(n)]
    for pos in virusList:
        x = pos[0]
        y = pos[1]
        visited[x][y] = True
    while virusList:
            if len(virusList) == 0 or K == 0:
                if K == 0:
                    return getMax(distMap)
                else:
                    return -1
            v_pos = virusList.popleft()
            v_x, v_y = v_pos[0], v_pos[1]
            for dir in D:
                    n_x = v_x + dir[0]
                    n_y = v_y + dir[1]
                    if 0<= n_x < n and 0<= n_y < n and visited[n_x][n_y] == False:
                            visited[n_x][n_y] = True
                            if( MAP[n_x][n_y] == 0 and (distMap[n_x][n_y] == -1 or distMap[n_x][n_y] > distMap[v_x][v_y] + 1)):
                                distMap[n_x][n_y] = distMap[v_x][v_y] + 1
                                K -= 1
                                virusList.append((n_x,n_y))
                            elif ( MAP[n_x][n_y] == 2 and (distMap[n_x][n_y] == -1 or distMap[n_x][n_y] > distMap[v_x][v_y] + 1)):
                                distMap[n_x][n_y] = distMap[v_x][v_y] + 1
                                virusList.append((n_x,n_y))
                            elif MAP[n_x][n_y] == 1:
                                continue
                            else:
                                continue
    if not checker(distMap,MAP):
                return -1
    else:
        return

def getMax(mylist):
    nowMax = -3
    N = len(mylist)
    for i in range(N):
        for j in range(N):
            nowMax = max(nowMax, mylist[i][j])
    return nowMax

def checker(mylist, MAP):
    N = len(mylist)
    for i in range(N):
        for j in range(N):
            if mylist[i][j] == -1 and MAP[i][j] == 0:
                return False
    return True


temp = virusPos(realMap)
tempVirusList = combinations(temp,m)
answer = 1e9
AA = False
for i in range(n):
    for j in range(n):
        if realMap[i][j] == 0:
            AA = True
if not AA:
    print(0)
    exit(0)
cnt = 0
for i in range(n):
    for j in range(n):
        if realMap[i][j] == 0:
            cnt+=1

for nowList in tempVirusList:
    K = cnt
    distMap = [[-1] * n for _ in range(n)]
    nowList = deque(nowList)
    T = move(nowList, realMap, distMap, K)
    if T!=-1 and answer > T:
        answer = T


if answer != 1e9:
    print(answer+1)
else:
    print(-1)
