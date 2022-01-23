def countNonRepeating(inputStr):
    resSeen = []
    resUnseen = []

    for ele in inputStr:
        if ele in resUnseen:
            resSeen.append(ele)
            resUnseen.remove(ele)
        elif ele in resSeen:
            continue
        else:
            resUnseen.append(ele)
    if resUnseen:
        return inputStr.find(resUnseen[0])
    else:
        return -1

for _ in range(int(input())):
    print(countNonRepeating(input()))