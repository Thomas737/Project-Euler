

def sum_of_squares(value: int):
    total = 0
    for n in range(1, value+1):
        total += n**2
    return total

def square_of_sum(value: int):
    total = 0
    for n in range(1, value+1):
        total += n
    return total ** 2

print(square_of_sum(100)-sum_of_squares(100))