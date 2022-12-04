with open('Input3.txt') as f:
    lines = f.read().splitlines()

priority = 0
for rucksack in lines:
    compartments = [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]
    mistake = set(compartments[0]).intersection(compartments[1])
    for item in mistake:
        if ord(item) >= 97:
            priority += ord(item) - 96
        else:
            priority += ord(item) - 38
print(priority)

line1 = ''
line2 = ''
priority = 0
for rucksack in lines:
    if line1 == '': 
        line1 = rucksack
        continue
    elif line2 == '':
        line2 = rucksack
        continue
    else:
        badge = set(line1).intersection(line2).intersection(rucksack)
        line1 = ''
        line2 = ''
    for item in badge:
        if ord(item) >= 97:
            priority += ord(item) - 96
        else:
            priority += ord(item) - 38  
print(priority)