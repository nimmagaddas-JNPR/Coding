def mergeTwoSortedArrs(n, arr1, arr2):
  arr1Ptr = n - 1
  arr2Ptr = len(arr2) - 1
  finalArrPtr = len(arr1) - 1;
  while (arr2Ptr >= 0):
    if arr1[arr1Ptr] < arr2[arr2Ptr]:
      arr1[finalArrPtr] = arr2[arr2Ptr]
      arr2Ptr -= 1
    else:
      arr1[finalArrPtr] = arr1[arr1Ptr]
      arr1Ptr -= 1
    finalArrPtr -= 1
  return arr1;


print(mergeTwoSortedArrs(6, [1,5,8,9,11,34, 0, 0, 0, 0, 0, 0],[2,4,5,7,14,32]))