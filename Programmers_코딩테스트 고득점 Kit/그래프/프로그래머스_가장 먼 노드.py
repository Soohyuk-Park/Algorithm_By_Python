from collections import deque

def solution(n, edge):# n은 노드의 개수 edge는 연결관계를 나타낸다.
    route = [0] * (n + 1) # 그 길까지 최단거리를 나타내는 거리 배열
    graph = [[] for _ in range(n + 1)] #여기엔 항상 그랬듯이 연결관계를 나타내고
    #edge.sort()  #이거는 다른분 풀이에서 정렬 해놨던데, 안해도 상관없어보여서 주석처리하고 돌렸더니 역시 잘 돌아간다. 이게 필요한 경우가 있나? 어차피 지나온거는 안보는데
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0]) #이런식으로 추가해주면 좋고
    queue = deque()
    queue.append(1) #시작점이 1이니까~
    route[1] = 1

    while queue:
        now = queue.popleft() # 하나씩 빼면서 가봅시다. 디큐에서 하나씩 빼는 이 아이디어가 dfs관련 문제에도 많이 쓰이는듯??
        for a in (graph[now]):
            if (route[a] == 0): #이미 지나온 길이라면 안볼겁니다!why? 최단거리가 아닐거니까!
                queue.append(a)
                route[a] = route[now] + 1

    Target = max(route) #자~ 이제 본격적으로 어디가 제일 먼 곳인지 확인 ㄱㄱ
    answer = 0 #일단 답은 0으로 세팅해주시고
    for r in range(n + 1):
        if route[r] == Target:
            answer += 1 # 제일 먼 Target과 같은게 발견될때마다 하나씩 플러스~
    return answer
