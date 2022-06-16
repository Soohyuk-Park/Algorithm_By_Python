import math

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n + 1)]

stars = []
edges = []
result = 0

for i in range(n):
    x, y, z = map(int, input().split())
    stars.append((x, y, z, i))

for i in range(3):
        stars.sort(key=lambda x:x[i])
        print(stars)
        for j in range(1, n):
            edges.append((abs(stars[j - 1][i] - stars[j][i]), stars[j - 1][3], stars[j][3]))
        print(edges)



edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost

print(int(result))