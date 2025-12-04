
banks = open('input.txt').read().splitlines()
banks = [tuple(map(int, list(bank))) for bank in banks]

def maxJoltage(bank, depth):
    if depth == 1:
        return max(bank) 
    leftVal = max(bank[:-depth + 1])
    return leftVal * (10 ** (depth - 1)) + maxJoltage(bank[bank.index(leftVal) + 1:], depth - 1)

print('Part 1:', sum(maxJoltage(bank, 2) for bank in banks))    # 17332
print('Part 2:', sum(maxJoltage(bank, 12) for bank in banks))   # 172516781546707
