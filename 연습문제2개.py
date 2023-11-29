# 배수 찾기
# 1. 첫째 줄에 n이 주어짐, 다음 줄부터 값이 주어짐
# 목록에 있는 수가 n의 배수인지 아닌지 판별
# 0을 입력 하면 목록이 끝남

n = int(input())
ls = []
while True :
    x = (int(input()))
    if x == 0 : break
    ls.append(x)

for e in ls:
    if e % n == 0: print(f"{e} is multiple of {n}.")
    else: print(f"{e} is Not multiple of {n}.")


# 피타고라스 정리
# 피타고라스의 정리 : 직각삼각형에서 빗변을 제외한 나머지 두 변의 길이를 각각 제곱해 더하면 빗변의 길이의 제곱과 같다.

rst= []
while True :
    li = list(map(int,input().split()))
    li.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0: break
    elif li[2]**2 == li[1]**2 + li[0]**2:
        rst.append("right")
    else:
        rst.append("wrong")

for e in rst : print(e)
