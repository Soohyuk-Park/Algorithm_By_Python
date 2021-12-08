# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    lottos.sort()
    zero = lottos.count(0)
    visited = [0] * 6

    for i in range(6):
        for j in range(6):
            if (lottos[i] == win_nums[j]):
                visited[i] = 1

    cor = visited.count(1)
    N = zero + cor
    NN = cor
    if (zero == 0 and cor == 0):
        answer = [6, 6]
    elif (NN == 0):
        answer = [7 - N, 6]
    else:
        answer = [7 - N, 7 - NN]
    return answer