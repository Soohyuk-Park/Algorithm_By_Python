# https://www.acmicpc.net/problem/2961 #
# combinations를 쓰는 방식에 대해 연습할 수 있었다
# 근데 이거 안쓰고 푸는 방법을 생각해봐도 좋을 것 같다.
# 그리고 찾았다..
# 백준 아이디 'iknoom1107'를 쓰시는 분의 풀이를 보게 되었다.

#####################################
# N = int(input())
# arr = [tuple(map(int, input().split())) for _ in range(N)]
# answer = float('inf')
# for i in range(1, 1 << N):
#     a = 1
#     b = 0
#     for j in range(N):# comb랑 개념은 같지만 이런식으로 사용한게 거의 예술이다.
#         if i & (1 << j):
#             a *= arr[j][0]
#             b += arr[j][1]
#     answer = min(answer, abs(a - b))
# print(answer)
#############################################애초에 문제 카테고리도 비트마스크라 이게 출제자의 의도가 맞는 것 같다.

from itertools import combinations

n = int(input())
answer = 1e9
L = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n+1):
    total = list(combinations(L, i))

    for a in total:
        s = 1
        b = 0
        for x,y in a:
            s *= x
            b += y
        answer = min(answer , abs(s - b))
print(answer)