import operator
import functools
import math

boxes = [tuple(map(int, line.split(','))) for line in open('input.txt').read().splitlines()]

connections = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        connections.append((i, j, math.sqrt(pow(boxes[i][0] - boxes[j][0], 2) + pow(boxes[i][1] - boxes[j][1], 2) + pow(boxes[i][2] - boxes[j][2], 2))))
connections.sort(key=lambda v: v[2])

circuits = {i : set([i]) for i, box in enumerate(boxes)}
boxesToCircuitsId = [i for i in range(len(boxes))]

connectCount = 0
for connect in connections:
    connectCount += 1
    srcBoxId, trgtBoxId = connect[0], connect[1]
    if boxesToCircuitsId[srcBoxId] == boxesToCircuitsId[trgtBoxId]:
        continue
    
    srcBoxCircuitsId, trgtBoxCircuitsId = boxesToCircuitsId[srcBoxId], boxesToCircuitsId[trgtBoxId]
    circuits[srcBoxCircuitsId] = circuits[srcBoxCircuitsId].union(circuits[trgtBoxCircuitsId])

    mergedCircuits = circuits.pop(trgtBoxCircuitsId)
    for boxId in mergedCircuits:
        boxesToCircuitsId[boxId] = srcBoxCircuitsId

    if connectCount == 1000:
        circuitSizes = [len(circuit) for circuit in circuits.values()]
        circuitSizes.sort()
        print('Part 1:', functools.reduce(operator.mul, circuitSizes[-3:], 1))  # 123420

    if len(circuits) == 1:
        print('Part 2:', boxes[srcBoxId][0] * boxes[trgtBoxId][0]) # 673096646



