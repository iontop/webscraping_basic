import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser=webdriver.Chrome("./chromedriver.exe") # chromedriver.exe가 있는 경로 입력

# 네이버에서 검색
# browser.get("http://naver.com")

# elem=browser.find_element_by_class_name("link_login") # 로그인 화면으로 오기
# elem.click()
# browser.back() # 뒤로가기
# # browser.forward() # 앞으로가기
# # browser.refresh() # 새로 고침
# elem=browser.find_element_by_id("query") # 검색창 화면에서 검색어 넣기 직전
# elem
# elem.send_keys("나도코딩") # 검색어 입력
# elem.send_keys(Keys.ENTER) # 엔터를 치는 것과 같은 역할

# elem=browser.find_elements(By.TAG_NAME, "a") # 예전에는 이렇게 사용 >> elem=browser.find_element_by_tag_name("a")

# for e in elem:
#     e.get_attribute("href")

# 다음에서 검색
# browser.get("http://daum.net")
# elem=browser.find_element(By.NAME, "q")
# elem.send_keys("창원벚꽃")
# elem=browser.find_element(By.XPATH, '//*[@id="daumBtnSearch"]') # 엔터치는 대신 검색버튼의 XPath를 불러옴
# elem.click()

# browser.close() # 현재 열려있는 탭만 종료
# browser.quit() # 전체 브라우저 종료

# 네이버 로그인 해보기
browser.get("http://naver.com")

browser.find_element(By.CLASS_NAME, "link_login").click() # 로그인 화면으로 오기
browser.find_element(By.ID, 'id').send_keys("ultimateant") # 저장할 필요가 없으니 바로 .send_keys로 보냄
browser.find_element(By.ID, 'pw').send_keys("next1234!")
# browser.find_element(By.ID, 'log.login').click() # 네이버는 이렇게 자동으로 로그인 할 수 없게 되어 있음

# browser.find_element(By.ID, 'id').clear() # id에 있는 기존 글자를 지우기 위해서 clear 사용

print(browser.page_source) # page source를 출력 >> 이걸로 웹스크래핑 작업이 가능

browser.quit()