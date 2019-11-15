def eliminate_zeros(numbers):
    numbers[:] = [i for i in numbers if i != 0]
