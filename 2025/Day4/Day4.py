def get_neighbours(matrix, row_idx, col_idx):
    am_rows = len(matrix)
    am_cols = len(matrix[0])
    neighbours = 0
    if row_idx != 0:
        neighbours += 1 if matrix[row_idx-1][col_idx] == "@" else 0
    if col_idx != 0:
        neighbours += 1 if matrix[row_idx][col_idx-1] == "@" else 0
    if row_idx != am_rows-1:
        neighbours += 1 if matrix[row_idx+1][col_idx] == "@" else 0
    if col_idx != am_cols-1:
        neighbours += 1 if matrix[row_idx][col_idx+1] == "@" else 0
    if row_idx != 0 and col_idx != 0:
        neighbours += 1 if matrix[row_idx-1][col_idx-1] == "@" else 0
    if row_idx != 0 and col_idx != am_cols-1:
        neighbours += 1 if matrix[row_idx-1][col_idx+1] == "@" else 0
    if row_idx != am_rows-1 and col_idx != 0:
        neighbours += 1 if matrix[row_idx+1][col_idx-1] == "@" else 0
    if row_idx != am_rows-1 and col_idx != am_cols-1:
        neighbours += 1 if matrix[row_idx+1][col_idx+1] == "@" else 0
    return neighbours

with open("Input.txt", "r") as f:
    matrix = []
    for line in f:
        line = line.split("\n")[0]
        matrix.append(list(line))
    new_matrix = [["."] * len(matrix[0]) for _ in range(len(matrix))]
    total = 0
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == ".":
                continue
            if get_neighbours(matrix, row_idx, col_idx) < 4:
                total+=1
            else:
                new_matrix[row_idx][col_idx] = "@"
    print(total)

    done = False
    matrix = new_matrix.copy()
    new_matrix = [["."] * len(matrix[0]) for _ in range(len(matrix))]
    while not done:
        additions = 0
        for row_idx, row in enumerate(matrix):
            for col_idx, value in enumerate(row):
                if value == ".":
                    continue
                if get_neighbours(matrix, row_idx, col_idx) < 4:
                    total+=1
                    additions +=1
                else:
                    new_matrix[row_idx][col_idx] = "@"
        if additions == 0:
            done = True
        else:
            matrix = new_matrix.copy()
            new_matrix = [["."] * len(matrix[0]) for _ in range(len(matrix))]
    print(total)

        
