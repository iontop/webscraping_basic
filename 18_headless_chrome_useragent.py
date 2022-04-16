from attr import attr
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 요것만 넣으면 됨
options=webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080") #눈에 보이지는 않지만 백그라운드에서 크롬이 돌기 때문에 화면크기를 알 수 없지만 명시적으로 줄 수 있음.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

browser=webdriver.Chrome(options=options)
browser.maximize_window()

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36
detected_value=browser.find_element(By.ID, 'detected_value')
print(detected_value.text)

# user agent를 add_argument에 넣어주지 않으면 아래와 같이 나옴
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4896.75 Safari/537.36
# HeadlessChrome 라는 글자가 붙음, 이 때문에 차단되는 경우도 많음.

browser.quit()