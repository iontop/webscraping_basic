import requests
from bs4 import BeautifulSoup

url="https://play.google.com/store/movies/top?hl=ko&gl=US"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 어떤 언어에 대한 페이지를 받고 싶은지 보내는 부분
    }

res=requests.get(url, headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")

movies=soup.find_all("div", attrs={"class":"WHE7ib mpg5gc"})
print(len(movies))

# # movies 변수로 가져온 정보를 열어보는 debugging
# with open("movie.html", "w", encoding="utf-8-sig") as f:
#     f.write(res.text) # movie.html로 저장되어 확인하기 어려운 경우가 있음
#     # f.write(soup.prettify()) # html 문서를 가공하여 보여줌

# 가져온 영화 제목 출력
for movie in movies:
    title=movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)