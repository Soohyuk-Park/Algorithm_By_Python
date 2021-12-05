# https://www.acmicpc.net/problem/2667 #
# 아이디어는 다 떠올렸는데 괜히 중간에 이상한 실수하다가 시간 날렸다..
# 항상 철저한 논리로 풀어야되는데, 의식의 흐름대로 하면 당연히 이렇게 꼬인다.
# dfs라는 함수가 어떻게 생겼는지 확실하게 기억해두자.
# 1이면 0으로 만드는게 기본이고. 거기서 상하좌우 탐색하면서 한 번 더 1을 0으로 만든다
# 나는 cnt라는 배열을 통해서, 한 번의 dfs실행시 변하는 1의 개수( 단지의 크기 ) 를 측정했다.
# 그러면 cnt라는 배열에 단지의 크기수만큼의 1이 들어온다. 그래서 cnt.count(1)로 리턴해주고
# 리턴하고 나서는 바로바로 다시 cnt = []라는 빈 리스트로 만들어주고.
# 어쨋든 재밌는 문제고, 이제 실버1 문제도 어느정도 잘 풀리는 느낌이다. 상반기 내로 백준 플레티넘 가고싶다.


n = int(input())
graph = []
for i in range(n):
   graph.append(list(map(int, input())))

cnt = []
arr = []

def dfs(graph, r, c):
    if( graph[r][c] == 1):
        graph[r][c] = 0
        cnt.append(1)
        D = [(0,1),(0,-1),(1,0),(-1,0)]
        for i,j in D:
            if(0<= r+i < n and 0<= c+j < n and graph[r+i][c+j] == 1):
                dfs(graph, r+i,c+j)
    return cnt.count(1)


for i in range(n):
    for j in range(n):
      if(graph[i][j] == 1) :
        arr.append(dfs(graph, i, j))
        cnt = []

arr.sort()
print(len(arr))

for i in range(len(arr)):
    print(arr[i])