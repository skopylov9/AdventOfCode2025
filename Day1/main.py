
lines = open('input.txt').read().splitlines()

rotations = [int(line[1:]) * (1 if line[0] == 'R' else -1) for line in lines]

# dial = 50
# dials = [50]
# for rotation in rotations:
#     dial = (dial + rotation) % 100
#     dials.append(dial)
# How to create dials in one line???

# toZeroDialDst = [dials[i] if rotations[i] < 0 else 100 - dials[i] for i in range(len(rotations))]
# inZeroCount = sum([1 if dial == 0 else 0 for dial in dials])
# overZeroCount = sum([(1 if abs(rotation) % 100 > toZeroDst and toZeroDst else 0) + abs(rotation) // 100 for toZeroDst, rotation in zip(toZeroDialDst, rotations)])

dial = 50
inZeroCount = 0
overZeroCount = 0
for rotation in rotations:
    toZeroDialDst = dial if rotation < 0 else 100 - dial
    
    dial = (dial + rotation) % 100

    inZeroCount += 1 if dial == 0 else 0
    overZeroCount += (1 if abs(rotation) % 100 > toZeroDialDst and toZeroDialDst else 0) + abs(rotation) // 100
        
print('Part 1:', inZeroCount)                   # 984
print('Part 2:', inZeroCount + overZeroCount)   # 5657
