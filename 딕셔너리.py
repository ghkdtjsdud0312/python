# 딕셔너리 : 키와 값이 한쌍으로 이루어진 구조
# 중괄호{} 감싸서 선언, 쉼표(,)로 구분
# 키와 값은 클론(:)으로 구분

coffee_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte" : 4000, "Moca" : 4500}
tea_menu = {"Black tea" : 4000, "Green tea" : 4000, "Milk tea" : 3500}
food_menu = {"Cake " : 5000,"Bakery" : 6000, "Ice Cream" : 7000}
print(coffee_menu)
print(food_menu)
print(coffee_menu["Americano"])
print(food_menu.get("Latte")) # get을 넣어서 값이 있는지 확인함

# 추가 : **`딕셔너리[키] = 값`** 새로운 키와 값을 추가 할 수 있음
# 삭제: **`del 딕셔너리[키]`** 형식으로 써 줌
# 키존재 여부 확인 :  **`if 키 in 딕셔너리KEY`**
# 키로 값 확인 : **`딕셔너리[키]`**  또는 **`딕셔너리.get(키)`**

# update 함수 : 딕셔너리의 데이터를 한꺼번에 바꿀 때 사용함
dict = {"곰돌이사육사" : 90, "안유잔" : 88, "장원영" : 77}
dict.update({"곰돌이" : 100, "장원영" : 100})
print(dict)

# 정보 얻기 : keys(), values(), items() 함수의 반환값으로 딕셔녀리의 정보를 확인
# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
dict1 = {"자바":80,"JavaScript":88,"HTML":70}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print("HTML" in dict1) # 참, 거짓으로 판별
print("Python" in dict1)
print(dict1.get("Python")) # 없는 값은 none으로 나옴

# for 반복문 사용하기 : 딕셔너리 내부의 키가 자동으로 key 할당
for key in coffee_menu :
    print(key,":",coffee_menu[key])


