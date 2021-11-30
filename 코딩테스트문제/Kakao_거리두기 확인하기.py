def solution(places):
    answer = []
    def check(arr):
        D = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]} #이거는 한 방향으로만 이동하는 경우. *2하면 두칸도 가능
        Q = {0: [1, 1], 1: [-1, 1], 2: [-1, 1], 3: [-1, -1]} #이거는 대각선으로 이동하는거
        isok = 1 # is_ok의 의미인데. 거리두기가 됐으면 ㅇㅋㅇㅋ니까 넘어가자는 의미~
        for i in range(5):
            for j in range(5): # for문 2개로 일단 모든 칸은 확인해봐요
                if(arr[i][j] == 'P'):#사람이 있다!!
                  for k in range(4):#그러면 이제 주변을 확인해야지
                      ni = i + D[k][0]
                      nj = j + D[k][1]
                      if(0 <= ni < 5 and 0 <= nj < 5 ):#여기서는 한 칸 떨어진 부분 먼저 확인
                             if( arr[ni][nj] == 'P'):## 사람이면 ? 0을 리턴해야지( 거리두기 실패니까 )
                               isok = 0
                               return isok
                  for k in range(4):
                      ni = i + D[k][0] * 2## 여기서는 두칸인데. 한 방향으로 2칸 떨어진경우
                      nj = j + D[k][1] * 2
                      if (0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == 'P'):
                            if (i - ni in [2, -2] or j - nj in [2, -2]):
                               if (arr[(i + ni) // 2][(j + nj) // 2] == "X"):#이 경우에 중간에 X로 칸막이 있으면 ㄱㅊ
                                   continue
                               else:
                                  isok = 0
                                  return isok
                  for p in range(4):
                       ni = i + Q[p][0]#여기서는 대각선으로 되어있는데
                       nj = j + Q[p][1]#이 때는 서로의 위치랑 크로스하는 모양으로 X가 있으면 ㄱㅊㄱㅊ
                       if (0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == 'P'):
                           if (arr[ni][j] == 'X' and arr[i][nj] == 'X'):
                                continue
                           else:
                               isok = 0
                               return 0
        return 1

    for b in range(5):
       check(places[b])
       answer.append(check(places[b]))
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))