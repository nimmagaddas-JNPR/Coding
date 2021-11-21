# Merge 2 sorted arrays
# Eg: [1,5,8,9,11,34] [2,4,5,7,14,32] o/p: 2

def mergeTwoSortedArrs(arr1, arr2):
  finalArr = [];
  arrayOnePtr = 0;
  arrayTwoPtr = 0;
  while(arrayOnePtr < len(arr1) and arrayTwoPtr < len(arr2)):
    if(arr1[arrayOnePtr] < arr2[arrayTwoPtr]):
        finalArr.append(arr1[arrayOnePtr]);
        arrayOnePtr += 1;
    else:
      finalArr.append(arr2[arrayTwoPtr]);
      arrayTwoPtr += 1;
  if (arrayOnePtr < len(arr1)):
    finalArr += arr1[arrayOnePtr:]
  if (arrayTwoPtr < len(arr2)):
    finalArr += arr2[arrayTwoPtr:]
  return finalArr;

print(mergeTwoSortedArrs([1,5,8,9,11,34],[2,4,5,7,14,32]))
print(mergeTwoSortedArrs([34,56,66,78,89,98],[3,5,67,77]))
