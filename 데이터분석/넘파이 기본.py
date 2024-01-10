 # 넘파이(np)는 배열이라 생각하기, 제약 조건이 많음
import numpy as np

# [] : 리스트
# {} : 딕셔너리
# () : 튜플 / 괄호가 없어도 튜플

data = [0,1,2,3,4,5,6,7,8,9,10] # 리스트로 데이터 생성(읽고 쓸 수 있는 배열 형태, 아무 데이터 다 올 수 있고 넘파이를 변환하기 위해 정수만 가능)
a1 = np.array(data) # 리스트를 넘파이 배열로 변환
print(a1)

# 묵시적 타입 캐스팅(자동적으로 형 변환이 일어남)
data2 = [0,1,2,3,4,5,1.56,3.14,0.3333]
a2 = np.array(data2)
print(a2)

x = np.array([0.1,0.2,0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄 (3행, 열)
print(x.dtype) # 배열 요소의 타입 확인(64비트 부동소수점 형태)

y = np.array(([1,2,3],[4,5,6])) # 2행 3열 / 2차원 배열 [[]]
print(y)
print(y.shape) # 배열의 형태를 나타냄 (2행 3열)
print(y.dtype) # 배열 요소의 타입 확인(32비트 int 형태)

# 범위를 지정해 배열 생성
a3 = np.arange(0,10,2) # 0에서 10미만, 간격은 2
print(a3)

a4 = np.arange(1,20) # 1에서 20미만, 간격은 1
print(a4)

# 배열 형태 변경, 0 ~ 12 미만 배열 생성 (배열은 0 부터 시작)
a5 = np.arange(12).reshape(4,3) # 4행 3열로 구조 바꿈/ reshape는 배열의 구조를 변경
print(a5)
print(a5.shape)

# 배열의 시작과 끝 지정, 그리고 데이터의 개수를 지정해 배열 생성
a6 = np.linspace(1,10,3) # 시작, 끝, 개수를 지정하면 시작과 끝 범위 내에서 값이 적절히 분포가 됨(시작과 끝 포함)
print(a6)

a7 = np.linspace(0, np.pi, 20)
print(a7)

# 특별한 형태의 배열 생성
# 1차원 배열
a8 = np.zeros(10) # 0으로 채워진 10개 배열 생성
print(a8)

a9 = np.zeros((3,4)) #3행 4열로 만들어진 배열로 만들어짐
print(a9)

a10 = np.ones(10) # 1으로 채워진 10개 배열 생성
print(a10)

a11 = np.ones((5,5)) # 1로 채워진 5행 5열 형태
print(a11)

# 단위 행렬 생성 : n * n 정사각형의 행렬에서 주 대각선이 모두 1
a12 = np.eye(4) # 대각선 방향으로 1이 모두 들어가져 있음
print(a12)

# 배열의 타입 변환 : 배열은 숫자 뿐만 아니라 문자열도 요소로 가질 수 있음(단, 같은 타입이어야 함)
a13 = np.array(['+1.5','0.62','-2','3.14','3.141592'])
print(a13)
print(a13.dtype) # <U8 의미 : 데이터 형식이 유니코드(아스키값으로 대응,문자를 표시할 때)이며 문자의 최대 8개라는 의미('3.141592' -> 8개)
print(a13.shape)

num_a13 = a13.astype(float) # 문자열을 실수 타입으로 형 변환
print(num_a13)

# 난수 배열의 생성 : 0 ~ 1미만의 임의의 실수로 난수를 발생 시킴
a14 = np.random.rand(2,3)
print(a14)
print("")

a15 = np.random.rand(2,3,4)
print(a15)

# 지정한 범위에서 해당하는 정수로 난수 배열 생성
a16 = np.random.randint(10, size=(3,10)) # 0~10 미민의 정수 난수 발생
print(a16)

# 배열의 연산 : 넘파이의 배열은 배열의 형태가 같다면 사칙연산 수행 가능함
# (연산자 오버로딩 - c++가능, 자바는 불가능)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
print(result)
result1 = arr1 * arr2
print(result1)
result2 = arr1 ** arr2
print(result2)

# 요소별 연산 : true, false로 반환
arr3 = np.array([10,20,30,40,50])
print(arr3 > 20)

# 통계를 위한 연산 : 배열의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적곱 등의 통계에서 많이 사용되는 메소드
arr4 = np.arange(5) # 0에서 부터 5미만의 값으로 구성된 배열 생성
print(arr4)
print(f"합계:{arr4.sum()}") # f는 포맷, 자바스크립트의 백틱이랑 비슷
print(f"평균:{arr4.mean()}")
print(f"표준편차:{arr4.std()}") # 데이터가 얼마나 떨어져있는가
print(f"분산:{arr4.var()}")
print(f"최소값:{arr4.min()}")
print(f"최대값:{arr4.max()}")

# 배열 인덱싱
arr5 = np.arange(1,6)
print(arr5)
print(arr5[3]) # 세번째 인덱스의 값을 나타냄
print(arr5[0])

# 배열 슬라이싱 : 값을 잘라냄
new_arr = arr5[1:3] # 1번 인덱스에서 3번 인덱스 미만의 값만 값을 슬라이싱
print(new_arr)

# universal 함수 : 배열의 원소별 연산을 지원하는 함수
# 산술연산 : add(), substract(), multiply(), divide(), power()-> 거듭제곱
# 삼각함수 : sin() cos() tan()
# 지수와 로그 : exp(), log(), log10()
# 집계함수 : sum(), mean(), max(), min()
# 논리함수 : logical_and(), logical_or(), logical_not()
xx = np.arange(0., 2*np.pi, 0.1)
print(np.pi) # pi값
yy = np.sin(xx)
print(yy)

matrix1 = np.array([[1,2],[4,5]])
matrix2 = np.array([[5,6],[7,8]])
# 행렬 덧셈
res = np.add(matrix1, matrix2)
print(res)

# 정렬과 탐색 : 배열의 정렬과 탐색을 위한 함수와 메소드
xxx = np.array([9,8,7,2,3,4,6,11])
print(np.amin(xxx)) # 배열내에 있는 최소값 찾기
print(np.amax(xxx)) # 배열내에 있는 최대값 찾기
print(np.max(xxx)) # 최대값
print(np.argmin(xxx)) # 배열내의 최소값의 위치
print(np.argmax(xxx)) # 배열내의 최대값의 위치
print(np.sort(xxx)) # 오름차순
print(np.sort(xxx)[::-1]) # 내림차순
print(np.argsort(xxx)) # 값의 인덱스

# 브로드 캐스팅 : 배열의 크기가 다른 경우에 연산을 수행하도록 헤주는 기능
ax = np.array([1,2,3]) # 1차원 배열
bx = np.array([[4],[5],[6]]) # 2차원 배열 (3*1)로 구성된 2차원 배열
cx = ax + bx
print(cx)



