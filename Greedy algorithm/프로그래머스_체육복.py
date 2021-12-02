# https://programmers.co.kr/learn/courses/30/lessons/42862 #

'''def solution(n, lost, reserve):
    lost.sort()  ##sort를 안해주면 오류가 생긴다. 이유가 뭘까? 애초에 정렬된 배열이 들어오는 줄 알았는데 아니었나보다.
    reserve.sort()
    can = [1] * (n + 1)
    while lost: # 여벌체육복 && 잃어버림 동시에 있는 조건을 먼저 처리해주면 좋기는할듯.
        for k in range(n+1):
          if (k in lost and k in reserve):
               lost.pop(lost.index(k))
               reserve.pop(reserve.index(k))
               can[k] = 1

        k = lost.pop(0)
        can[k] = 0


        if (k in reserve):
            can[k] = 1
            reserve.pop(reserve.index(k))
        elif ((k - 1) in reserve):
            can[k] = 1
            reserve.pop(reserve.index(k - 1))
            continue
        elif ((k + 1) in reserve):
            can[k] = 1
            reserve.pop(reserve.index(k + 1))
            continue
    N = (can.count(1) - 1)

    answer = N
    return answer

print(solution(3,[1,2],[2,3]))''' #여기까지가 내가 푼 정석적인 풀이

#아래는 다른분들 풀이로 복습

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]# 여분의 체육복 있고 + 본인은 잃어버리지 않음= 빌려줄 수 잇는 사람들
    _lost = [l for l in lost if l not in reserve]# 잃어버렸고 + 여분 없음 = 빌려야하는 사람들
    for r in _reserve: #빌려줄수 있는 사람을 기준으로 앞과 뒤를 본다.
        f = r - 1
        b = r + 1
        if f in _lost: #앞사람이 없다면 일단 빌려주고.
            _lost.remove(f)
        elif b in _lost:# 앞사람이 있는데, 뒷사람이 없으면 뒷사람 빌려주고.
            _lost.remove(b)# 빌려줬으면, 빌려야하는 사람의 배열에서 빼줘야지
    return n - len(_lost) #총 수에서 빌려하는 수를 빼면 남는게 답