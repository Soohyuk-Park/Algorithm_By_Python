# https://www.acmicpc.net/problem/13305
N = int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))
maxi = -2
dp = [0]*(N)
dp[1] = city[0]*distance[0]
yesterday = city[0]
for i in range(2,N):
    dp[i] = min(dp[i-1] + yesterday*distance[i-1], dp[i-1] + city[i-1]*distance[i-1])
    if( dp[i] == dp[i-1] + city[i-1]*distance[i-1]):
        yesterday = city[i-1]
print(dp[N-1])