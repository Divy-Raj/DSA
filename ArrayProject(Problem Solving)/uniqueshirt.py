def getUnique(arr):
    resDict = {}
    for ele in arr:
        if ele in resDict:
            resDict[ele] += 1
        else:
            resDict[ele] = 1

    print(len([ele for ele in resDict if resDict[ele]==1]))
# The upper line code is about creating different array traversing through it and giving it unique value
# You can also write code given below in comment
#arrTemp = []
#for ele in resDict:
#   if resDict[ele] == 1:
#      arrTemp.append(ele)

count = input()
arr = [int(ele) for ele in input().split(" ")]
# This could be rewritten as given below
# arr = list(map(int,input().split())
# for ele in range (len(arr)):
getUnique(arr)