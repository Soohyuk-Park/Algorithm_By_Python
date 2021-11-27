from collections import deque


def solution(m, n, tomatoes):
    count = 0  # Count number of days
    deq = deque()
    # deq = list()
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def search(row, col):
        searched_list = []

        for i, j in D:
            if (row + i < N and col + j < M) and (row + i >= 0 and col + j >= 0):
                #이 부분은 row, col이 사각형 외부로 나가지않게 해주는 코드
                if tomatoes[row + i][col + j] == 0:
                    tomatoes[row + i][col + j] = 1
                    searched_list.append((row + i, col + j))
                    #그 좌표가 0이면
                    #search( 1,3 )이라면 1,3기준으로 주변에 0인걸 1로 바꿔줌
                    #그리고 searched_list에 그 좌표들을 추가해줌
        return searched_list
    #새롭게 추가된 Searched_list반환

    # Add all riped tomatoes
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                deq.append((r, c))
                #deq에는 토마토가 있는 좌표들이 저장됨

    # Search begin
    while deq:
        for _ in range(len(deq)):#토마토의 개수만큼 반복
            r, c = deq.popleft()#토마토가 있는 좌표를 꺼냄
            for tomato in search(r, c):#그 좌표에 대하여 search수행
                #search를 수행한다는건 그 좌표 기준으로 주변의 0을 1로 바꾸고
                #searched_list에 주변좌표들을 반환한다는 의미
                deq.append(tomato)## Deq에는 새롭게 익은 토마토가 추가.
        count += 1

    # Check unriped tomato(es) after search
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 0:
                return -1

    return count - 1


if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    tomatoes = [[int(n) for n in input().split(" ")] for _ in range(N)]
    print(solution(M, N, tomatoes))
