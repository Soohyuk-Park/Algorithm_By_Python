from collections import deque


def dfs(graph, v, visited):  # DFS알고리즘에 대한 함수를 정의할것이다.

    visited[v] = True  # 이 부분은 그래프의 특정한 부분이 이미 방문되었는지 체크할 용도로 사용할것.
    # visited는 모든 원소가 False로 초기화되어있으므로, 방문하는 순간 True가 된다 ( True <=> 방문 )
    print(v, end=' ')  # 방문했다면, 출력을 해주게 된다.
    for i in graph[v]:  # graph[v]는 v라는 숫자의 노드와 간선으로 연결된 노드들이 모여있는 리스트이다.
        if not visited[i]:  # v를 봤으니, 그것과 연결된 것들을 방문할 예정인데, 그게 방문을 안했다면 not visited[i] == 1 이 된다.
            dfs(graph, i, visited)  # 위의 과정이 새로운 연결된 점들에 계속해서 반복된다.
            # 최초에 시작하는 dfs의 v라는 노드로부터 시작해서, 쭉쭉 들어가면서 탐색이 진행된다.
            # 그러다가 탐색이 끝나면 다시 처음의 v로 돌아와서 탐색이 시작된다. 이러한 이유로 '깊이'를 우선으로 한 탐색방법이다.


def bfs(graph, start, visited):
    queue = deque([start])  # queue 에는 시작점이 들어있다.
    visited[start] = True  # visited의 경우 dfs와 똑같은 역할을 한다.
    while queue:  # queue가 빌때까지 계속되는 while문. 이 부분이 BFS알고리즘의 핵심
        v = queue.popleft()  # 처음엔 queue에 시작점만 들어있으니 그걸 v로 Popleft해준다.
        print(v, end=' ')  # dfs처럼 일단 시작점 출력하고서 출발~
        for i in graph[v]:  # 아까는 dfs문 안의 For문에 새로운 점에 의한 dfs가 또 있었는데 이번에는 좀 다르다.
            if not visited[
                i]:  # graph[시작점]에 모든 점들에 대해서 일단 탐색을 진행한다. 방문한적 없으면 그 점을 queue에 추가하고. visited[방문한 점의 index] =1로 해준다.
                queue.append(i)  # 이런 과정후에 queue는 시작점이 사라졌지만 그거하고 간선 1개만큼 떨어진 점들로 이루어져있다.
                visited[i] = True  # deque이므로 이러한 점들이 차례차례 가면서, 또 자신과 연결된 점들을 출력하게 도와준다.


n, m, start = map(int, input().split())  # 두개의 숫자를 입력받는다. n은 노드의 개수, m은 간선의 개수이다.

graph = [[] for _ in range(n + 1)]  # 그래프의 연결관계를 나타내는 2차원 리스트.

for i in range(m):
    a, b = map(int,
               input().split())  # 2하고 4가 연결되어있다면 그 의미를, graph[2] 라는 리스트에 4를 추가하고 graph[4]라는 리스트에 2를 추가하는 식으로 한다. 쌍방향 연결이므로.
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()  # 각 그래프의 요소들은 나중에 편하도록 정렬해두자.

visited = [False] * (n + 1)
dfs(graph, start, visited)
print('')

visited = [False] * (n + 1)
bfs(graph, start, visited)
