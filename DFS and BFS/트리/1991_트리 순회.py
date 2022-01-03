# https://www.acmicpc.net/problem/1991

from collections import deque
n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(1,n+1):
    L = list(map(ord,input().split()))
    arr[L[0]-64].append(L[1])
    arr[L[0]-64].append(L[2])

def dfs1(v):
    print(chr(v+64),end='')
    if(arr[v][0] != 46):
        dfs1(arr[v][0] - 64)
    if(arr[v][1] != 46):
        dfs1(arr[v][1] - 64)

def dfs2(v):
    if(arr[v][0] != 46):
        dfs2(arr[v][0] - 64)
    print(chr(v+64),end='')
    if(arr[v][1] != 46):
        dfs2(arr[v][1] - 64)

def dfs3(v):
    if(arr[v][0] != 46):
        dfs3(arr[v][0] - 64)
    if(arr[v][1] != 46):
        dfs3(arr[v][1] - 64)
    print(chr(v+64),end='')




dfs1(1)
print('')

dfs2(1)
print('')
dfs3(1)