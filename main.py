arr = [[1,3,9], [8,3,5], [5,3,2]]
averagesArr = []
averagesDict = {}
result = []

def calculateAvarega(arr):
    return (sum(arr) / len(arr))

for i in arr:
    average = calculateAvarega(i)
    averagesDict[average] = i
    averagesArr.append(average)

averagesArr.sort()

for a in averagesArr:
    result.append(averagesDict[a])

print('Starting array:', arr)
print('Sorted array by average value:',result)