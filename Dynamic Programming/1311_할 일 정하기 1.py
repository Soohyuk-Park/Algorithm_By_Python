## https://www.acmicpc.net/problem/1311 ##
# 문제의 아이디어는 001이면 1번사람이 3번일을 한 상태. 즉 graph_ i,j 는 i인 사람이 j인 일을 했다는 뜻이다.
# 한 사람은 일 하나만 해야하고..이런 느낌으로 가면 001 -> 101 --> 111 처럼 할 수 있고 비슷하게 하면 된다.
#비트카운팅 기법이 좀 낯설긴한데 연습 복습 공부!

graph = {}

def bit_counting(x): # 1의 개수를 세는 함수
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
for i in range(1<<n): # for문을 도는데 처음엔 001 / 그리고 010 그리고 100 순으로 돌게 된다.
    k = bit_counting(i)
    for j in range(n): # j를 통해서 이게 i하고 비교해서 겹치는게 없어야 한다.
        if not i & (1 << j):
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i]+graph[k][j]) #그러면 겹치는게 없으니 하나라도 1인 부분들이 합쳐진다.
                # 합쳐지는 부분의 값은 케이스중에 큰걸로. 복습 철저히 !
print(dp[-1])