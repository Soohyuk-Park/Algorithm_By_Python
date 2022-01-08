n, m = map(int,input().split())
L = []
arr = [[0]*n for _ in range(n)]

for i in range(n):
    K = list(map(int,input().split()))
    L.append(K)
result = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
# def mat_zecob(matrix):
#     arr = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 arr[i][j] += (L[i][k]*L[k][j])
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] %= 1000
#     return arr

def mat_cob(A,B):
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[i][j] += ( A[i][k] * B[k][j] )
    for i in range(n):
        for j in range(n):
            arr[i][j] %= 1000
    return arr

m = bin(m)[2:]
for i in range(len(m)):
    if(m[-i-1] == '1'):
        temp = L[:]
        while i != 0:
            temp = mat_cob(temp,temp)
            i -= 1
        result = mat_cob(result,temp)

for row in result:
    print(*row)