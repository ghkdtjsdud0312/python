# 1번 문제 : 상근날드, 초급문제
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류
# 입력 : 연속해서 3종의 햄버거, 2종의 음료 가격 입력
# 출력 : 헴버거 3종 중 가장 싼 메뉴 + 음료 2종 총 싼거 - 50 한 결과 값

ls = list(map(int,input().split()))
min_b = min(ls[:3])
min_d = min(ls[3:5])
print(f"{min_b + min_d - 50}")

# 2번 : 저항, 중급문제
# 입력 : 3개의 저항값 입력
# 저항에 대한 색상 : "black","brown","red","orange","yellow","green","blue","violet","grey","white"
# 첫번째 색상은 10의 자리수, 두번째 수는 1의 자리수, 세번째 자리수는 곱해야 하는 수(1, 10, 100 ....)

color = "black","brown","red","orange","yellow","green","blue","violet","grey","white"
f_name= color.index(input())
s_name= color.index(input())
t_name= color.index(input())
print(int(str(f_name)+str(s_name))*(10**t_name))

# 3번 : PC방 알바, 중급문제
#1~100번까지의 컴퓨터가 있음
# 손님은 자리에 앉고 싶어하는 자리를 선택하고자 한다. 이미 예약된 자리는 선택할 수 없으므로 거절해야 하며, 거절 횟수를 구하는 문제

seat_num = list(map(int, input().split()))
pc = [0]*100 # 0으로 초기화된 100개의 리스트 생성
cnt = 0
for i in seat_num:
    if pc[e-1] != 0: cnt+=1 # 예액된 좌석이 없음 사용가능
    else: pc[e-1] == 1 # 이미 좌석이 있는 자리
print(cnt)

# 4번 문제
# `Knuth-Morris-Pratt => KMP, Mirka-Slavko => MS`
upper_str = ""
for e in input():
    if e.isupper():upper_str+=e
print(upper_str)

