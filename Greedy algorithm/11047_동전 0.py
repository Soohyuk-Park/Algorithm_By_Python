#전형적인 그리디 알고리즘
#큰 동전들이 작은 동전의 배수라 엄청 쉽게 풀린다.
#배수가 안되는 경우는 나중에 또 문제로 나오겠지.. 이것보단 훨씬 까다로울듯

n,m = map(int, input().split())
tmp = 0

coins = []

for i in range(n):
    coins.append(int(input().rstrip()))

coins.reverse()

for i in range(n):
    if m >= coins[i]:
        k = m // coins[i]
        m -= coins[i] * k
        tmp += k
    else:
        continue

print(tmp)