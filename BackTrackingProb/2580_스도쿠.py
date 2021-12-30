# https://www.acmicpc.net/problem/2580

import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)



######################### 비슷하지만, set을 활용하는 풀이
import sys


board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def get_possibles(r, c):
    possibles = set(range(1, 10))
    possibles -= set(board[r])
    test = set()
    for i in range(9):
        test.add(board[i][c])
    possibles -= test
    test = set()
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            test.add(board[i][j])
    possibles -= test
    return tuple(possibles)


def solve(i):
    if i == len(zeros):
        [print(*row) for row in board]
        sys.exit()
    r, c = zeros[i]
    possibles = get_possibles(r, c)
    for num in possibles:
        board[r][c] = num
        solve(i+1)
        board[r][c] = 0


solve(0)