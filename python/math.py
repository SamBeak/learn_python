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
# 20. 약수 구하기
def divisor_fundamental(num1):
    divisor = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisor.append(i)
    return divisor
# 21. 소수 구하기
def prime_number_fundamental(num1):
    prime_number = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            prime_number.append(i)
    if len(prime_number) == 2:
        return True
    else:
        return False
# 22. 약수 개수 구하기
def divisor_count_fundamental(num1):
    divisor_count = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisor_count += 1
    return divisor_count
# 23. 소수 개수 구하기
def prime_number_count_fundamental(num1):
    prime_number_count = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            prime_number_count += 1
    if prime_number_count == 2:
        return True
    else:
        return False
# 24. 소인수분해
def prime_factorization_fundamental(num1):
    prime_factorization = []
    for i in range(2, num1 + 1):
        if num1 % i == 0:
            prime_factorization.append(i)
            num1 = num1 // i
            i = 1
    return prime_factorization
# 25. 이진수 변환
def binary_fundamental(num1):
    binary = bin(num1)
    return binary
# 26. 8진수 변환
def octal_fundamental(num1):
    octal = oct(num1)
    return octal
# 27. 16진수 변환
def hexadecimal_fundamental(num1):
    hexadecimal = hex(num1)
    return hexadecimal