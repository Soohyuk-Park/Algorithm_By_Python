# https://www.acmicpc.net/problem/1920
# 처음엔 그냥했다가 시간초과떠서 리스트를 쪼개서 해보니까 됐다.

n = int(input())
arr1 = list(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()

arr11 = arr1[0:len(arr1)//2]
arr12 = arr1[len(arr1)//2:len(arr1)]
half = arr1[len(arr1)//2]

for i in range(m):
    if(arr2[i] < half ):
        if(arr2[i] in arr11):
            print(1)
        else:
            print(0)
    else:
        if (arr2[i] in arr12):
            print(1)
        else:
            print(0)

#풀기는 했지만 너무 별로인 풀이 같아서 다른 분들의 코드를 리뷰하는 시간을 가져본다.
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

arr = [1 if x in A else 0 for x in B]

for x in arr:
    print(x)
###??? 내가 처음에 한거랑 비슷한데 이건 시간초과 아닌가보네.. 이런식으로.. 신기하구먼
# 심플하고 저거 for문하고if를 한 줄에 쓰는거 아직 익숙치 않은데 잘 배워두자.

#이분 탐색

n = int(input())
A = list(map(int,input().split()))
m = int(input())
M = list(map(int,input().split()))

A.sort()

def binary_search(arr, start, end, target):
    if start>end: return False

    mid = (start+end) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr,start,mid-1,target)
    elif arr[mid] < target:
        return binary_search(arr,mid+1,end,target)

for i in M:
    if binary_search(A,0,len(A)-1,i): print(1)
    else: print(0)

## 이것도 신기하고 재밌넹 ㅋㅋㅋ 잘 봐두고 연습도 해보자.