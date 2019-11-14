def eliminate_zeros(numbers):
    return list(filter(lambda n: n != 0, numbers))
    # return [i for i in numbers if i != 0]
