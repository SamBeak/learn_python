# List, Tuple, Dictionary, Set
# 1. List
arr1 = [1, 2, 3, 4, 5]
tup1 = (1, 2, 3, 4, 5)
dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
set1 = {1, 2, 3, 4, 5}

# array method
# 1. append (맨 뒤에 추가)
arr1.append(6)
print(arr1)
# 2. insert (원하는 위치에 추가) 첫 parameter는 index, 두번째 parameter는 value
arr1.insert(0, 0)
print(arr1)
# 3. extend (리스트를 확장) 첫 parameter는 index, 두번째 parameter는 value, 세번째 parameter는 value
arr1.extend([7, 8, 9])
print(arr1)
# 4. remove (원하는 값을 삭제) 첫 parameter는 value (index가 아님)
arr1.remove(9)
print(arr1)
# 5. pop (맨 뒤의 값을 삭제) 첫 parameter는 index (default는 -1)
arr1.pop()
print(arr1)
# 6. index (원하는 값의 index를 반환) 첫 parameter는 value 5의 인덱스넘버를 반환
print(arr1.index(5))
# 7. count (원하는 값의 개수를 반환) 첫 parameter는 value 5의 갯수를 반환
print(arr1.count(5))
# 8. sort (정렬) parameter로 reverse=True를 넣으면 내림차순으로 정렬 가능 (default는 오름차순)
arr1.sort()
print(arr1)
# sorted (정렬) parameter로 reverse=True를 넣으면 내림차순으로 정렬 가능 (default는 오름차순)
print(sorted(arr1))
# sort()와 sorted는 똑같이 정렬을 하지만 하나는 파괴적 하나는 비파괴적이다. 파괴적은 원본을 바꾸고 비파괴적은 원본을 바꾸지 않는다. sort가 파괴적이고 sorted가 비파괴적이다.
# 중복제거 (set을 이용)
print(list(set(arr1)))
# 중복제거 (dictionary를 이용)
print(list(dict.fromkeys(arr1)))
# 중복제거 (list comprehension을 이용)
print([value for index, value in enumerate(arr1) if value not in arr1[:index]])
# 9. reverse (배열을 역순으로 정렬) parameter로 reverse=True를 넣으면 내림차순으로 정렬 가능 (default는 오름차순)
arr1.reverse()
print(arr1)
# 10. clear (배열을 비움)
arr1.clear()
print(arr1)
# 11. copy (배열을 복사)
arr2 = arr1.copy()
print(arr2)
# 12. len (배열의 길이)
print(len(arr2))
# 13. sum array의 모든 요소의 합 array의 모든 요소가 숫자여야 함 (문자열이 있으면 에러)
print(sum(arr2))
# 14. min array의 모든 요소의 최소값 array의 모든 요소가 숫자여야 함 (문자열이 있으면 에러)
print(min(arr2))
# 15. max array의 모든 요소의 최대값 array의 모든 요소가 숫자여야 함 (문자열이 있으면 에러)
print(max(arr2))
# 16. all (모두 참이면 True, 아니면 False)
print(all(arr2))
# 17. any (하나라도 참이면 True, 아니면 False)
print(any(arr2))
# 18. range (범위를 지정) 첫 parameter는 시작값, 두번째 parameter는 끝값, 세번째 parameter는 증가값
print(list(range(1, 10, 2)))
# 19. enumerate (index와 value를 반환) 첫 parameter는 index, 두번째 parameter는 value (index, value) 형태로 반환 (default는 0부터 시작) 
for index, value in enumerate(arr2):
    print(index, value) # 0 1 1 2 2 3 3 4 4 5
# 20. filter (조건에 맞는 요소만 반환) 첫 parameter는 함수, 두번째 parameter는 배열 (함수의 조건에 맞는 요소만 반환)
def over_3(value):
    return value > 3
print(list(filter(over_3, arr2))) # [4, 5]
# 21. map (요소를 변환) 첫 parameter는 함수, 두번째 parameter는 배열 (함수의 조건에 맞는 요소만 반환)
def double(value):
    return value * 2 # [2, 4, 6, 8, 10]
print(list(map(double, arr2)))
# 22. zip (두 개의 배열을 합쳐서 반환) 첫 parameter는 배열, 두번째 parameter는 배열 (두 배열의 요소를 하나씩 묶어서 반환)
arr3 = [6, 7, 8, 9, 10]
print(list(zip(arr2, arr3))) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# 23. lambda (함수를 간단하게 표현) lambda key: value (key는 parameter, value는 return)
print(list(map(lambda value: value * 2, arr2))) # [2, 4, 6, 8, 10]
# 24. reduce (배열의 요소를 하나씩 함수에 적용하여 하나의 결과를 만듦) 첫 parameter는 함수, 두번째 parameter는 배열 (함수의 조건에 맞는 요소만 반환)
from functools import reduce
def sum_reduce(value1, value2):
    return value1 + value2
print(reduce(sum_reduce, arr2))
# 25. list comprehension (배열을 간단하게 표현)
print([value * 2 for value in arr2])
# 26. dictionary comprehension (딕셔너리를 간단하게 표현)
print({key: value for key, value in dic1.items()})
# 27. set comprehension (셋을 간단하게 표현)
print({value * 2 for value in set1})
# 28. tuple comprehension (튜플을 간단하게 표현)
print(tuple(value * 2 for value in tup1))
# 29. list unpacking (배열을 간단하게 표현)
arr4 = [1, 2, 3, 3, 3]
print(*arr4)
# 30. dictionary unpacking (딕셔너리를 간단하게 표현)
dic2 = {'a': 1, 'b': 2, 'c': 3}
print(*dic2) # a b c
# 31. set unpacking (셋을 간단하게 표현)
set2 = {1, 2, 3}
print(*set2)
# 32. tuple unpacking (튜플을 간단하게 표현)
tup2 = (1, 2, 3)
print(*tup2)
# 33. set Array -> set(array) (배열을 셋으로 변환) 중복된 값은 하나만 남음, 중복 값 제거
print(set(arr4)) # {1, 2, 3}
# 34. dictionary에서 해당 문자 찾기
print(dic1['a']) # 1
# 35. dictionary에서 해당 문자가 없으면 에러가 나지 않고 None을 반환
print(dic1.get('f')) # None
# 중복 제거
# 36. set (중복된 값을 제거)
print(set(arr4)) # {1, 2, 3}