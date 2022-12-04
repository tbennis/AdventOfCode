with open('Input2.txt') as f:
    lines = f.read().splitlines()

STATIC_POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

STATIC_OUTCOMES_1 = {
    'A X': 3,
    'B Y': 3,
    'C Z': 3,
    'A Y': 6,
    'B Z': 6,
    'C X': 6,
    'A Z': 0,
    'B X': 0,
    'C Y': 0
}

STATIC_OUTCOMES_2 = {
    'A X': 3,
    'B Y': 5,
    'C Z': 7,
    'A Y': 4,
    'B Z': 9,
    'C X': 2,
    'A Z': 8,
    'B X': 1,
    'C Y': 6
}

total = 0
total_2 = 0
for game in lines:
    total += STATIC_OUTCOMES_1[game]
    total += STATIC_POINTS[game[2]]
    total_2 += STATIC_OUTCOMES_2[game]
print(total)
print(total_2)