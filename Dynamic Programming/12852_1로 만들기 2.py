# https://www.acmicpc.net/problem/12852

n = int(input())
dp = [[0, []] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = [1]
for i in range(2,n+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    if(dp[i//3][0] + 1 < dp[i][0] and i%3 ==0 ):
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
    if(dp[i//2][0] + 1 < dp[i][0] and i%2 ==0 ):
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
for i in dp[n][1][::-1]:
    print(i,end=' ')