# 세 자리수 중에서 가장 큰수
n= int(input("세자리 정수 입력 : "))
a= n // 100
b= (n % 100) // 10
c= n % 10
if a> b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)

# 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
근무타임 = int(input("주간근무[1], 야간근무[2]를 입력하세요 :"))
근무시간 = int(input("근무 시간을 입력하세요 : "))
if 근무타임 == 1:
    급여 = 근무시간 * 9620
else: 급여 = 근무시간 * 9620 * 1.5

근무타임문자열 = 근무타임 == 1 and "주간" or "야간"
print(f"{근무시간}시간 동안 근무한 {근무타임문자열} 급여는 {급여}원 입니다. ")

#문자열 추가하기
s = input("s 문자열 : ")
k = input("k 문자열 : ")
n = int(input("정수 입력 : "))
print(s[-n:] + k)
