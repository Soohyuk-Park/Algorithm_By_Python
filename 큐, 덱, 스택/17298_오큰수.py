# https://www.acmicpc.net/problem/17298
# for문 두번으로해서 비교하려니까 실패
# 지금 방법은 일단 스택을 쭉쭉 채우는데, 스택 안에는 계속해서 인덱스가 들어있게됨.
# 저장된 인덱스에 대해서, 거기를 채워줄 값이 나오면 인덱스를 팝 시키면서 답안의 해당 인덱스를 그 큰 값으로 채우고 넘어감

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
answer = [-1]*len(L)
stack = [0]

for i in range(1,n):
    while stack and L[stack[-1]] < L[i]:
        answer[stack.pop()] = L[i]
    stack.append(i)

print(*answer)