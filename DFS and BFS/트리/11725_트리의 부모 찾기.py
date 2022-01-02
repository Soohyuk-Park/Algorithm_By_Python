# https://www.acmicpc.net/problem/11725
# 일단 내가 푼 첫번째 풀이
# 좀 복잡하게 풀어서 다른 분들 풀이를 참고하기로 했다.
# parents=[0]라는 배열을 만들어서 그거에 각각의 부모노드를 저장하는게 정성인듯
# 나도 결국 distance를 통해 해당 과정을 본거긴한데, 복잡하게 한듯싶다.

from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
distance = [1 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = deque()
q.append(1)
while q:
    x = q.popleft()
    if( visited[x] == False):
       visited[x] = True
       for i in graph[x]:
           if( visited[i] == False):
             distance[i] = distance[x] + 1
             q.append(i)

for i in range(2,n+1):
    for j in graph[i]:
        if( distance[j] == distance[i] - 1):
            print(j)
            break
