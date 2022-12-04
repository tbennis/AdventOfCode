with open('Input4.txt') as f:
    lines = f.read().splitlines()

answer = 0
answer2 = 0
for line in lines:
    pairs = line.split(',')
    [min1, max1] = pairs[0].split('-')
    [min2, max2] = pairs[1].split('-')
    min1 = int(min1)
    min2 = int(min2)
    max1 = int(max1)
    max2 = int(max2)
    if (min1 >= min2 and max1 <= max2) or (min2 >= min1 and max2 <= max1):
        answer += 1
    if (min1 <= max2 <= max1) or (min2 <= max1 <= max2):
        answer2 += 1
print(answer)
print(answer2)