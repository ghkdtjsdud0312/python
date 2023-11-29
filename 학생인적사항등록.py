# 학생 인적사항 등록
# 메뉴 구성 : 등록 / 검색 / 수정 / 전체 보기 / 저장 / 불러오기 / 종료
# JSON 형태로 저장하고 불러오기

import json
student_map = {}

# 학생 정보 등록
def reg_student() :
    student_id = input("학번 입력 : ")
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    student_map[student_id] = {"이름": name, "주소": addr}
    print(f"{name}님의 정보가 등록 되었습니다.")

# 학생 정보 검색
def search_student() :
    student_id = input("검섹 힐 힉번 입력 : ")
    student_info = student_map.get(student_id)
    if student_info :
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")
    else:
        print("해당 핟번의 학생 정보를 찾을 수 없습니다.")

# 학생 정보 저장
def save_student() :
    with open("student.json",'w',encoding='utf-8') as file :
        json.dump(student_map,file,ensure_ascii=False)
    print("학생 정보가 저장 되었습니다.")

# JSON 파일을 불러 옴
def load_student() :
    try :
        with open("student.json",'r',encoding='utf-8') as file:
            student_map.clear()
            student_map.update(json.load(file))
        print("학생 정보를 불러왔습니다.")
    except FileExistsError:
        print("학생 정보가 저장된 파일을 찾을 수 없습니다.")
# 학생 정보 변경
def modify_student() :
    student_id = input("수정 할 학번 입력 : ")
    student_info = student_map.get(student_id)
    if student_info :
        name = input("새로운 이름 입력 : ")
        addr = input("새로운 주소 입력 : ")
        student_info['이름'] = name
        student_info['주소'] = addr
        print(f"{name}님의 주소가 수정되었습니다.")
    else: print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# 학생 정보 삭제
def delete_student() :
    student_id = input("삭제 할 학번 입력 : ")
    if student_map.get(student_id) :
        del student_map[student_id]
        print("학생 정보가 삭제 되었습니다.")
    else : print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# 학생 정보 보기
def view_all_student() :
    for student_id in student_map :
        student_info = student_map[student_id]
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")

while True :
    print("="*5,"학생 정보 관리 프로그램","="*5)
    choice = input("[1]등록 [2]검색 [3]수정 [4]삭제 [5]전체보기 [6]저장 [7]불러오기 [8]종료 : ")
    if choice == "1":
        reg_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        modify_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        view_all_student()
    elif choice == "6":
        save_student()
    elif choice == "7":
        load_student()
    elif choice == "8":
        break
    else:
        print("선택한 메뉴가 없습니다.")
