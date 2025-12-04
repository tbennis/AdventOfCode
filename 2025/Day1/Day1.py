count = 0
loc = 50

with open("Input.txt", "r") as f:
    for line in f:
        dir = 1 if line[0] == "R" else -1
        steps = int(line[1:])
        for _ in range(steps):
            if dir == 1:
                loc = (loc+1)%100
                if loc==0:
                    count+=1
            else:
                loc = (loc-1)%100
                if loc==0:
                    count+=1

print(count)

