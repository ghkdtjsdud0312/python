#def 함수이름(매개변수): # parameter
#	실행할 코드
#	return 변수
#함수명(인수)   # argument

# 함수란? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램

# 이름, 주소, 전화번호를 매개변수로 전달받아 출력하는 함수(바뀌는 부분)

# 반복 호출
def name_card(name, addr, phone) :
    print(f"주소 : {addr}")
    print(f"전화번호 : {phone}")
    print(f"이름 : {name}")
    print(f"회사 : KH정보교육원") # 공통된 부분

# 함수는 선언 이후 호출 해야만 동작 함, 한번 만들어진 함수를 여러번 호출하여 반복되는 코드를 줄임
name_card("안유진","서울시 강남구 삼성동","010-1234-5678")
name_card("장원영","서울시 강남구 역삼동","010-1234-0000")
name_card("이서","서울시 강남구 청담동","010-1111-2222")

# 계좌 개설 (뮤터블 변수)
def open_account(name) :
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name # 반환 값으로 이름을 전달

# 입금 함수
def deposit(input) : # 잔고와 입금액을 매개변수로 전달 받음
    global balance
    balance += input
    print(f"{input}이 입금 되었습니다. 잔액은 {balance}입니다.")

# 출금 함수
def withdraw(output) :
    global balance
    if balance >= output :
        balance -= output
        print(f"{output}이 출금 되었습니다. 잔액은 {balance}입니다.")
    else:
        print(f"출금이 실패 했습니다. 잔액은 {balance} 입니다.")

balance = 0 # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
name = open_account("곰돌이사육사")
deposit(1000)
withdraw(500)
print(f"{name}의 잔액은 {balance}입니다.")

# 순차 검색
def search_list(a,x) :
    for i in range(len(a)) :
        if x == a[i] : return i
    return -1

v= [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v,33))
print(search_list(v,18))
print(search_list(v,100))

# 기본값 인자 : 함수 선언 시 매개변수에 대해서 기본 값을 정의 할 수 있음
# 매개변수에 기본 값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값이 호출 됨
def profile(name,year = 2, age = 18, school = "태양고"):
    print(f"이름 : {name}, 학교 : {school}, 학년 : {year}, 나이 : {age}") # 이름 빼고 초기값이 들어감

profile("나희도")
profile("고유림")
profile("백이진",None,22)

# 가변 매개변수 : 변수의 개수가 정해지지 않은 경우에 사용
# *(별표)를 붙여주면 함수의 매개변수를 몇개를 입력하든 함수내에서 튜플로 인식-> 전부를 의미(all)
def profile(name,age,*lang) :
    print(f"이름 : {name}, 나이 : {age}",end=" ")
    for e in lang:
        print(e,end=" ")
    print()

profile("나희도",18,"Python","Java","C","C++","REACT")
profile("조세호",38,"Python","Java","Swift")
profile("유재석",47,"Java","Kotlin")

# 지역변수 사용
knife = 10 # 칼을 10자루 준비
def game(player) :
    global knife
    knife -= player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")


player = int(input("경기에 참여 하는 학생이 몇명 입니까? : "))
game(player)
print(f"경기에 사용하고 남은 칼은 {knife} 자루 입니다.")

# 람다란? 간단한 함수의 선언과 하나의 식으로 간략히 표현 한 것
# 파이썬에서 람다 함수를 통해 이름이 없는 함수를 만들 수 있음
# 람다함수의 장점은 코드의 간결함, 메모리의 절약이라고 생각 함
def add(a,b):
    return a + b

print(add(1,2))

print((lambda a,b: a+b)(1,2))

# 람다식
def power(n) : # 제곱근/ 함수를 선언하는 방법
    return n * n

power_l = lambda n: n * n # 람다식으로 만들어 변수에 대입하는 방법

in_ = [1,2,3,4,5]

out_ = list(map(lambda n: n * n, in_)) # 함수 자리에 람다식으로 익명의 함수를 만들어 넣는 방법
print(out_)


# 리스트에 람다 함수를 넣는 방법도 가능
my_list = [lambda a,b: a*b, lambda a, b : a+b]
print(my_list[0](5,2))
print(my_list[1](5,2))

