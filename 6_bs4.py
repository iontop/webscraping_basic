import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 첫번째로 발견되는 a element를 출력하라는 뜻
# print(soup.a.attrs)
# print(soup.a["href"]) # a element의 herf 속성을 출력

# soup.find("a", attrs={"class":"Nbtn_upload"})
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class값이 유일할 경우에는 a element가 없어도 됨. element가 무엇이든 관계없음

# 인기 급상승 만화를 찾아서 가져옴
#print(soup.find("li", attrs={"class":"rank01"})) # 이렇게 하면 a element 내용이 모두 끌려오기 때문에 링크만 필요하면...
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())


## next_sibling을 사용하는 방법 ##

# rank1.next_sibling
# print(rank1.next_sibling) # HTML 사이에 개행정보 같은 것이 있으면 .next_sibling을 사용해서 다음 것을 찾을 때 아무것도 출력되지 않을 수 있음.
# print(rank1.next_sibling.next_sibling) # 이럴 때는 .next_sibling을 하나 더 쓸 것
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

# print(rank2.get_text())
# print(rank3.get_text())

## next 대신 previous를 써서 이전 값을 가져올 수도 있음 ## 

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())

## parent를 사용하면 상위 전체 내용을 가져올 수 있음 ##

# print(rank1.parent) # 상위(부모) 메뉴의 정보를 가져올 때 사용

## next_sibling을 사용할 때 개행정보가 있으면 여러 번 써야 하므로 이를 해결하기 위해 find_next_sibling을 사용 ##

# rank2 = rank1.find_next_sibling("li") # .next_sibling을 두 번 쓰지 않고 패턴을 이용하여 다음 sibling을 찾는 방법
# print(rank2.get_text())

# rank3 = rank2.find_next_sibling("li") # next 대신 previous를 사용할 수 있음.
# print(rank3.get_text())

## 한 번에 모든 정보를 가져온 다음 처리하는 방법 ##

# print(rank1.find_next_siblings("li")) # sibling이 아닌 siblingS를 사용

## find 명령 이용 ##

webtoon = soup.find("a", text = "여신강림-197화") # 모든 element 중에서 a 태그에 포함된 text가 있는 정보를 가져오라는 의미
print(webtoon)