## https://programmers.co.kr/learn/courses/30/lessons/42576 ##

"""def solution(participant, completion):
    arr = [False] *(len(participant))
    for i in range(len(participant)):
        for j in range(len(completion)):
          if(participant[i] == completion[j]):
            arr[i] = True
            completion.pop(j)
            break
    answer = participant[arr.index(False)]
    return answer
# 이 풀이는 테스트케이스는 맞는데 효율성 테스트를 통과 못함 """

def solution1(participant, completion): # 1번 풀이
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()



import collections ## 좀 특이한 풀이라 적어둠


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
D = collections.Counter(participant)
print(collections.Counter(participant))
print(collections.Counter(completion))
print(collections.Counter(participant) - collections.Counter(completion))
print(D.keys())
