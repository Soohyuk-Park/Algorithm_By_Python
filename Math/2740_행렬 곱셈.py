# https://www.acmicpc.net/problem/2740
# 이왜브? ( 이게 왜 브론즈 라는 뜻 )

r1,c1 = map(int,input().split())
mat1 = []


for i in range(r1):
    L = list(map(int,input().split()))
    mat1.append(L)


r2,c2 = map(int,input().split())
mat2 = []
for i in range(r2):
    L = list(map(int,input().split()))
    mat2.append(L)
result = [[0]*c2 for _ in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += mat1[i][k] * mat2[k][j]
for i in result:
    for j in i:
        print(j,end=' ')
    print()