# https://www.acmicpc.net/problem/2193

N = int(input())

dp = [[1,0],[0,1]]
for i in range(2,91):
    k = dp[i-1]
    dp.append([k[1],k[1]+k[0]])
print(sum(dp[N-1]))