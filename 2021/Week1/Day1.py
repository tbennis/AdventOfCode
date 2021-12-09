with open('Input1.txt') as f:
    lines = f.read().splitlines()
lines = [int(line) for line in lines]
ltp = 0
for i in range(len(lines)-1):
    if lines[i+1] > lines[i]:
        ltp += 1
print(ltp)

ltps = 0
for j in range(len(lines)-3):
    if lines[j+3] > lines[j]:
        ltps += 1
print(ltps)
