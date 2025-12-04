lines = open('input.txt').read().splitlines()
helpful_diagram = [list(line) for line in lines]

def readyToRemove(helpful_diagram, x, y):
    count = 0
    for dx, dy in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
        if x + dx not in range(len(helpful_diagram)):
            continue
        if y + dy not in range(len(helpful_diagram[x])):
            continue
        if helpful_diagram[x + dx][y + dy] != '@':
            continue
        count += 1
    return count < 4

def getRolls(helpful_diagram):
    return [(x, y) for x in range(len(helpful_diagram)) for y in range(len(helpful_diagram[x])) if helpful_diagram[x][y] == '@']

def removeRolls(helpful_diagram):
    toRemove = []
    for x, y in getRolls(helpful_diagram):
        if readyToRemove(helpful_diagram, x, y):
            toRemove.append((x, y))
    
    for x, y in toRemove:
        helpful_diagram[x][y] = '.'
    
    return len(toRemove)

removedCount = removeRolls(helpful_diagram)
accessedRollsOne = removedCount
accessedRollsTotal = removedCount
while removedCount:
    removedCount = removeRolls(helpful_diagram)
    accessedRollsTotal += removedCount

print('Part 1:', accessedRollsOne)      # 1549
print('Part 2:', accessedRollsTotal)    # 8887
