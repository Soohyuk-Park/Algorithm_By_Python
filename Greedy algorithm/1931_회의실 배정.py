# https://www.acmicpc.net/problem/1931 #
#이러한 알고리즘을 풀 때 최대의 회의실이 배정되기 위해서는
#끝나는 시간을 기준으로 정렬해줘야 된다. 증명은 나중에 해볼까..
##처음에 이 부분을 어떻게 정렬해야할지가 가장 의문이었다
#그리고 정렬을 하는 방법을 떠올린 뒤에는 크게 어렵지가 않았다.

n = int(input())

time = []

for i in range(n):
    n,m = map(int, input().split())
    time.append([n,m])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

start = 0
end = 0
cnt = 0

for a,b in time:
    if( end <= a):
       cnt += 1
       start = a
       end = b

print(cnt)