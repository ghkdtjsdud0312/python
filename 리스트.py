# 리스트
# 크기가 정해져 있지 않다.
# 아무 자료형이나 와도 상관없다.
# 중첩 사용이 가능하다.
# 뮤터블 객체 : 읽고 쓰기 가능

# 변수와 리스트를 비교 해보기
# kor,eng,mat = map(int, input("성적 입력 : ").split())
# print(sum([kor,eng,mat]))
#
# # 리스트는 성적의 개수에 상관없이 입력 받을 수 있음
# score = list(map(int, input("성적 입력 : ").split()))
# print(sum(score)/len(score))

# # 인덱싱
# str_name = ["seoul","gangnam","suwon","inchon"]
# print(str_name)
# print(str_name[1])
# print(str_name[1][2])
#
# # 슬라이싱 : 자르는 것
# slice = str_name[1:3]
# print(slice)
# print(len(slice))
# print(len(slice[0]))

# # prime(소수)
# prime = [2,3,5,7]
# print(prime[0]) # 2
# print(prime[-1]) # 7
# print(prime[-2:]) # 5,7

# 리스트 연산자 : 연결(+), 반복(*), len()- 문자열 개수
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a + list_b)
# print(list_a * 3)
# print(len(list_a + list_b)) # 6

# 리스트 제거하기 : pop(), remove(), clear(), del 리스명[인덱스]
# pop() : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제, 인덱스가 있으면 해당 위치의 값을 삭제
# remove(값) : 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우 낮은 인덱스값 제거
# clear() : 모든 값을 삭제, 리스트 지우지 않음
# list_all= [0,1,2,3,4,5,6,7,8,9, 0,1,2,3,4, "a","b","c","d","korea"]
# print(list_all)
# print(list_all.pop(11)) # 해당 인덱스의 값을 삭제하면서 보여줌
# print(list_all.pop()) # pop() 인덱스가 없으면 맨 마지막에 값 제거
# list_all.remove(2) # 해당값을 제거하는데 보여주지 않음(반환값이 없음)
# print(list_all)
#
# del list_all[3] # 해당 인덱스의 값을 지움
# print(list_all)
#
# list_all.clear()
# print(list_all)

# 중복 제거
# my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,1,2,3,4]
# new_list = []
# for e in my_list:
#     if e not in new_list:
#         new_list.append(e)
# print(new_list)

# int()
# # map(반환함수, 입력자료형), filter(반환함수, 입력자료형) 동작 확인
# num = list(filter(lambda e: int(e)*int(e), input("값 :").split()))
# print(num)
#
# num = list(filter(lambda e: (int)(e) % 2 == 0, input("값 :").split()))
# print(num)

# # 리스트의 원소 스캔하기
# x= ["John", "George", "Paul", "Ringo"]
# for e in x: # 향상된 for문과 비슷한 형태
#     print(e)
#
# for i in range(len(x)): # 범위 기반 for문(초기값, 최종값, 증감값)
#     print(x[i])

# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제
num = list(map(int, input("입력 : ").split()))
odd = []
even = []
for e in num:
    if e % 2 == 0: even.append(e)
    else: odd.append(e)
print(f"홀수 : {odd}")
print(f"짝수 : {even}")

# filter 내장 함수와 lambda를 이용한 방법
num = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda e: e % 2 == 1, num))
even = list(filter(lambda e : e % 2 == 0,num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")




