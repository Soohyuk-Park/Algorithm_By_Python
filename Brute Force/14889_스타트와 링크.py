# https://www.acmicpc.net/problem/14889

from itertools import combinations
N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
members = [i for i in range(N)]
diff = int(1e7)
team_list = []
for i in (combinations(members,N//2)):
    i = list(i)
    team_list.append(i)

for i in range(len(team_list)//2):
    team_a = team_list[i]
    team_b = team_list[-1-i]
    sum_a = 0
    sum_b = 0
    for y in range(N//2):
        person_a = team_a[y]
        for z in team_a:
            sum_a += L[person_a][z]
    for y in range(N//2):
        person_b = team_b[y]
        for z in team_b:
            sum_b += L[person_b][z]
    diff = min(abs(sum_a-sum_b), diff)
print(diff)
