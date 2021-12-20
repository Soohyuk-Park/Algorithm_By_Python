# https://www.acmicpc.net/source/36465299
#기본적인 방법
def factorial(n):
    if( n == 1):
        return 1
    else:
        return n * factorial(n-1)

n,m = map(int,input().split())
answer = factorial(n) // ( factorial(m) * factorial( n- m))
print(answer)

# 다이나믹 프로그래밍. 조금 참신한 방법. 백준에서 'smk6221'님 풀이 참고.
n, m = map(int, input().split())

dp = [n for _ in range(m+1)]
print(dp)
dp[0] = 0

for i in range(1,m+1):
    if i == 1: continue
    dp[i] = (dp[i-1]*(n-i+1))//i

print(dp[m])