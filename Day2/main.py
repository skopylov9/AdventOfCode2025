
ranges = open('input.txt').read().split(',')
ranges = [tuple((map(int, r.split('-')))) for r in ranges]

def checkIdPart1(id):
    idstr = str(id)
    idlen = len(idstr)

    if idlen % 2 == 0 and idstr[0 : idlen // 2] == idstr[idlen // 2 : ]:
        return id
    
    return 0

def checkIdPart2ByStr(id):      # By the way, the same time
    idstr = str(id)
    idlen = len(idstr)

    for partSize in range(1, idlen // 2 + 1):
        if idlen % partSize:
            continue
        
        for part in range(1, idlen // partSize):
            if idstr[0 : partSize] != idstr[part * partSize : (part + 1) * partSize]:
                break
        else:
            return id        
    
    return 0

tenMap = [10 ** i for i in range(10)]
def checkIdPart2(id):
    idstr = str(id)
    idlen = len(idstr)

    for partSize in range(1, idlen // 2 + 1):
        if idlen % partSize:
            continue
        
        baseValue = id % tenMap[partSize]
        for part in range(1, idlen // partSize):
            if baseValue != id // tenMap[part * partSize] % tenMap[partSize]:
                break
        else:
            return id        
    
    return 0

print('Part 1:', sum(checkIdPart1(id) for left, right in ranges for id in range(left, right + 1)))   # 19219508902
print('Part 2:', sum(checkIdPart2(id) for left, right in ranges for id in range(left, right + 1)))   # 27180728081
