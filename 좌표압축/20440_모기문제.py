import sys
import collections

input = sys.stdin.readline

n = int(input())

mosq = collections.defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    mosq[x] += 1
    mosq[y] -= 1

print(mosq)

coors = list(mosq.keys())
coors.sort()

print(coors)

result = []
total = 0
for i in coors:
    total += mosq[i]
    result.append(total)

max_num = max(result)

start = result.index(max_num)
end = start
while end < len(result) and result[end] == max_num:
    end += 1

print(max_num)
print(coors[start], coors[end])