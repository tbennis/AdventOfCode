with open('Input6.txt') as f:
    source = f.read()

def progressDay(fishCount, days):
    for j in range(days):
        newFish = fishCount[0]
        for i in range(8):
            fishCount[i] = fishCount[i+1]
        fishCount[8] = newFish
        fishCount[6] += newFish
    return fishCount    

fishList = [int(i) for i in source.split(',')]
fishCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in fishList:
    fishCount[i] += 1
fishCount = progressDay(fishCount, 80)
print(sum(fishCount))
print(sum(progressDay(fishCount, 176)))