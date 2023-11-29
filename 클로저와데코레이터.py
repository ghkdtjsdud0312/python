# 클로저 : 함수 안에 내부 함수를 구현하고 그 내부 함수를 반환하는 함수
# 콜백 함수를 사용하기 위해서도 호출 함
def calc() :
    a = 3 # 데이터 은닉 특성
    b = 5
    def mul_add(x) :
        return a * x + b
    return mul_add # 내부 함수를 리턴

c = calc()
print(c(1), c(2), c(3)) # 외부 함수의 변수의 값을 기억하고 있음

import time
def operation(x, y, callback) :
    result = 0
    for e in range(x) :
        result += e + x + y
        time.sleep(1)
    callback(result)

def callback(result) :
    print(f"실행 결과를 되돌려 받기 위한 콜백 함수 호출 : {result}")

operation(10,20,callback)

# 데코레이터 : 이미 만들어져 있는 함수의 앞과 뒤에 기능을 추가 할 때 사용
from _datetime import datetime
def datetime_deco(func) : # 핵심 요소가 꾸밈요소 사이에 들어감
    def decorated() :
        print(datetime.now()) # 시작시간
        func() # 핵심 요소가 꾸밈요소 사이에 들어감/ func()에 들어감
        print(datetime.now()) # 끝나는 시간
    return decorated

@datetime_deco # 핵심 요소
def for_sum() :
    sum = 0
    for i in range(1,100+1):
        sum += i
    print(sum)

for_sum()