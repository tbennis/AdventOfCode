def find_highest(nr, l):
    substr = nr[:-l+1] if l > 1 else nr
    mx, idx = 0, 0
    for i, c in enumerate(substr):
        if int(c) > mx:
            mx, idx = int(c), i
    return str(mx) + find_highest(nr[idx+1:], l-1) if l > 1 else str(mx)

with open("Input.txt", "r") as f:
    total, total2 = 0, 0
    for line in f:
        line = line.split("\n")[0]
        total += int(find_highest(line, 2))
        total2 += int(find_highest(line, 12))
    print(f"Part 1: {total} - Part 2: {total2}")