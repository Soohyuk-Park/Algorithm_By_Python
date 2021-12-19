# https://www.acmicpc.net/problem/20551
# 그냥 탐색을 하면 안되고  뭔가의 방법이 필요했던 문제
# 처음으로 찾은 풀이는 이분탐색이었는데
# 지금 밑에 있는 풀이는 블로그에서 찾은 풀이이다.
# 처음으로 등장한 어떤 숫자에 대해 그 곳의 인덱스를 dict형태로 저장한다.

import sys
input = sys.stdin.readline

a_idx = {}
N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])
for i in range(N):
    if A[i] not in a_idx:
        a_idx[A[i]] = i
D = [int(input()) for _ in range(M)]
for num in D:
    if num in a_idx:
        print(a_idx[num])
    else:
        print(-1)


### 아래는 이분탐색 풀이 ##
# https://www.acmicpc.net/problem/20551
def lower_bound(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            if right == mid:
                break
            right = mid
    if nums[mid] == target:
        return mid
    else:
        return -1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

for i in range(m):
    z = int(input())
    print(lower_bound(a, z))