#!/usr/bin/python
# def greet(name: str) -> str:
#     return f"Hello {name}"


# def my_sum(a: int, b: int) -> int:
#     return a + b


from mypython.calc import calc


def main():
    _two_multiplayer = calc.multiplyer(2)
    _add_five = calc.adder(5)
    _two_division = calc.division(2)

    def multiply_by_two(num: int) -> int:
        return _two_multiplayer(num)

    def start_by_five(num: int) -> int:
        return _add_five(num)

    def _divide_by_two(num: int) -> int:
        return _two_division(num)

    a = multiply_by_two(1)
    print(a)
