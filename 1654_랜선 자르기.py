# https://www.acmicpc.net/problem/1654 #
# 잘 기억해두자. 처음엔 뻘짓으로 for 문 돌려고 풀려했는데 말도 안되는 소리였고
# while이라는 단순한 함수를 어떻게 이용하는지가 알고리즘 풀이에 있어서 상당히 중요하다는 생각이 든다
# Que가 빌때까지 라는 조건을 주거나 지금처럼 처음이 끝을 넘을때 라던가..전부 신기한 조건들

k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
start = 1
end = max(line)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in line:
        cnt += i // mid
    if cnt >= n:  # 자른 개수가 많으면 -> 더 크게잘라야함
        start = mid + 1
    else:
        end = mid - 1
print(end)