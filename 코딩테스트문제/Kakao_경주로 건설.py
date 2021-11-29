import sys
from collections import deque


def solution(board):
    n = len(board)
    c = 0
    def dfs(start):  # row , col, cost , dir
        visited = [[sys.maxsize] * n for _ in range(n)]
        dic = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]}
        queue = deque([start])
        visited[0][0] = 0
        while queue:
            a, b, c, d = queue.popleft()
            for i in range(4):
                na = a+dic[i][0]
                nb = b+dic[i][1]
                if (0<=na<n and 0<=nb<n and board[na][nb]==0):
                    if(d == i):
                        nc = c + 100
                    else:
                        nc = c + 600
                    if visited[na][nb] > nc:
                        queue.append([na, nb, nc, i])
                        visited[na][nb] = nc
        return visited[-1][-1]

    return min([dfs((0, 0, 0, 0)), dfs((0, 0, 0, 1))])

board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))