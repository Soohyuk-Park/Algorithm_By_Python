n = int(input())
m = int(input())
parent = [0] * (n+1)

def find(a):
    if parent[a] == a:
        return a
    else:
        p = find(parent[a])
        parent[a] = p
        return p

def union(a,b):
    if find(a) == find(b):
        return
    elif find(a) < find(b):
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)

graph = []

for i in range(1,n+1):
    parent[i] = i

for _ in range(n):
    L = list(map(int,input().split()))
    graph.append(L)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1,j+1)

L = list(map(int,input().split()))
L.sort()
P = parent[L[0]]
for i in L:
    if parent[i] != P:
        print("NO")
        break
    elif i == L[-1] and parent[i] == P:
        print("YES")
        break

