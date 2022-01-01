# https://www.acmicpc.net/problem/11049
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
matrix = []
for i in range(N):
    x,y=map(int,input().split())
    matrix.append((x,y))
for i in range(N-1):
    arr[i][i+1] = matrix[i][0] * matrix[i][1]*matrix[i+1][1]
for i in range(2,N):
    for j in range(0,N-i):
        arr[j][j+i] = 2**32
        for k in range(j, j+i):
          arr[j][j+i] = min(arr[j][j+i], arr[j][k] +arr[k+1][j+i] +matrix[j][0] * matrix[k][1] * matrix[j+i][1])
print(arr[0][N-1])
