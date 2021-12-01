## https://programmers.co.kr/learn/courses/30/lessons/43162
## 틀려서 멘붕왔는데, 바로 고치니까 잘 작동해서 다행이다 ㅜㅜ 요즘 BFS/DFS관련 문제 좀 풀었는데 이정도 문제 안풀리면 안되지
## 밤이라 집중력 떨어져서 그런가 너무 의식의 흐름으로 한거같고.
## 이런 문제는 다양한 풀이들이 더 존재할 수 있는 것 같다.
## 그래도 지금 풀이 나쁘지 않은 것 같고, 처음엔 이해도 못했던 알고리즘을 이해하고 활용하는 과정이 즐겁다.
## 취업을 할 수 있을지 아니면 뭐가 될런지 잘은 모르곘고 조금 불안하면서 걱정도 많다
## 그래도 문제를 풀고 성공을 받는 지금 이 순간의 기쁨과 성취의 뿌듯함을 즐기자.

def solution(n, computers):
    numnet = 0 ## 이거는 네트워크 숫자입니다.
    visited = [False] * (n+1) # visited[ 여기는 그냥 숫자 칸 넣으면 된다 ] 노테이션 편리하게 하려구

    def dfs(v, computers):
        if(visited[v] == False): ## 방문한적 없으면.
            visited[v] = True
            for i in range(1, n+1):
                if (computers[v - 1][i - 1] == 1 and visited[i] == False):
                    dfs(i, computers) ## dfs는 함수 자체에서는 -1이 되지만 함수에 대입할때는 i로 넣어주세요

    for j in range(1,n+1): # 1--n까지 쭉 해줄건데
        if( visited[j] == False):# 아직 방문 안했어야만 dfs를 도려줄거에요.
          dfs(j, computers)
          numnet += 1 #한 번의 dfs를 돌았다는건 네트워크를 다 돈거다.
        if( visited.count(True) == n): # 모든 칸들에 대해 네트워크를 탐색했으면 종료해야지
            break

    answer = numnet# 네트워크 숫자 구하는 문제니까 그냥 이게 정답
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))