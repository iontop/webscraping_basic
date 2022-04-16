from attr import attr
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 요것만 넣으면 됨
options=webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080") #눈에 보이지는 않지만 백그라운드에서 크롬이 돌기 때문에 화면크기를 알 수 없지만 명시적으로 줄 수 있음.

browser=webdriver.Chrome(options=options)
browser.maximize_window()

url="https://play.google.com/store/movies/top?hl=ko&gl=US"
browser.get(url) # 페이지로 이동
browser.find_element(By.LINK_TEXT, "더보기").click()

time.sleep(1) # 화면 뜰 때까지 1초 기다리기

# 자바스크립트를 이용하여 지정된 위치까지 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 바탕화면 > 마우스 우클릭 > 디스플레이 설정 > 1920x1080 확인, 1080 위치까지 내리기

# 자바스크립트를 이용하여 끝까지 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height=browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True: # 무한 반복
    # 자바스크립트를 이용하여 끝까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    current_height=browser.execute_script("return document.body.scrollHeight")
    
    if current_height==prev_height:
        break
    
    prev_height = current_height
    
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png") # headless로 잘 돌고 있는지 확인하기 위하여 스크롤이 끝났을 때 스크린샷을 저장

import requests
from bs4 import BeautifulSoup

soup=BeautifulSoup(browser.page_source, "lxml")

movies=soup.find_all("div", attrs={"class":"Vpfmgd"}) # 여러 클래스를 동시에 가져오려면 리스트 형식으로 묶어줌, "class":["클래스이름1","클래스이름2"]
print(len(movies))

# 가져온 영화 제목 출력
for movie in movies:
    title=movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    
    # 할인 전 가격
    original_price=movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price=original_price.get_text()
    else:
        # print(title, "  <할인되지 않은 영화 제외>")
        continue
    
    # 할인 된 가격
    price=movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"})
    if price:
        price=price.get_text()
    
    # 링크 정보
    link=movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 연결이 되려면 href가 <a href="/store/movies/details/~>로 되어 있으므로 앞에 https://play.google.com을 붙여주어야 함
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : ", "https://play.google.com" + link)
    print("-"*120)
    
browser.quit()