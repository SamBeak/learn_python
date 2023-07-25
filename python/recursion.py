# 재귀함수 사용
def remainder_fundamental(num1, num2):
    if num1 < num2:
        return num1
    else:
        return remainder_fundamental(num1 - num2, num2)
# 재귀함수 사용
def gcd_fundamental(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd_fundamental(num2, num1 % num2)

# >> 비트연산자 설명 : https://dojang.io/mod/page/view.php?id=2460
# a >> b a의 비트를 b번 이동시킴 (오른쪽으로 이동)
# >> 비트시프트 사용
# 1. 왼쪽으로 1비트 이동
def left_shift_fundamental(num1):
    left_shift = num1 << 1
    return left_shift
# 2. 오른쪽으로 1비트 이동
def right_shift_fundamental(num1):
    right_shift = num1 >> 1
    return right_shift
# 3. 비트 논리곱
def bit_and_fundamental(num1, num2):
    bit_and = num1 & num2
    return bit_and
# 4. 비트 논리합
def bit_or_fundamental(num1, num2):
    bit_or = num1 | num2
    return bit_or
# 5. 비트 배타적 논리합
def bit_xor_fundamental(num1, num2):
    bit_xor = num1 ^ num2
    return bit_xor
# 6. 비트 논리부정
def bit_not_fundamental(num1):
    bit_not = ~num1
    return bit_not

