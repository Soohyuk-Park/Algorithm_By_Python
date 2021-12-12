## https://www.acmicpc.net/problem/4948 ##
# 소수의 리스트를 만들기 위해서 제일 먼저 is prime정의하기
# 루티까지만 for문 돌리기. 안그러면 시간초과
# 그리고 필요한 만큼 리스트 소수로 채워두고 원하는 범위에서 카운팅스타~ 밤하늘의 펄

def is_prime(v):
    if( v== 1):
        return False
    else:
        for i in range(2,int(v**(1/2)) + 1):
            if( v % i == 0 ):
                return False
        return True

Prime = []

for i in range(1, 246912):
    if(is_prime(i)):
        Prime.append(i)

while 1:
    n = int(input())
    cnt = 0
    if n == 0 :
        break
    else:
        for i in Prime:
            if( n < i < 2*n +1):
                cnt += 1
    print(cnt)
    continue