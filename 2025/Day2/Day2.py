def is_invalid_id(i):
    l = len(i)
    if l%2==1:
        return False
    st = i[:int(l/2)]
    en = i[int(l/2):]
    if st == en:
        return True

def is_invalid_id_2(i):
    l = len(i)
    for j in range(l-1):
        if l%(j+1) == 0:
            lst = [i[k:k+j+1] for k in range(0, l, j+1)]
            if all(x == lst[0] for x in lst):
                return True
    return False

with open("Input.txt", "r") as f:
    for line in f:
        ranges = line.split(",")

        sol1 = 0
        sol2 = 0

        for r in ranges:
            spl = r.split("-")
            st = spl[0]
            en = spl[1]
            for i in range(int(st), int(en)+1):
                if is_invalid_id(str(i)):
                    sol1 += i
                if is_invalid_id_2(str(i)):
                    sol2 += i
        print(sol1)
        print(sol2)

