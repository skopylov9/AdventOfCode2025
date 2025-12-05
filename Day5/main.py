
freshIdRangeList, idList = (inputStr.splitlines() for inputStr in open('input.txt').read().split('\n\n'))
freshIdRangeList = [tuple(map(int, idRange.split('-'))) for idRange in freshIdRangeList]
idList = list(map(int, idList))

freshIdRangeList = sorted(freshIdRangeList)

i = len(freshIdRangeList)
while i >= 0:
    if (i + 1 < len(freshIdRangeList)) and (freshIdRangeList[i][1] >= freshIdRangeList[i + 1][0]):
        freshIdRangeList[i] = (freshIdRangeList[i][0], max(freshIdRangeList[i][1], freshIdRangeList[i + 1][1]))
        freshIdRangeList.pop(i + 1)
    else:
        i -= 1

freshCount = sum(1 if any(id in range(idRange[0], idRange[1] + 1) for idRange in freshIdRangeList) else 0 for id in idList)
totalFreshCount = sum(right - left + 1 for left, right in freshIdRangeList)

print('Part 1:', freshCount)        # 775
print('Part 2:', totalFreshCount)   # 350684792662845
