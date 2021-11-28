n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(graph, v):
    for i in graph[v]:
        if(visited[i] == False):
         visited[i] = True
         dfs(graph, i)

dfs(graph, 1)

print(visited)
print(visited.count(True)-1)