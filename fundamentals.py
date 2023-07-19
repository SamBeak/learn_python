import math

# 1. 덧셈
def plus_fundamental(num1, num2):
    plus = num1 + num2
    return plus
# 2. 뺄셈
def minus_fundamental(num1, num2):
    minus = num1 - num2
    return minus
# 3. 곱셈
def multiply_fundamental(num1, num2):
    multiply = num1 * num2
    return multiply
# 4. 나눗셈
def divide_fundamental(num1, num2):
    divide = num1 / num2
    return divide
# 5. 몫만 구하기
def quotient_fundamental(num1, num2):
    quotient = num1 // num2
    return quotient
# 6. 나머지만 구하기
def remainder_fundamental(num1, num2):
    remainder = num1 % num2
    return remainder
# 7. 거듭제곱 구하기
def power_fundamental(num1, num2):
    power = num1 ** num2
    return power
# 8. 제곱근 구하기
def square_root_fundamental(num1):
    square_root = num1 ** 0.5
    return square_root
# 9. 절댓값 구하기
def absolute_fundamental(num1):
    absolute = abs(num1)
    return absolute
# 10. 반올림 구하기
def round_fundamental(num1):
    round = round(num1)
    return round
# 11. 올림 구하기
def ceil_fundamental(num1):
    ceil = math.ceil(num1)
    return ceil
# 12. 내림 구하기
def floor_fundamental(num1):
    floor = math.floor(num1)
    return floor