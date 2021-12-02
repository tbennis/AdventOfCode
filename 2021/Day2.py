with open('Input2.txt') as f:
    lines = f.read().splitlines()
p1 = d1 = 0
a2 = p2 = d2 = 0
for line in lines:
    dir = line.split(' ')[0]
    dist = int(line.split(' ')[1])
    if dir == 'forward':
        p1 += dist
        p2 += dist
        d2 += a2*dist
    elif dir == 'down':
        d1 += dist
        a2 += dist
    else:
        d1 -= dist
        a2 -= dist
print(p1*d1)
print(d2*p2)