from collections import deque

n, m=map(int, input().split())
k=101
g=[*range(k)]
dist=[-1]*k

for i in range(n+m) :
    x, y=map(int, input().split())
    g[x]=y

q=deque()
dist[1]=0
q.append(1)
while q :
    x=q.popleft() ## 처음엔 q = { 1 } 인 상태이다.
    for i in range(1, 7) :
        y=x+i # 처음에 여기서 2,3~ 7까지 돌게될텐데
        if(y>100) :
            continue
        y=g[y]## 사다리가 있다면 올라가줍시다.(내려갈수도 있고)
        if(dist[y]==-1 or dist[y]>dist[x]+1) :## 방문한적이 없거나, 최단거리가 아니었다면 갱신!
            dist[y]=dist[x]+1
            q.append(y)# 그 점을 추가해서 다시 위의 과정을 반복~

print(dist[-1])