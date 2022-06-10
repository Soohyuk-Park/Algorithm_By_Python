target_number, numberOfBrand = map(int,input().split())

mok, namoji = divmod(target_number,6)
answer = 0
costArray = []
for i in range(numberOfBrand):
    setCost, oneCost = map(int,input().split())
    costArray.append((setCost,oneCost))
costArray.sort(key = lambda x : x[0])
minSetValue = costArray[0][0]
costArray.sort(key = lambda x : x[1])
minOneValue = costArray[0][1]
if( minSetValue > minOneValue*6 ):
    minSetValue = minOneValue*6
else:
    minSetValue = minSetValue
answer += minSetValue * mok
if( namoji * minOneValue > minSetValue ):
    answer += minSetValue
else:
    answer += namoji * minOneValue

print(answer)

