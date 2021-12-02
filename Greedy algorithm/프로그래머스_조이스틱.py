# https://programmers.co.kr/learn/courses/30/lessons/42860 #

# 처음에 완전 잘못 접근했다. 너무 단순하게 생각해서..
# 반성하고 철저한 피드백을 통해서 알고리즘을 하기위한 사고를 잘 확립하자
# 내가 처음 했던 생각은, 시작위치로부터 왼쪽 or 오른쪽으로 정해서 쭉쭉 가면서 뭐가 더 작은지 확인하는 코드였다.
# 일반적인 테스트 케이스에서는 잘 맞았지만, 몇 개의 실패가 있었다.
# 원인을 찾아보니 중간에 AAAA같은 배열이 있으면, 오른쪽으로 가다가 왼쪽으로 돌아간다음 끝부분에서 탐색을 하는게 좋아서 그랬다.
# 그러면 어떻게 접근을 해야하나?
# 이 문제는 이동과 알파벳 바꾸기를 따로 봐야한다.
# 그래서 각 칸들에 대해서 몇 번 바꿔서 알파벳을 바꿔야하는지를 구해두고
# min_move를 통해서 얼마나 ( A만났을 때 뒤로 백 한거  vs 그냥 쭉쭉 간거 ) 의 거리를 비교해서 더 작은걸 min_move로 쓴다.

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer