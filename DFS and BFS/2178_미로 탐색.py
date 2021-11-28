n, m = map(int, input().split()) ##세로길이와 가로길이를 입력

Miro = [] #우리가 탈출해야하는 미로. 1은 길이고 0인 벽이다.
for i in range(n):
    Miro.append(list(map(int,input()))) # 미로생성중. 가로로 한줄씩 손수 제작한 핸드메이드 미로


checklist = [[0,0]] # 우리의 위치를 표시해줄 체크리스트 입니다.
dx = [0,0,1,-1] # 우리는 위 아래 왼 오 4가지 선택지의 이동을 가지고 있습니다. 2차원 Cartesian Coordinate System의 느낌
dy = [1,-1,0,0] # 하나가 0일때 나머지가 1,-1 , 다른게 0일때 남은게 1,-1. for로 돌거라서 순서는 크게 상관 X
while checklist: #위치가 사라지면 끝나겠쬬???
    a,b = checklist.pop(0) ## 우리의 위치에서 시작을 합니다. 하나씩 팝으로 뽑아주자구요
    for i in range(4): #아까 해줬던 좌표이동을 해줍시다. 우리의 위치라는 a,b에서 시작해서 이동한걸 x,y로 표현
        x = a + dx[i]
        y = b + dy[i]
        if( 0 <= x < n and 0 <= y < m and Miro[x][y] == 1) : #미로 안에 위치가 있어야하고. 길로만 가야곘죠?
            if(not (x ==0 and y == 0)): #이거는 처음에 왔던길로 가는거 방지하려고 넣어봤어요
                  Miro[x][y] = Miro[a][b] + 1 #미로라는 배열에는 그 위치까지 가는데 얼마나 걸었는지 표시해주게 바뀝니다.
                  checklist.append([x,y]) #걸어갔으면 위치를 업데이트 해줍니다.

print(Miro[n-1][m-1]) #마지막 위치까지 가는데 얼마나 걸었는지가 정답이 됩니다.
