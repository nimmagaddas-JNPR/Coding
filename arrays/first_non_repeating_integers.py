# First non-repeating integers in an array
# Eg: [3,4,5,0,3,4,5,6,8,7,4,5,6,7] o/p: 2

def findNonRepeating(arr):
  mappings = {}
  for ele in arr:
    if(ele in mappings):
      mappings[ele] = mappings[ele] + 1
    else:
      mappings[ele] = 1
  for j in mappings:
    if(mappings[j] == 1):
      return j

print(findNonRepeating([3,4,5,3,4,5,6,8,7,4,5,6,7]))
print(findNonRepeating([3,4,5,3,4,5,-6,8,7,4,5,6,7]))
