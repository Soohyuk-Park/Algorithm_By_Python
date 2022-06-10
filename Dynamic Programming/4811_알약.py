def solution(n):
    sum = 0
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    print(dp)
    for i in range(1,n+1):
        dp[1][i] = i
    for i in range(2, n+1):
        for j in range(1, n+1):
            if(i > j):
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]
if __name__ == '__main__':
    while(1):
        n = int(input())
        if( n == 0 ):
            break
        else:
            print(solution(n))