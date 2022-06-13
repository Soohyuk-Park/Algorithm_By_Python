n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1000000000] * m for _ in range(n)]
left = [[-1000000000] * m for _ in range(n)]
right= [[-1000000000] * m for _ in range(n)]
#1 첫줄작업
dp[0][0] = mat[0][0]
c = 0
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + mat[0][j]
    c += 1

for i in range(1, n):
    # 2 왼->오
    #2.1 left first
    left[i][0] = dp[i-1][0] + mat[i][0]
    for j in range(1, m):
        c += 1
        left[i][j] = max(dp[i-1][j]+mat[i][j], left[i][j-1]+mat[i][j])
    # 3 오 ->왼
    right[i][m-1] = dp[i-1][m-1] + mat[i][m-1]
    for j in range(m-2, -1, -1):
        right[i][j] = max(dp[i-1][j] + mat[i][j], right[i][j+1] + mat[i][j])
        c += 1
    #4 merge
    for j in range(m):
        dp[i][j] = max(right[i][j], left[i][j])
        c += 1
print(dp[n-1][m-1])


