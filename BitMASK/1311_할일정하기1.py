graph = {}

def bit_counting(x):
    answer = 0
    while x:
        answer += (x & 1)
        x >>= 1
    return answer

n = int(input())
dp = [1e9]*(1<<n)
for i in range(n):
    graph[i] = list(map(int,input().split()))

dp[0] = 0
for i in range(1<<n):## 현재 일의 상태
    k = bit_counting(i) ## 현재 일의 상태에서 일을 한 사람의 수
    for j in range(n): # 이번에 몇 번 일을 수행할것인지?
        if not i & (1 << j): # 현재 일의 상태하고/ 이번에 수행할 일을 & 연산하면 not이어야 함
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i]+graph[k][j])
            # 이 상태의 값은 ,     원래있던 값하고,  그 전의 일했던 값에서 새로운 일을 새로운 사람이 하는거

print(dp[-1])