## https://www.acmicpc.net/problem/1043 ##
## 이건 내가 처음에 푼 풀이이다.
# while문에서 반복을 좀 시켜줘야되는데
# 적당하게 반복하는걸 어떻게 해야할지 몰라서 그냥 쭉쭉 하다가 바뀌지 않는 순간까지로 정했다.
# 그래프 이론으로 푸는 문제인데 나는 그래프스럽게 풀지는 않은 것 같다..
# 그래서 풀이를 좀 더 찾아보기로 했다. 골드4인데 잘 풀려서 기분이 좀 좋다. ( 3월전에 골드 100문제 달성하기 목표 )

n,m = map(int,input().split())

jinsil = []
party = [[] for _ in range(m+1)]

L = list(map(int, input().split()))

for i in range(1,len(L)):
    jinsil.append(L[i])



for i in range(1,m+1):
    R = list(map(int, input().split()))
    for j in range(1,len(R)):
        party[i].append(R[j])

possible = [1] * ( m + 1)

Q = 0
QQ = 1



while Q != QQ:
    cnt = 0
    for i in jinsil:
        for j in range(1,len(party)):
            # print(i)
            # print(party[j])
            if(i in party[j] and possible[j]==1):
                possible[j] = 0
                cnt += 1
                jinsil = jinsil + party[j]
    if( cnt == 0 ):
        Q += 1


print(possible.count(1) - 1)


#################짧은 풀이 by iknoom1107##################

# N, M = map(int,input().split())
# # N : 사람수 M : 파티수
# q = list(map(int,input().split()[1:]))
# # q : 진실을 아는 사람들
# P = [set(map(int,input().split()[1:])) for _ in range(M)]
# # 각 파티에 있는 사람들
# V = [False] * M
#
# for u in q:
#     for i in range(M):
#         if not V[i] and u in P[i]: V[i] = True; q += list(P[i]-{u})
# print(M-sum(V))
#####