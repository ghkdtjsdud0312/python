# 회원정보 출력하기
name = input("이름을 입력 하세요 : ")
while True :
    age = input("나이를 입력 하세요 : ")
    if age.isdigit() : # 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : break
    print("나이를 잘 못 입력 하셨습니다.")

while True :
    gender = input("성별을 입력 하세요 : ")
    if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f': break
    print("성별이 잘 못 되었습니다.")

while True :
    jobs = input("직업을 입력 하세요 : ")
    if jobs.isdigit() :
        jobs = int(jobs)
        if 0 < jobs < 5 : break
    print("직업을 잘 못 입력 하셨습니다.")

if gender == 'M' or gender == 'm' : gen_str = "남성"
else: gen_str = "여성"

jobs_str = "", "학생", "회사원", "주부", "무직" # 안 써도 튜풀가능(튜플) / 임의로 만들어진 데이터를 여러군데 나눠 담는 것
print("="*3, "회원정보", "="*3)
print(f"""이름 : {name}
나이 : {age}
성별 : {gen_str}
직업 : {jobs_str[jobs]}
""")

# 2번문제 : 핸드폰 요금 계산하기
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원
n=int(input()) # 통화 횟수
call = list(map(int, input().split())) # 통화 횟수에 대한 통화 시간 /list는 크기를 늘리는 것
# input을 받고 문자열로 받는다.
# split은 공백 한칸 기준으로 쪼개서 int 형으로 바꿈
# map은 입력 받은걸 앞에 원하는 타입으로 바꿈, 함수도 가능
# list는 받아 주는 애가 있어야 하는데 알수가 없으니 갯수가 정해 지지 않은 배열을 만들수 있어 쓴다.
y_pay = m_pay = 0
for i in range(n) :
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M",m_pay)
elif y_pay < m_pay:
    print("y",y_pay)
else:
    print("Y M",y_pay)

# 3번 문제 : 대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력 받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
import IPython.extensions.autoreload

rst = "" # 공백 만들어 줘야 에러가 안남/ 외부에서 미리 만들어놓고 집어넣어야 해서 공백으로 만들어둠
for e in input() : # 입력 받는 문자열 만큼 자동 순회
    if e.islower():
        rst += e.upper() # 공백에 문자욜 추가되서 대문자로 만들어 줌
    else:
        rst += e.lower()
print(rst)

# 4번 문제 : 숫자의 개수
# A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력

a,b,c = map(int,input("정수 3개 입력 : ").split())
total_val = str(a * b * c) # a * b * c 결과를 문자열 변환
for i in range(10) :
    print(total_val.count(str(i))) # count 동일한 문자가 몇개 나오는지 궁금할 때 사용
