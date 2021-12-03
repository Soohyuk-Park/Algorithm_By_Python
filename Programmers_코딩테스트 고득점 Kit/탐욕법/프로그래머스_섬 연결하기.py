# https://programmers.co.kr/learn/courses/30/lessons/42861 #
# 이런걸 '크루스칼 알고리즘'이라고 한다네요.
# 그래프 문제 요즘 dfs,bfs하면서 좀 풀었지만 이런건 또 좀 새롭네..

def solution(n, costs):
    sorted_costs = sorted(costs, key = lambda x: x[2])  ## 최소비용을 찾는거라 일단 비용대로 정렬
    costs_sum = sorted_costs[0][2] # 나중에 리턴할 값이라서 하나씩 차근차근 더해준다.
    path = set({sorted_costs[0][0], sorted_costs[0][1]}) # path는 집합으로 지금까지 지나온 길들을 저장
    sorted_costs.pop(0) # 정렬된거에서 처음꺼는 정보 다 알았고 저장도 했으니 팝팝

    while len(path) != n: # path가 모든 점들을 보유할때까지 합시다.
        for cost in sorted_costs: # cost는 for문을 돌면서 0번째 1번째에는 각각 노드의 정보 2번째에는 그 노드들 연결비용
            if cost[0] in path and cost[1] in path: # 둘 다 이미 있으면 무시해
                continue
            elif cost[0] in path or cost[1] in path:# 하나만 있으면 그건 추가해줘야지!
                path |= set({cost[0], cost[1]})
                costs_sum += cost[2]
                sorted_costs.remove(cost)
                break
    return costs_sum
