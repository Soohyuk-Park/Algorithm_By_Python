from collections import deque


def solution(m, n, tomatoes): #우리가 원하는 답을 만들어줄 Solution함수. 이름만큼 듬직하네요.
    count = 0  # Count number of days
    deq = deque()
    # deq = list()
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 내가 dx, dy 따로 했던거랑 다르게 이런식의 설정이 가능하다면 더 효율적일수도 있다는 생각이 든다.
    # 좋은 방향이 있다면 흡수하고 배우자.
    def search(row, col): #서치 함수를 설정했는데 이게 뭔지 함 살펴봅시다~
        searched_list = [] # 서치 함수가 도는 순간 서치리스트가 빈 리스트로 생기네요?? 이게 뭘까여

        for i, j in D: #이거의 의미는 당연히 2차원 배열상에서의 위치이동이겠죠
            if (row + i < N and col + j < M) and (row + i >= 0 and col + j >= 0):
                #이 부분은 row, col이 사각형 외부로 나가지않게 해주는 코드
                if tomatoes[row + i][col + j] == 0: #최초의 서치는 토마토의 위치이기에 거기서 한 칸 떨어진 이동칸에서 값이 0이면 거기를 1로 바꿔줍시다.
                    tomatoes[row + i][col + j] = 1
                    searched_list.append((row + i, col + j)) #이제 아까 빈 리스트였던 서치리스트가 나왔네요. 여기다가 새롭게 토마토가 된 칸의 위치를 넣어줍니다.
                    #그 좌표가 0인데 1(토마토) 바로 근처에 있으니까요!
                    #search( 1,3 )이라면 1,3기준으로 주변에 0인걸 1로 바꿔줌
                    #그리고 searched_list에 그 좌표들을 추가해줌. 즉 서치리스트에 있는 좌표들은 새롭게 토마토가 된것들이네요~
        return searched_list
    #새롭게 추가된 Searched_list반환
    # 즉 search( 4, 5 ) 을 하면 좌표상에 4행 5열의 토마토를 기준으로 0이던걸 1(토마토)로 바꾸면서 그 좌표들을 전부 가진 리스트를 만들어줍니다.
    
    for r in range(N):
        for c in range(M):      #여기서는 뭐를 할까요?
            if tomatoes[r][c] == 1: #보니까 토마토가 맞는지 확인하네여
                deq.append((r, c)) #토마토가 맞다면 deq에 그 좌표를 추가합니다.
                #deq에는 토마토가 있는 좌표들이 저장되었다는 사실을 기억합시다.

    # Search begin
    while deq: #토마토의 좌표가 전부 사라질때까지~~ 뭘 하려나?
        for _ in range(len(deq)): #토마토의 개수(좌표수)만큼 반복
            r, c = deq.popleft()  #토마토가 있는 좌표를 꺼냄
            for tomato in search(r, c):  #그 좌표에 대하여 search수행
                #search를 수행한다는건 그 좌표 기준으로 주변의 0을 1로 바꾸고
                #searched_list에 주변좌표들을 반환한다는 의미
                deq.append(tomato)   ## Deq에는 새롭게 익은 토마토의 좌표들이 추가된다.
        count += 1 # 단위시간마다 이미 존재하는 토마토 기준으로 상하좌우 토마토 바꾸기를 진행하니까 시간이 1만큼 지났음을 표시


    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 0:  # 모든 과정이 끝났는데. 여전히 안익은 토마토가 있다며? 문제의 조건에 따라 -1을 반납해줍시다.
                return -1 # 이 부분은 완성된 배열에서 그냥 0이 있나 보는거니까 쉽죠?

    return count - 1  #마지막으로 count -1 을 리턴하게 됩니다. 토마토를 전부 채운 마지막 시점에서도 한 번 더 while 문이 돌아서. 낭비한 시간이 하나 있겠죠?


if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    tomatoes = [[int(n) for n in input().split(" ")] for _ in range(N)]
    print(solution(M, N, tomatoes))
