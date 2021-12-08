## https://www.acmicpc.net/problem/1038 ##
### 말도 안되는 풀이.. 이런거 떠올릴수나 있을런지.. 이해하는것도 힘든데 ㅋㅋㅋ 진짜 천재들이 있기는하구나 ##
# L = set()
#
# def DFS(N,first) :
#     if first :
#         for i in range(10) :
#             L.add(i)
#             DFS(i,False)
#     else :
#         for i in range(N%10) :
#             NN = N*10+i
#             print(NN)
#             L.add(NN)
#             DFS(NN,False)
#
# DFS(0, True)

## comb와 정렬을 활용한 그나마 평범한 풀이.

import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()               # 모든 감소하는 수
for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순

try:
    print(nums[n])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)


# 무난하면서 정석적인 풀이가 이거인 것 같다.
# 위에 어려운 풀이랑 아이디어는 같은데 뭔가 많이 다른느낌?

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n = int(input())
# dp = [0] * 1000001
#
# if 0<= n <= 10:
#     print(n)
#     sys.exit()
# queue = deque()
# for i in range(11):
#     queue.append(i)
#     dp[i] = i
#
# cnt = 10
# while queue:
#     now = queue.popleft()
#     x = now % 10
#     for i in range(x):
#         dp[cnt] = now * 10 + i
#         queue.append(now * 10 + i)
#         cnt += 1
#
# if cnt >= n and dp[n] != 0:
#     print(dp[n])
# else:
#     print(-1)


####################################################
# Short 풀이 하나 추가 참고.

from itertools import combinations
target = int(input())
dicrease_num = []
for i in range(1,11):
    for comb in combinations(range(0,10),i):
        dicrease_num.append(int(''.join(map(str,sorted(comb,reverse=True)))))
dicrease_num.sort()
print(dicrease_num[target] if target<len(dicrease_num) else -1)
