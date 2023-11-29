# 튜플이란? 변경할 수 없는 시퀀스 자료형(나머지는 리스트와 동일)
# 튜플의 정의 ()괄호를 사용하거나 생략 할 수 있음

# person = "곰돌이사육사" # 튜플이 아님
# print(person)

# person = "곰돌이사육사", # 튜플이 맞음/ ,로 판단
# print(person)

# 튜플 만들기
person = "곰돌이사육사", 20, "서울시 강남구 역삼동"
print(person)

# 튜플 요소 접근하기
print(person[0])
print(person[1])

# 튜플의 언패킹 : 묶인 걸 푸는 것
이름, 나이, 주소 = person
print(이름)
print(나이)
print(주소)

# 튜플의 언패킹 기능을 이용한 함수 만들기
def get_person() :
    name = "가을"
    age = 23
    addr = "서울시 강남구 역삼동"
    return name,age,addr

result = get_person() # 언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a,b,c = get_person()
print(a)
print(b)
print(c)

# 튜플 객체
tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3)) # 매개변수로 전달한 변수가 몇번 나오는지 확인 하는 함수

# 튜플에서 안 되는 것(이뮤터블 특성이기 때문에 삭제 할 수 없음/ 읽기만 가능해서 수정,삭제 불가)
#del_tp[0]

# 인덱싱
print(tp.index(2)) # 매개변수로 전달한 변수의 시작 인덱스를 반환

# 길이
print(len(tp))


# 집합
# 집합이란? 주로 중복 제거를 목적으로 자주 사용
# 순서가 보장 되지 않음
# 중복 불가
# mutable 특성을 가짐
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 요소의 중복 제거
s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
print(s3)

# 합집합 : 집합에서 한군데만 존재하면 포함됨, 중복 제거
print(s1.union(s2))
print(s1 | s2)

# 교집합 : 집합에서 양쪽 모두에 존재하는 요소만 선택
print(s1.intersection(s2))
print(s1 & s2)

# 차집합 : 집합에서 앞에서 뒤를 빼서 남은 앞의 요소만 선택
print(s1.difference(s2))
print(s1 - s2)

# 중복 제거 로또 번호 만들기
import random
nums = set()
while True :
    num = random.randrange(1,46)
    nums.add(num)
    if len(nums) == 6: break
    print(nums)