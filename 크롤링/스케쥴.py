import schedule
import time
import requests
from bs4 import BeautifulSoup

# 함수 만드는 def
def perform_web_crawling():
    # 웹 크롤링 작업 수행
    url = "http://www.naver.com"
    resp = requests.get(url)
    if resp.status_code == 200 :
        soup = BeautifulSoup(resp.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작 하도록 구현(항상 같은 시간에 크롤링해서 백엔드로 스케쥴링 함)
schedule.every().day.at("09:44").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # sleep을 1초마다 돌아서 돈다.(sleep 꼭 넣어줘야 함, 최소 1/1000은 줘야 함)