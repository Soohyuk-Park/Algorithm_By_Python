# https://www.acmicpc.net/problem/1629
# 똑같은 방식이었는데, 재귀로 해야 시간초과가 안난다.
# 아래와 같이 파워함수 안에 또 파워를 하는데 b를 절반으로 쪼갠걸 temp로 해준다.

def power(a, b):
    if b == 1:  # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2)  # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C  # b가 짝수인 경우
        else:
            return temp * temp * a % C  # b가 홀수인 경우


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)

####### 다른분의 풀이( 같은  방식인데 그냥 한 번 더 보면서 복습 )
a, b, c = map(int, input().split(' '))


def dnc(length):
    if length == 1:
        return a % c
    if length % 2 == 0:
        left = dnc(length // 2)
        return left * left % c
    else:
        left = dnc(length // 2)
        return left * left * a % c


print(dnc(b))