# https://www.acmicpc.net/problem/18870
# 정렬시키면서 set으로 만든다.
# dic으로 각 원소의 순서 저장하고
# arr(쳐음 배열) 에 대해새 for문으로 하나씩 꺼냄
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
#print(arr)

arr2 = sorted(list(set(arr)))
#print(arr2)
dic = {arr2[i] : i for i in range(len(arr2))}
#print(dic)
for i in arr:
    print(dic[i], end = ' ')