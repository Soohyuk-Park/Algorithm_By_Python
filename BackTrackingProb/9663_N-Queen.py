# https://www.acmicpc.net/problem/9663
# 어려운 문제라 구글링해서 열심히 그림그리고 손으로 풀면서 이해했다.
# 전형적인 백트랙킹 문제라는데 아직 너무 낯설어서 잘 못푼것같다.
# 이번주는 백트래킹 달리자
# 그래프 + 백트래킹 위주로 열심히 풀어봅시다.
# https://rebas.kr/761 : 풀이 출처
n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)