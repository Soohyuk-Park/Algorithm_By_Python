# https://www.acmicpc.net/problem/2108
# 최빈값을 구하는 부분만 좀 까다로웠고, 나머지 부분은 그냥저냥~

from collections import Counter

N = int(input())
arr = []
for i in range(N):
    k=int(input())
    arr.append(k)

brr = arr.copy()
brr.sort()

cnt = Counter(arr)
Bindo = cnt.most_common()
Bindo.sort(key = lambda x:x[0], reverse = False)
Bindo.sort(key = lambda x:x[1], reverse = True)

V = round((sum(arr)/len(arr)),0)
print(int(V))
print(brr[len(arr)//2])

if( N == 1):
    print(arr[0])
elif(Bindo[0][1] == Bindo[1][1]):
    print(Bindo[1][0])
else:
    print(Bindo[0][0])
print(max(arr) - min(arr))


##############################################################
# 푸는데 도움이 됐던 내용들을 정리해두자.
# 출처는 https://codepractice.tistory.com/71
from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter(colors)
cnt
## cnt에 대한 결과 : Counter({'blue': 3, 'red': 2, 'green': 1})

numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5]
from collections import Counter
cnt = Counter(numbers)
cnt.most_common()#괄호안에 숫자 넣으면 상위 n개에 대한 정보만!
## 에 대한 결과 [(4, 3), (3, 2), (5, 2), (1, 1), (2, 1)]