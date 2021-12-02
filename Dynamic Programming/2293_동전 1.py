# https://www.acmicpc.net/problem/2293 #

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

dp = [0 for i in range(m + 1)]
dp[0] = 1

# dp[N] 을 구하기 위해서는 dp[N - something] 의 값들을 다 합치면 된다.
# 여기서 something은 우리가 가지고 있는 동전 ( 즉 arr 의 원소들 )
# N-something 까지의 경우의 수가 dp[N - something]에 존재하고
# 나머지 - 부분은 그냥 더해버리면 해결 완료!

for i in arr:
    for j in range(1, m + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[m])