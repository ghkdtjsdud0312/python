# 내장 함수
num = list(map(int, input("정수값 입력 : ").split()))
print(f"최대값 : {max(num)}")
print(f"최소값 : {min(num)}")
print(f"합계 : {sum(num)}")
print(f"총점 : {sum(num)/len(num)}")
print(f"몫과 나머지 : {divmod(sum(num),5)}")

# 정렬
my_list = [1,2,3,4,54,65,6,77,777,88,99,100]
print(sorted(my_list, reverse=True)) # 내림차순
print(sorted(my_list)) # 오름차순

# 외장 함수
import random

for i in range(100):
        rand = random.randint(0,4) # 0~4이하
        print(rand)
for i in range(100):
        rand = random.randrange(0,4) # 0~4미만
        print(rand)

# 외장 함수 - 현재 시간
from datetime import datetime
print(datetime.today())
print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100.1)) # 무조건 올림
print(math.floor(100.9999)) # 무조건 내림

# 중복 값이 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = []
while True:
    rand = random.randrange(1,46)
    if rand not in ls:
        ls.append(rand)
    if len(ls) == 6: break
print(ls)

