import math


def build(links):            # 이거는 그냥 트리를 만들어주려는 코드라 어렵지 않음. 쏘 이지 문제는 뒤에 있는데
    tree = [[] for _ in range(len(links) + 1)]
    for p, q in links:
        tree[p - 1].append(q - 1)
    return tree


def calc(iTable, eTable, sales, tree, idx): # 여기에 I,T 테이블과 세일즈정보 트리 그리고 시작의 인덱스까지 다 주어진다.
    if len(tree[idx]) == 0: # 트리의 안에서 길이가 0이라는건 뭘까? 자기 밑으로 직원이 없다는거지
        iTable[idx] = sales[idx] #그러면 그냥 자기 포함했을때의 값은 자신의 세일즈에서 값 더해주면 끝
        return
    diff = math.inf
    for child in tree[idx]: #여기서 이제 어려워지기 시작한다... 일단 특정 부모노드에서 시작할경우에 자식(직원)을 하나하나 다 봐줘야하는데
        calc(iTable, eTable, sales, tree, child) # 그 자식에 대해서도 자식이 있다면 그것도 쭉쭉 다 봐줘야한다.
        local = iTable[child] - eTable[child] # 이거는 각 자식노드에서 I,T중에 뭐가 더 큰지를 판별( 왜냐면 작은것만 더해서 위에꺼를 만들어야하니까 )
        # iTable[idx] = min(iTable[child], eTable[child])
        if local > 0: # local이 음수라는건 E테이블쪽 값이 더 크다는거에요
            iTable[idx] += eTable[child] #그러면 위에 테이블( 부모노드 ) 에 더할때 E를 더해주세요.
            diff = min(diff, local) # 여기서 만약 나중에 봤는데 자식노드가 다 E를 택했다면 차이중에 제일 작은걸 더해줘야함
                                    # 이 과정은 적어도 하나는 I여야 하니까 차이 제일 작은거에 차이를 더해서 E를 I로 만드는거지
        else: #이거는 I가 더 크다는거 -> 즉 I에서 선택하게됨 -> 나중에 굳이 E를 I로 바꿀필요 없다. -> 그래서 diff는 0으로 설정돼서 나중에 더하지 말도록
            iTable[idx] += iTable[child]
            diff = 0

    eTable[idx] += iTable[idx]# 위의 과정에서 iTable에는 자식노드들에서 그냥 무조건 작은것만 골라놨음
    eTable[idx] += diff # diff가 존재한다는건 모두 Excluded라는거고 그러면 제일 차이가 작은거 하나를 included로 바꾸는 과정
    iTable[idx] += sales[idx] # 그리고 itable은 자신을 포함한거니까 스스로의 sales를 더해주자


def solution(sales, links):
    tree = build(links)
    iTable = [0] * len(sales)
    eTable = [0] * len(sales)
    calc(iTable, eTable, sales, tree, 0)
    return min(iTable[0], eTable[0])