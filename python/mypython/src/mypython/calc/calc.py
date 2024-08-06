def multiplyer(by: int):
    return lambda x: by * x


def adder(start: int):
    return lambda x: start + x


def subtraction(start: int):
    return lambda x: start - x


def division(start: int):
    return lambda x: start / x
