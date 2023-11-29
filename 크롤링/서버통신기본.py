import requests
import json

#JSON 데이터 생성
data = {
    "id": "곰돌이사육사",
    "pwd": "sphb8250"
}
#json 데이터 서버로 전달하기
url = "http;//localhost:8111/test/python"
header = {"Content-Type": "application/json"}
resp = requests.post(url, data=json.dumps(data), headers=headers)

#서버 응답 확인
if resp.status_code == 200:
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print("데이터 전송에 실패 했습니다.", resp.status_code)