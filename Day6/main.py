import operator
import functools

inputStr = open('input.txt').read().splitlines()

operations = list(filter(None, inputStr[-1].split(' ')))
numbersPart1 = [list(map(int, filter(None, numberLine.split(' ')))) for numberLine in inputStr[:-1]]
numbersPart1 = list(list(n) for n in zip(*numbersPart1))[::-1]
numbersPart1.reverse()

numbersPart2 = list(''.join(list(s)[:-1]).strip() for s in zip(*inputStr))[::-1]
numbersPart2 = [list(map(int, n.split('\n'))) for n in '\n'.join(numbersPart2).split('\n\n')]
numbersPart2.reverse()

def calcSum(numbers, op):
    msum = sum(functools.reduce(operator.mul, n, 1) for o, n in zip(op, numbers) if o == '*')
    asum = sum(functools.reduce(operator.add, n, 0) for o, n in zip(op, numbers) if o == '+')
    return msum + asum

print('Part 1:', calcSum(numbersPart1, operations)) # 4719804927602
print('Part 2:', calcSum(numbersPart2, operations)) # 9608327000261
