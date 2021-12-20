#https://www.acmicpc.net/problem/11444
#숫자가 크니까 행렬 계산중에 나누기를 안해주면 계속 오류가 발생했다.

zero = [[1,0],[0,1]]
base = [[1,1],[1,0]]
SIZE = 2
def mat_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += (a[i][k] * b[k][j] ) % 1000000007
        return new

def getn(n):
    hang = zero.copy()
    k = 0
    tmp = base.copy()
    while 2**k <= n:
        if( n & (1<<k)) != 0:
            hang = mat_mul(hang, tmp)
        k+=1
        tmp = mat_mul(tmp,tmp)
    return hang[1][0] % 1000000007

N = int(input())
print(getn(N))