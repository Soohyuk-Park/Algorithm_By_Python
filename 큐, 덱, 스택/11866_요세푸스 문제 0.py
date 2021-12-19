# https://www.acmicpc.net/problem/11866
from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n + 1):
    q.append(i)

print("<", end='')
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    print(q.popleft(), end="")
    if q:
        print(", ", end="")

print(">")