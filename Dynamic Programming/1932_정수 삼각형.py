## https://www.acmicpc.net/problem/1932
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

if( n == 1 ):
    print(arr[0][0])
else:
   dp = [[0]*n for _ in range(n)]
   dp[0][0] = arr[0][0]
   dp[1][0] = dp[0][0] + arr[1][0]
   dp[1][1] = dp[0][0] + arr[1][1]

   c = 2
   for i in range(2,n):
      for j in range(c+1):
        if( j == 0):
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif( j == c):
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]
      c += 1

   print(max(dp[n - 1]))
