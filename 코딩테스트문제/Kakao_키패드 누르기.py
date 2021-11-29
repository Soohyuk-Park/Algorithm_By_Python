from collections import deque
## https://programmers.co.kr/learn/courses/30/lessons/67256 ## 문제 링크

def solution(numbers, hand):
    graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [55, 0, 55]]
    right = [[3, 2]]
    left = [[3, 0]]

    def finder(v):
        find = [[v] * 3 for _ in range(4)]
        for i in range(4):
            for j in range(3):
                if (find[i][j] == graph[i][j]):
                    return (i, j)

    answer = ''
    for i in range(len(numbers)):
        this = numbers.pop(0)
        x, y = finder(this)
        if (y == 0):
            answer = answer + 'L'
            left.pop(0)
            left.append([x, y])
        if (y == 2):
            answer = answer + 'R'
            right.pop(0)
            right.append([x, y])
        if (y == 1):
            a = abs(left[0][0] - x)
            b = abs(left[0][1] - y)
            c = abs(right[0][0] - x)
            d = abs(right[0][1] - y)
            if (a + b < c + d):
                answer= answer + 'L'
                left.pop(0)
                left.append([x, y])
            elif (c + d < a + b):
                answer= answer + 'R'
                right.pop(0)
                right.append([x, y])
            elif (c + d == a + b):
                  if (hand == 'right'):
                      answer= answer + 'R'
                      right.pop(0)
                      right.append([x, y])
                  elif (hand == 'left'):
                      answer= answer + 'L'
                      left.pop(0)
                      left.append([x, y])

        answer = ''.join(answer)

    return answer

hand = "right"
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], hand))