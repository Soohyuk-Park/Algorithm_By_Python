import sys
input = sys.stdin.readline

A = input().strip().upper() #문자2개를 입력받을건데, 각각 A,B라고 저장해두자.
B = input().strip().upper()
len1 = len(A)# 단어의 길이도 받아두고
len2 = len(B)

graph = [[0] * (len2 + 1) for _ in range(len1 + 1)] #이게 핵심.
#A,B 의 각 글자를 인덱스를 a,b로해서 graph[a][b]에 거기까지의 겹치는 LCS숫자를 출력해두자.

for i in range( 1, len1 + 1):
   for j in range( 1, len2 + 1):
      if A[i-1] == B[j-1]:## 글자가 같다면 그 전까지( 대각선 기준 왼쪽 위 ) 보다 하나가 더 추가된 느낌
         graph[i][j] = graph[i-1][j-1] + 1
      else: # 거기서 추가가 안되면 그 전까지랑 같은건데. A,B뭐든 하나만 줄여보고 둘중에 큰걸로 ㄱㄱ
         graph[i][j] = max(graph[i-1][j] , graph[i][j-1])



print(graph[-1][-1])