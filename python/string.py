# 문자열 메서드
my_string = "hello world"
# 1. capitalize (첫 글자를 대문자로 변환)
print(my_string.capitalize()) # Hello world
# 2. title (각 단어의 첫 글자를 대문자로 변환)
print(my_string.title()) # Hello World
# 3. upper (모든 글자를 대문자로 변환)
print(my_string.upper()) # HELLO WORLD
# 4. lower (모든 글자를 소문자로 변환)
print(my_string.lower()) # hello world
# 5. swapcase (대문자는 소문자로, 소문자는 대문자로 변환)
print(my_string.swapcase()) # HELLO WORLD
# 6. strip (양쪽 공백을 제거)
print(my_string.strip()) # hello world
# 7. lstrip (왼쪽 공백을 제거)
print(my_string.lstrip()) # hello world
# 8. rstrip (오른쪽 공백을 제거)
print(my_string.rstrip()) # hello world
# 9. replace (문자열을 치환) 첫 parameter는 문자열, 두번째 parameter는 치환할 문자열 (치환할 문자열을 치환)
print(my_string.replace("hello", "hi")) # hi world
# 10. split (문자열을 나누어 배열로 반환) 첫 parameter는 구분자 (구분자로 문자열을 나누어 배열로 반환)
print(my_string.split()) # ['hello', 'world']
# 11. join (배열을 문자열로 변환) 첫 parameter는 배열, 두번째 parameter는 구분자 (배열의 요소를 구분자로 합쳐서 문자열로 반환)
print(" ".join(my_string)) # h e l l o   w o r l d
# 12. startswith (문자열이 특정 문자로 시작하는지 확인) 첫 parameter는 문자열, 두번째 parameter는 시작 문자열 (시작 문자열로 시작하면 True, 아니면 False)
print(my_string.startswith("hello")) # True
# 13. endswith (문자열이 특정 문자로 끝나는지 확인) 첫 parameter는 문자열, 두번째 parameter는 끝 문자열 (끝 문자열로 끝나면 True, 아니면 False)
print(my_string.endswith("world")) # True
# 14. find (문자열이 특정 문자를 찾아서 index를 반환) 첫 parameter는 문자열, 두번째 parameter는 찾을 문자열 (찾을 문자열이 있으면 index를 반환, 없으면 -1을 반환)
print(my_string.find("world")) # 6 인덱스가 6인 이유는 공백도 인덱스로 치기 때문에 hello world에서 w의 인덱스는 6이다.
# 15. index (문자열이 특정 문자를 찾아서 index를 반환) 첫 parameter는 문자열, 두번째 parameter는 찾을 문자열 (찾을 문자열이 있으면 index를 반환, 없으면 에러)
print(my_string.index("world")) # 6 인덱스가 6인 이유는 공백도 인덱스로 치기 때문에 hello world에서 w의 인덱스는 6이다.
# 16. count (문자열이 특정 문자의 개수를 반환) 첫 parameter는 문자열, 두번째 parameter는 찾을 문자열 (찾을 문자열의 개수를 반환)
print(my_string.count("l")) # 3
# 17. isalpha (문자열이 문자로만 이루어져 있는지 확인) 문자열이 문자로만 이루어져 있으면 True, 아니면 False
print(my_string.isalpha()) # False
# 18. isdigit (문자열이 숫자로만 이루어져 있는지 확인) 문자열이 숫자로만 이루어져 있으면 True, 아니면 False
print(my_string.isdigit()) # False
# 19. isalnum (문자열이 문자와 숫자로만 이루어져 있는지 확인) 문자열이 문자와 숫자로만 이루어져 있으면 True, 아니면 False
print(my_string.isalnum()) # False
# 20. isspace (문자열이 공백으로만 이루어져 있는지 확인) 문자열이 공백으로만 이루어져 있으면 True, 아니면 False
print(my_string.isspace()) # False
# 21. center (문자열을 특정 길이로 만들고 문자열을 가운데 정렬) 첫 parameter는 길이, 두번째 parameter는 문자열 (문자열을 가운데 정렬하고 길이를 맞춤)
print(my_string.center(20, "*")) # *****hello world*****
# 22. [::-1] (문자열을 역순으로 만듦)
print(my_string[::-1]) # dlrow olleh
# 23. [::2] (문자열을 2칸씩 건너뛰면서 만듦)
print(my_string[::2]) # hlowrd
# 24. [1:3] (문자열을 1부터 3까지 만듦)
print(my_string[1:3]) # el
# 25. [1:] (문자열을 1부터 끝까지 만듦)
print(my_string[1:]) # ello world
# 26. [:-1] (문자열을 처음부터 끝까지 만듦)
print(my_string[:-1]) # hello worl
# 27. 특정 문자열 찾아서 제거
print(my_string.replace("hello", "")) # world
# 28. 반복문 안에서 한글자씩 추가
my_string = ""
for i in range(10):
    my_string += str(i)
print(my_string) # 0123456789
# 29. 숫자를 영문자로 변환
print(chr(65)) # A
# 30. 영문자를 숫자로 변환
print(ord("A")) # 65