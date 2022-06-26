from itertools import combinations
import copy
n,m,d = map(int,input().split())

# n * m 크기의 격자
# n + 1 번째 행에는 성
# 궁수 3명 배치
# 거리 D이하인 적 중에서 가장 가까운 적 공격
# 그러한 적이 여럿이면 가장 왼쪽에 잇는 적을 공격
# 같은 적이 여러 궁수에게 공격당할 수 있다.

realGameMap = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
def attack(archerList):
    A = []
    for one in archerList:
        temp = []
        for r in range(n):
            for c in range(m):
                if gameMap[r][c] == 1:
                    dist1 = abs( one - c ) + abs( n - r )
                    if dist1 <= d:
                        temp.append((r,c,dist1))
        if not temp:
            continue
        T = sorted(temp, key=lambda x : (-x[2],-x[1]))
        A.append(T.pop())
    for i in A:
        if gameMap[i[0]][i[1]] == 1:
            global cnt
            cnt += 1
        gameMap[i[0]][i[1]] = 0

def move(gampMap):
    for i in range(1,n+1):
        if i == n:
            gameMap[-i] = [0]*(m)
            break
        gameMap[-i] = gameMap[-i-1]

def isEmpty(gameMap):
    finalStage = True
    for i in range(n):
        for j in range(m):
            if gameMap[i][j] == 1:
                finalStage = False
                break
    return finalStage

mylist = list(range(m))
answer = 0

for archerList in combinations(mylist, 3):
        gameMap = copy.deepcopy(realGameMap)
        cnt = 0
        while not isEmpty(gameMap):
            attack(archerList)
            #print(1)
            move(gameMap)
        answer = max(answer, cnt)
print(answer)




