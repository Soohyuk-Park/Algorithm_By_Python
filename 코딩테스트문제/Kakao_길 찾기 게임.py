import sys

sys.setrecursionlimit(10 ** 6)  # 이걸 안해주면 횟수제한에 걸려서 재귀가 막혀버림

preorder = list()
postorder = list()
midorder = list()

def solution(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)  # 어떤 레벨이 있는지 파악
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)),
                   key=lambda x: (-x[1][1], x[1][0]))  # 노드좌표와 인덱스를 서로 연결 해 줌
    order(nodes, levels, 0)
    print(nodes)
    L = list(x[1] for x in nodes)
    print(L)
    midorder = sorted( list(x for x in nodes) , key=lambda x : (-x[1][1],x[1][0]) )
    midorder = list(x[0] for x in midorder)
    print(midorder)

    return [preorder, postorder, midorder]


def order(nodeList, levels, curLevel):
    n = nodeList[:]
    cur = n.pop(0)
    preorder.append(cur[0])
    if n:
        for i in range(len(n)):
            if n[i][1][1] == levels[curLevel + 1]: # 이번 레벨이랑 i번째의 y좌표가 같으면
                if n[i][1][0] < cur[1][0]: # i번째 n의 x좌표 < 지금의 x좌표
                    order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel + 1)
                if n[i][1][0] > cur[1][0]: # i번째 n의 좌표 >= 지금의 x좌표
                    order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel + 1)
    postorder.append(cur[0])

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
