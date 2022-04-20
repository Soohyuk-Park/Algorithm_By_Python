import sys
input = sys.stdin.readline
length = int(input())

maze = list(map(int,input().split()))

dp = [[0 for _ in range(length)] for _ in range(length)]
dp[0][0] = 1
for i in range(length):
    for j in range(length):
        if( dp[i][j] != 0):
            for k in range(1,maze[j] + 1):
                if( j + k < length):
                  dp[i+1][j+k] = dp[i][j] + 1

min_value = 9999999
for i in range(length):
    if( dp[i][length-1] !=0 ):
        min_value = min( min_value, dp[i][length-1])

if( min_value == 9999999):
    print(-1)
else:
    print(min_value - 1)