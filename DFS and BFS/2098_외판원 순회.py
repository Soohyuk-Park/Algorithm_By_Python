# https://www.acmicpc.net/problem/2098 #

# 너무 어려운 문제였다. dfs,bfs에 꽂혀서 요즘 열심히 푸는 중인데.
# 이거도 시도해보다가 뭔가 아니라는 사실을 깨달았다.
# 비트마스킹을 사용하는 문제들이 아직은 좀 낯설고 까다롭게 느껴지는 것 같다.
# 확실히 문제의 아이디어는 엄청 좋고, 신선하면서 재밌다.
# dfs로 탐색을 하면서 그 와중에 visited로 방문여부를 체크하고
# 그러면서 Min을 통해서 최소값을 계속 받아내야하는
# 정말 종합선물세트같은 골드1 문제였다.
# 혼자 푸는데는 좀 한계가 있어서 # https://hongcoding.tistory.com/83 # 를 참고해서 공부했다.
# DFS,BFS에 좀 더 익숙해지기 위해서 노력하자
# 어제 카카오_네트워크 문제는 잘 풀려서 좋았는데 역시 문제의 난이도 상승은 끝이 없구나 싶다.

n = int(input())

INF = int(1e9)
dp = [[INF] * ( 1 << n ) for _ in range(n)]

def dfs( x, visited):
  if visited == (1 << n) -1:
    if graph[x][0]:
      return graph[x][0]
    else:
      return INF

  if dp[x][visited] != INF:
    return dp[x][visited]

  for i in range(1,n):
    if not graph[x][i]:
      continue
    if visited & (1 << i):
      continue

    dp[x][visited] = min(dp[x][visited] , dfs(i, visited | (1<<i)) + graph[x][i])
  return dp[x][visited]

graph = []

graph = [list(map(int, input().split())) for _ in range(n)]

print(dfs(0,1))