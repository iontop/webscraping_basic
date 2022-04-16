from operator import contains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser=webdriver.Chrome()
browser.maximize_window() # 창 최대화

url="https://flight.naver.com/flights/"
browser.get(url) # url로 이동

time.sleep(0.5)

# 가는 날 선택, 
# 강의에서는 LINK_TEXT로 "가는 날"을 찾으면 되는 것으로 나오는데 그렇게 해서는 나오지 않아 XPath로 찾아서 클릭하는 것으로 변경
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(0.5)

# 이번 달 27일 선택
# '나도코딩'강의에서는 browser.find_elements_by_link_text("27")[0].click()로 설명하였으나 되지 않아 수정함
# LINK_TEXT로 찾으려면 <a> tag 안에 있어야 함
# XPath를 분석: //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{Month}]/table/tbody/tr[{Week}]/td[{Day}]/button/b
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button/b').click()
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button/b').click()

# 다음 달 선택
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button/b
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button/b').click()
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[6]/button/b').click()

# 위치 선택
# //*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b # 출발지
# //*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b # 도착지

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b').click() # 출발지 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click() # 국내 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[3]/i[1]').click() #부산 선택


browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click() # 도착지 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click() # 국내 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]/i[1]').click() #제주 선택

# 항공권 검색
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()

# Loading을 기다려야 함
# time.sleep은 시간 낭비가 있을 수 있음.
# element가 나올 때까지 기다렸다가 element가 나오면 다음으로 넘어가서 처리하게 할 수 있음. - WebDriverWait / expected_conditions 이용

# 10초 동안 기다렸는데 결과가 안나오면 진행시키는 것이 의미가 없으므로 try, finally 사용하여 브라우저 종료
try:
# 원하는 XPATH가 나올 때까지(until) 10초 동안 기다리다가 나오면 다음으로 넘어감
    elem=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div')))
    print(elem.text)
finally:
    browser.quit()