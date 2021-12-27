# https://www.acmicpc.net/problem/11724

n,m = map(int,input().split())
graph =[[] for _ in range(n+1)]
visited = [False] *(n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
tmp = 0
def dfs(x):
      visited[x] = True
      for i in graph[x]:
         if(visited[i] == False):
             visited[i] = True
             dfs(i)
      return

for i in range(1,n+1):
    if(visited[i] == False):
         dfs(i)
         tmp += 1

print(tmp)
