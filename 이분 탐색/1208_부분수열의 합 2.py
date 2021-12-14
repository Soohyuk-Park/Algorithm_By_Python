# https://www.acmicpc.net/problem/1208
# 너무 어렵다. 이 코드도 너무 어렵다. 이해는 되는데 참 천재분들이 많다.
# 부분수열 1 문제가 너무 쉬워서 이것도 바로 풀어보려했다.
# 문제가 똑같은데? 라고 이상하게 생각하고 비슷하게 코드를 작성했더니 바로 시간초과
# 이 문제는 단순 해결보다 효율적인 코드 작성이 중요한 문제였다.
# defaultdict라는 도구를 처음 만났다. 아직 익숙하지는 않지만 잘 활용하기 위한 연습을 해두면 좋을 것 같다.

from sys import stdin
from collections import defaultdict #새로 배운 defaultdict


def dfs(idx, end_idx, subtotal, direction):
    global answer

    if idx == end_idx: # 끝부분 인덱스에 오기 전에는 그냥 쭉쭉 넘어가게되는 부분.
        if direction == "right":
            answer += left[s - subtotal]
        else:
            left[subtotal] += 1
        return

    dfs(idx + 1, end_idx, subtotal, direction) ## 그냥 인덱스가 넘어가는거 하나
    dfs(idx + 1, end_idx, subtotal + nums[idx], direction) ## 넘어갈때 subtotal에다가 인덱스의 값을 추가해주는거 하나.



answer = 0
n, s = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
left = defaultdict(int)



dfs(0, n//2, 0, "left") # 여기서 left라는 리스트를 채우게된다.
dfs(n//2, n, 0, "right") # 여기서 Right을 돌면서, s를 만들기 위한게 left에 있으면 그거의 개수를 answer에다가 추가해준다.
print(answer if s != 0 else answer - 1) # s가 0이 아니면 정답을 출력할건데, 만약 0이라면 -1을 해서 출력해준다!(기본으로 있는 0)