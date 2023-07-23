#  반복문에서 print 줄바꿈 없애기 (end="") 사용 (default는 end="\n") 
for i in range(10):
    print(i, end=" ")
print()
#  반복문에서 index와 value를 같이 출력하기
for index, value in enumerate(range(10)):
    print(index, value) # 0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9
#  반복문에서 index와 value를 같이 출력하기 (index는 1부터 시작)
for index, value in enumerate(range(10), 1):
    print(index, value) # 1 0 2 1 3 2 4 3 5 4 6 5 7 6 8 7 9 8 10 9
#  반복문에서 index와 value를 같이 출력하기 (index는 1부터 시작, index와 value를 묶어서 출력)
for index, value in enumerate(range(10), 1):
    print(index, value, sep=":") # 1:0 2:1 3:2 4:3 5:4 6:5 7:6 8:7 9:8 10:9
# 반복문에서 index와 value를 같이 출력하기 (index는 1부터 시작, index와 value를 묶어서 출력, value는 문자열로 변환)
for index, value in enumerate(range(10), 1):
    print(index, str(value), sep=":") # 1:0 2:1 3:2 4:3 5:4 6:5 7:6 8:7 9:8 10:9
# printf"" % (value1, value2, ...) 사용
print("%d %d" % (1, 2)) # 1 2
# format(value1, value2, ...) 사용
print("{} {}".format(1, 2)) # 1 2
# f-string 사용
print(f"{1} {2}") # 1 2
# f"" 변수 사용
a = 1
print(f"{a}") # 1