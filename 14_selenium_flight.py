from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.maximize_window() # 창 최대화

url="https://flight.naver.com/flights/"
browser.get(url) # url로 이동

time.sleep(3)

# 가는 날 선택, 
# 강의에서는 LINK_TEXT로 "가는 날"을 찾으면 되는 것으로 나오는데 그렇게 해서는 나오지 않아 XPath로 찾아서 클릭하는 것으로 변경
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 이번 달 27일 선택
browser.find_element(By.LINK_TEXT, "27").click()