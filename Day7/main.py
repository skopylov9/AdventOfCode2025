import operator
import functools

manifold = [list(line) for line in open('input.txt').read().splitlines()]
manifold = [[{'^':-1, '.':0, 'S':1}[c] for c in line] for line in manifold]

splitCount = 0
for i in range(1, len(manifold)):
    for j in range(len(manifold[i])):
        if manifold[i][j] == -1 and manifold[i - 1][j] > 0:
            splitCount += 1
            manifold[i][j - 1] += manifold[i - 1][j]
            manifold[i][j + 1] += manifold[i - 1][j]
        elif manifold[i][j] >= 0 and manifold[i - 1][j] > 0:
            manifold[i][j] += manifold[i - 1][j]

print('Part 1:', splitCount)        # 1587
print('Part 2:', sum(manifold[-1])) # 5748679033029
