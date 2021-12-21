# https://www.acmicpc.net/problem/1912

n = int(input())
L = list(map(int,input().split()))

dp = [0] * n
dp[0] = L[0]

for i in range(1,n):
    dp[i] = max( dp[i-1] + L[i], L[i])

print(max(dp))
