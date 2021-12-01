def sum_of_square(x):
    y = 0
    for i in range(1, x+1):
        y += i*i
    return y

def square_of_sum(x):
    y = 0
    for i in range(1, x+1):
        y += i
    return y*y