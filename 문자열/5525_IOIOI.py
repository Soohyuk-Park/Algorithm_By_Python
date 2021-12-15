
# 50점짜리 풀이

n = int(input())
str = 'I' + 'OI'*n
str = list(str)

m = int(input())
target = input()
target = [char for char in target]
cnt = 0
for i in range(len(target) - len(str) + 1):
    if(str == target[i:i+len(str)]):
        cnt += 1
print(cnt)

# 참고한 100점짜리 풀이( 복습하자 )
n = int(input())
m = int(input())
s = input()

stack = [i for i in range(len(s)) if s[i]=='I']
count, answer = 0, 0

for i in range(1, len(stack)):
    if stack[i]-stack[i-1]==2: count += 1
    else: count = 0
    if count >= n: answer += 1

print(answer)


### 또 다른 100점 풀이( 나중에 이해해봅시다.. ) 어떻게 한건지 바로 눈에 들어오지가 않네

N = int(input()) ## 처음 IOI의 O의 개수
M = int(input()) ## 비교할 문자열의 개수
S = input() ## 비교할 문자열 입력받고.

ans = 0
dfs = [[0, 1], [2, 1], [0, 1]]
state = 0
streak = 0

for c in S: ## 비교할 문자열에서 하나씩 가져온다.
    new_state = dfs[state][int(c == 'I')] #

    if state == 2 and new_state == 1:
        streak += 1
        if streak >= N:
            ans += 1
    if state + new_state != 3:
        streak = 0

    state = new_state

print(ans)
