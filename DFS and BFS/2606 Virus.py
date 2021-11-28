n = int(input()) # 바이러스 문제이지만 노드와 간선 느낌으로 이해해도 ㅇㅋㅇㅋ. 그래프 문제 풀듯이 해봅시당!!
m = int(input())

graph = [[] for _ in range(n+1)] # 그래프 문제라 생각해서 그냥 배열도 그래프로 이름을 지어줬습니다.

for i in range(m):
    a, b = map(int, input().split()) # 그래프라면 역시 노드끼리 어떻게 연결되어있는지 알아야겠죠
    graph[a].append(b) #방향없는 그래프라서 그냥 2개의 노드가 연결되면 양방향으로 서로서로 연결을 표시해줍니다.
    graph[b].append(a)

visited = [False] * (n+1) #이거는 뭐 이제 워낙 익숙합니다. 특정 숫자에 방문했니? 라는 질문에 대한 답이 되겠죠

def dfs(graph, v): #이제는 친숙한 dfs함수. 방문하지 않았다면 방문한걸로 바꾸면서 그 위치를 True로 바꾸며 진행합니다.
    for i in graph[v]:
        if(visited[i] == False):
         visited[i] = True
         dfs(graph, i)

dfs(graph, 1)

#위 과정이 지나고 결과적으로 1번 컴퓨터가 몇 개의 다른 컴퓨터를 감염시켰는지 여부를 판단합니다.
#저의 코드에서는 1번 컴퓨터도 True이기 때문에 True의 개수에서 최초의 바이러스인 1번컴퓨터때문에 1을 빼주면 답이 됩니다~~ 아주 쉽고 재밌는 문제네요. 얼른 어려운 그래프 문제 ㄱㄱㄱㄱ
print(visited.count(True)-1)
