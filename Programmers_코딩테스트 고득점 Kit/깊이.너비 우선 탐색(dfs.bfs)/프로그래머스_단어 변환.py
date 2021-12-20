#https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]

    if target not in words:
        return 0

    def compare_helper(a,b):
        diff = 0
        for i in range(len(a)):
            if( a[i] != b[i]):
                diff += 1
        if( diff == 1 ):
                return True
        return False
    def bfs(current, words, visited):
        q = deque()
        q.append((current,0))
        while q:
            A = q.popleft()
            if( A[0] == target):
                return A[1]
            for k in range(len(words)):
                if  compare_helper(A[0],words[k]) and visited[k] == 0:
                    q.append((words[k],A[1]+1))
                    visited[k] = 1
        return 0

    return bfs(begin, words, visited)

print(solution("hit","cog",["hot","cot","cog"]))