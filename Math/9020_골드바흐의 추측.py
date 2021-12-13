N = int(input())

def is_prime(v):
    if( v== 1):
        return False
    else:
        for i in range(2,int(v**(1/2)) + 1):
            if( v % i == 0 ):
                return False
        return True

Prime = []

x = 10001
y = 0

for i in range(1, 10000):
    if(is_prime(i)):
        Prime.append(i)

for i in range(N):
    a = int(input())
    x = 10001
    y = 0
    for j in range(len(Prime)):
        if( a - Prime[j] < 0):
            break
        elif( a - Prime[j] in Prime):
            K = Prime.index( a - Prime[j])
            if( abs(Prime[j]-Prime[K]) < abs(x - y)):
              x, y = Prime[j], Prime[K]
    print(x,y)
