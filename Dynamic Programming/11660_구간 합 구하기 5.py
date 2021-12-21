##  https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph= []
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + graph[i][j]

for i in range(m):
    answer = 0
    x_1,y_1,x_2,y_2 = map(int,input().split())
    print(dp[x_2][y_2] - dp[x_1-1][y_2] - dp[x_2][y_1-1] + dp[x_1-1][y_1-1])