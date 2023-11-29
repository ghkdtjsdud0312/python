# 연산자
tax_rate = 0.10
income = int(input("당신의 수입은 얼마입니까? : "))
print(f"당신이 내야 할 세금은 :{income*tax_rate:.2f} 입니다.")

# 조건문
#if ~ elif ~ else문
n = int(input("정수를 입력 하세요 :"))
if n > 100 :
    print(f"{n}은 100보다 커요")
elif n < 100:
    print(f"{n}은 100보다 작아요.")
else:
    print("100과 같아요.") # pass 넣어도 됨

# 문자열 비교
season = input("현재 계절을 입력 하세요. : ")
if season == "spring" :
    print("봄이 왔어요.")
elif season == "summer" :
    print("무더운 여름입니다.")
elif season == "fall"or season == "autumn" :
    print("선선한 가을 입니다.")
elif season == "winter" :
    print("추운 겨울이 왔어요.")
else:
    pass

# 회원 가입을 위한 아이디와 패스워드 입력 받기
user = int(input("아이디 입력 : "))
if len(user) >= 8 :
    pw = input("비밀번호를 입력하세요.")
    if len(pw) > 8 or len(pw) < 16:
        print("비밀번호는 8자에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else:
    print("아이디는 반드시 8자 이상이어야 합니다.")



