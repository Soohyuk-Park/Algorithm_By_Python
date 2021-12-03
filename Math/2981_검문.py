## 여러가지 숫자가 주어졌다고 할 때
## 공통된 나머지를 가지게 만들기 위해서는 숫자들이
# A = X * a + P
# B = X * b + P
# C = X * c + P
# D = X * d + P
# 같은 형태이고 이러면
# A - B = X(a-b)
# B - C = X(b-c)
# C - D = X(c-d)
# 이렇게 되면 X라는거는 각각을 서로서로 뺀 수들의 최대공약수가 된다.
# 그리고 그 최대공약수의 약수들도 우리가 생각하는 조건을 만족시킬 수 있다




import math
t = int(input())
s = []
a = []
gcd = 0
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0]) #차이만 알면 되니까는 절댓값 씌워줍시다.
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)

gcd_a = int(gcd ** 0.5)

for i in range(2, gcd_a + 1): # 루트까지만 돌아 대신에 그거랑 오른쪽에 있는 공약수랑 쌍으로 세자
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)

a.append(gcd)
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')