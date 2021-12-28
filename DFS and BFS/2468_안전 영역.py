# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(10000)
n = int(input())
L = []
for i in range(n):
    L.append(list(map(int,input().split())))
def check(graph, height):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(graph[i][j] > height):
                visited[i][j] = True
    return visited

def virus(graph,x,y):
    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in D:
        x_n = x+i[0]
        y_n = y+i[1]
        if( 0<= x_n < n and 0<= y_n< n and graph[x_n][y_n] == True ):
            graph[x_n][y_n] = False
            virus(graph,x_n,y_n)
    return
answer = []
tmp = 0
maxi = -3
D = [(0,1),(0,-1),(1,0),(-1,0)]
for q in range(0, 101):
    V = check(L,q)
    for i in range(n):
        for j in range(n):
            if(V[i][j] == True):
                V[i][j] = False
                virus(V,i,j)
                tmp+=1
    maxi = max(tmp, maxi)
    tmp = 0
print(maxi)
