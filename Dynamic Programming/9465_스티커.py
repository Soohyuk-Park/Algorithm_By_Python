#https://www.acmicpc.net/problem/9465
# 얼마나 걸린거냐.. 오류가 계속떠서 ㅜㅜㅜ 결국은 풀었다 장하다 장해 나의 끈기 칭찬해
# 너무 졸리다............... 이거만 풀고 자려했는데 이렇게 안 풀릴 일인가
# 99%에서 100% 넘어가면서 계속 오류가 떴다. 이유는 dfs함수에서 N=2인 경우에
# 마지막에 나오는 max값을 print만 하게 해두고 return을 안해서 그런거였다.
# 그래서 다시 값을 리턴하게 바꾸고 뒤에서는 dfs의 값을 반환하게 만들었다.
# 추가적인 코드 학습이 필요하겠다.(다른분들 풀이 리뷰) 내일 다시 하자 지금 너무 피곤해서 잘거야ㅑㅑㅑ 그래도 성취감 굿굿

t = int(input())

def dfs(graph):
    N = len(graph[0])
    # if(N == 1):
    #     print(max(graph))
    if(N == 2):
        return max(graph[0][0]+graph[1][1] , graph[0][1] + graph[1][0])
    else:
     score = [[0]*len(graph[0]) for _ in range(2)]
     score[0][0] = graph[0][0]
     score[1][0] = graph[1][0]
     score[0][1] = score[1][0] + graph[0][1]
     score[1][1] = score[0][0] + graph[1][1]
     for i in range(2, len(graph[0])):
        score[0][i] = max( score[1][i-1] + graph[0][i], score[0][i-2] + graph[0][i],score[1][i-2] + graph[0][i]  )
        score[1][i] = max( score[0][i-1] + graph[1][i], score[1][i-2] + graph[1][i],score[0][i-2] + graph[1][i]  )
     return (max(score[0][N-1],score[1][N-1]))






for _ in range(t):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int,input().split())))
    if( len(arr[0]) == 1):
        print(max(arr[0][0],arr[1][0]))
        continue
    arr2 = [[0]*len(arr[0]) for _ in range(2)]
    if(len(arr[1]) >= 3):
      for i in range(len(arr[1])):
         arr2[0][i] = arr[0][len(arr[1]) - 1 - i]
         arr2[1][i] = arr[1][len(arr[1]) - 1 - i]
    print(max(dfs(arr),dfs(arr2)))



#다른분의 코드를 리뷰( 백준 'rhs0266'님 )
import sys
si = sys.stdin.readline
TT = int(input())
for _TT in range(TT):
    n = int(input())
    a= [[0, 0] for _ in range(n)]
    for j in range(2):
        b = list(map(int, input().split()))
        for i in range(n):
            a[i][j] = b[i] # 여기선 스티커를 세로로 세웠다.



    dy = [[0, 0, 0] for _ in range(n)]

    # 초기값 채우기
    dy[0][1], dy[0][2] = a[0][0], a[0][1]

    # 점화식을 토대로 dy 배열 채우기
    for i in range(1, n):
        for prev in range(0, 3):
            dy[i][0] = max(dy[i][0], dy[i - 1][prev])
            for j in range(2):
                if prev & (1 << j): continue
                dy[i][1 << j] = max(dy[i][1 << j], dy[i - 1][prev] + a[i][j])

    print(max(dy[n - 1]))
#비트 마스크를 사용한듯하다. 너무 좋다.. 기말고사 끝나면 열심히 복습하고 관련문제 풀어보자.