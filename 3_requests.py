import requests

# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
# res = requests.get("http://nadodcoding.tistory.com")
# print("응답코드", res.status_code) # 200이면 정상, # 403은 접근 권한이 없다는 의미

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#         print("문제가 있습니다. [에러코드 ", res.status_code, " ]")

# 위와 같이 if문을 사용하는 방법 대신 raise_for_status()를 사용하는 방법도 있음.
# 실제 사용할 경우에는 reqeusts.get() 다음에 이어서 raise_for_status()를 사용할 것
res.raise_for_status()
#print("웹스크래을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)