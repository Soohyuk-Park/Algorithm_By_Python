# https://www.acmicpc.net/problem/11659 #

# 그냥 input으로 하니까 시간초과떠서 readline으로 바꿨다.
# 처음에 또 For문 두개 돌리다가 하나로 줄였는데, 그래도 input이면 시간초과라니.. 코드가 잘못된건지 Input이 이상한건지
# 그래도 이제 이정도 문제는 어느정도 쉽다고 느끼는 것 같아서 다행

import sys
input = sys.stdin.readline

n,m =map(int,input().split())
L = list(map(int,input().split()))
sum = 0
Cum = [[0] for _ in range(n)]

for i in range(len(L)):
    sum += L[i]
    Cum[i] = sum

for _ in range(m):
    a,b = map(int, input().split())
    if( a== 1):
        print(Cum[b-1])
    else:
        print(Cum[b-1] - Cum[a-2])
