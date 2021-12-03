import numpy as np

def to_string(array):
    string = ''
    for entry in array:
        string += str(int(entry))
    return string

def most_common(array, index):
    ones = 0
    for number in array:
        if int(number[index]) == 1:
            ones += 1
    if ones >= len(array)/2:
        return [number for number in array if int(number[index]) == 1]
    else:
        return [number for number in array if int(number[index]) == 0]

def least_common(array, index):
    ones = 0
    for number in array:
        if int(number[index]) == 1:
            ones += 1
    if ones < len(array)/2:
        return [number for number in array if int(number[index]) == 1]
    else:
        return [number for number in array if int(number[index]) == 0]

with open('Input3.txt') as f:
    lines = f.read().splitlines()

# Part 1
ones = np.zeros(len(lines[0]))
for line in lines:
    ones += [int(i) for i in line]
zeros = np.ones(len(lines[0]))*len(lines) - ones
gamma = ones-zeros
gamma[gamma<0] = 0
gamma[gamma>0] = 1
epsilon = zeros-ones
epsilon[epsilon<0] = 0
epsilon[epsilon>0] = 1
print(int(to_string(gamma),2)*int(to_string(epsilon),2))

# Part 2
mc = lines
lc = lines 
index_mc = 0
index_lc = 0
while len(mc) > 1:
    mc = most_common(mc, index_mc)
    index_mc += 1
while len(lc) > 1:
    lc = least_common(lc, index_lc)
    index_lc += 1
print(int(mc[0],2)*int(lc[0],2))