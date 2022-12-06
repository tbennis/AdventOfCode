with open('Input6.txt') as f:
    datastream = f.read().splitlines()[0]

result1 = 0
for i in range(len(datastream)):
    if i <= 2:
        continue
    four = datastream[i-3:i+1]
    if i>=13:
        fourteen = datastream[i-13:i+1]
    if result1 == 0 and len(set(four)) == 4:
        result1 = i+1
    if result1 != 0 and len(set(fourteen)) == 14:
        result2 = i+1
        break
print(result1)
print(result2)      