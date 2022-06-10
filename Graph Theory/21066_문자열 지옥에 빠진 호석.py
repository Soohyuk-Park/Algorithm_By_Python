import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


def dfs(x,y,st):
    if st:
        total[st] += 1
    if len(st) == 5:
        return

    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M
        dfs(nx,ny,st+arr[nx][ny])

N,M,K = map(int,input().split())

total = defaultdict(int)

arr = [list(input()) for _ in range(N)]
dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,-1,0,1,1,-1,1,-1]

for x in range(N):
    for y in range(M):
        dfs(x,y,arr[x][y])


for _ in range(K):
    print(total[input()])