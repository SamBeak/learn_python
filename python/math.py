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
# 13. 최대공약수 구하기
def gcd_fundamental(num1, num2):
    gcd = math.gcd(num1, num2)
    return gcd
# 14. 최소공배수 구하기
def lcm_fundamental(num1, num2):
    lcm = num1 * num2 // math.gcd(num1, num2)
    return lcm
# 15. 컴비네이션
def combination_fundamental(num1, num2):
    combination = math.comb(num1, num2)
    return combination
# 16. 팩토리얼
def factorial_fundamental(num1):
    factorial = math.factorial(num1)
    return factorial
# 17. 로그
def log_fundamental(num1, num2):
    log = math.log(num1, num2)
    return log
# 18. 제곱근
def sqrt_fundamental(num1):
    sqrt = math.sqrt(num1)
    return sqrt
# 19. 루트
def root_fundamental(num1, num2):
    root = num1 ** (1 / num2)
    return root