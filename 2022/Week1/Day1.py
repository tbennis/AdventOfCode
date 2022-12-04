with open('Input1.txt') as f:
    lines = f.read().splitlines()

caloryList = []
currentCalories = 0

for amount in lines:
    if amount == '':
        caloryList.append(currentCalories)
        currentCalories = 0
    else:
        currentCalories += int(amount)

print(max(caloryList))
caloryList.sort(reverse=True)
print(caloryList[0]+caloryList[1]+caloryList[2])