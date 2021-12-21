# https://www.acmicpc.net/problem/14502
# Deepcopy를 안써서, 처음에 리스트가 For문 돌면서 초기화가 안되더라.
# 그러다보니 자연스레 모든 0이 1로 채워지고. 답은 계속 0만 나오고.
# 그래서 처음엔 아래 코드처럼 매번 그래프를 작성하면서 했는데
# deepcopy를 사용하면 아래와 같은 문제 없이 해결가능!

from itertools import combinations

r , c = map(int,input().split())
graph =[]
for i in range(r):
    graph.append(list(map(int,input().split())))

onebon = [[0]*c for _ in range(r)]


def attack(graph):
    virus_point = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if( graph[i][j] == 2):
                virus_point.append((i,j))
    D = [(-1,0), (1,0), (0,1),(0,-1)]
    while virus_point:
      x,y = virus_point.pop()
      for i in D:
        x_n = x + i[0]
        y_n = y + i[1]
        if( 0<= x_n < len(graph) and 0<= y_n < len(graph[1]) ):
            if( graph[x_n][y_n] == 0):
                graph[x_n][y_n] = 2
                virus_point.append((x_n,y_n))
    answer = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if( graph[i][j] == 0):
                answer += 1
    return answer

zero_point = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if (graph[i][j] == 0):
            zero_point.append((i,j))

temp = list(combinations(zero_point,3))

# print(((0,1),(1,0),(3,5)) in temp)
# Q = ((0,1),(1,0),(3,5))
# graph = onebon
# graph[Q[0][0]][Q[0][1]] = 1
# graph[Q[1][0]][Q[1][1]] = 1
# graph[Q[2][0]][Q[2][1]] = 1
# print(attack(graph))

max = -1
for k in temp:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            onebon[i][j] = graph[i][j]
    onebon[k[0][0]][k[0][1]] = 1
    onebon[k[1][0]][k[1][1]] = 1
    onebon[k[2][0]][k[2][1]] = 1
    K = attack(onebon)
    if( K > max ):
        max = K
print(max)
