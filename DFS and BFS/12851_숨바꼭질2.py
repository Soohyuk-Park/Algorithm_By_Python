#  https://www.acmicpc.net/problem/12851 ##

# 숨바꼭질 1 문제에서 하나의 조건이 더 추가되었다.
# 그래서 이번에는 1차원 배열 대신에 2차원 배열을 사용했다.
# 배열의 [0]인덱스에는 숨바꼭질 1 문제와 같은 연산을 하고 [1]인덱스에는 새로운 연산( 경우의 수 )
# 처음엔 아예 새로 함수를 만들어야하나 싶었는데 이런식으로 2차원 배열을 활용하는게 신선했다.

from collections import deque


def bfs(n):
    q = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        x = q.popleft()

        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    q.append(i)

                elif visited[i][0] == visited[x][0] + 1:
                    visited[i][1] += visited[x][1]


n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

bfs(n)
print(visited[k][0])
print(visited[k][1])