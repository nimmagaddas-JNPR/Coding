#Find the second minimum element of an array
# Eg: [2,5,6,7,1,8,9,0] o/p: 2

def findSecondMin(arr):
  firstMinIdx = 0;
  secondMinIdx = 0;
  for i in range(len(arr)):
    if( arr[i] < arr[firstMinIdx]):
      secondMinIdx = firstMinIdx
      firstMinIdx = i
    elif( arr[i] < arr[secondMinIdx]):
      secondMinIdx = i
  return arr[secondMinIdx];

print(findSecondMin([2,5,6,7,1,8,9,0]))
print(findSecondMin([22,34,56,32,11,34,23,21,34]))
print(findSecondMin([34,54,32,33,45,67,78,86,3,45,6]))
