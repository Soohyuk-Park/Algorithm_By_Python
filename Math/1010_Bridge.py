n = int(input())

for i in range(n):
    n,m = map(int, input().split())
    a,b =(1,1)
    for i in range(n):
        a *=( m - i )
    for i in range(n):
        b *= i+1
    c = a / b
    print(int(c))
