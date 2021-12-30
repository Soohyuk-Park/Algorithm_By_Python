#https://www.acmicpc.net/problem/2004
def num_two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two
def num_five(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

n,m = map(int,input().split())
a,b,c=num_five(n),num_five(m),num_five(n-m)
d,e,f=num_two(n),num_two(m),num_two(n-m)
print(min(a-b-c,d-e-f))