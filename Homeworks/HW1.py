oddList = list(range(1,10,2))
evenList = list(range(0,9,2))

theList = oddList + evenList
theList.sort()

a = 0

for i in theList:
    theList[a] = theList[a] * 2
    print(theList[a])
    a += 1