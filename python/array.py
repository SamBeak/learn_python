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