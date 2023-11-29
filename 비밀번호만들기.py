# 각 사이트 비밀번호 만들기

# 규칙 : http://naver.com 앞의 http:// 잘라내기
# 규칙 2 : 처음 만나는 점 이후 제거
# 규칙 3 :
# 남은 글자 중 처음 세자리 + 글자 갯수
# + 글자에 포함된 'o'의 갯수 + 글자에 포함된 'k'의 갯수
# + "!" + 자신의 이니셜

url = input("사이트 : ")
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "hsy"
print(f"비밀번호 : " + password)

# 반복 수행 및 종료 조건 추가
# 파일에다가 저장하기
file_name = "password.txt"
fd = open(file_name,"wt")

while True : # True 첫 문자는 대문자로 쓰기
    url = input("사이트 : ")
    if url == "exit" : break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "hsy"
    print(f"비밀번호 : " + password)
fd.write(password + "\n")
fd.close()