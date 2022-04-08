import csv
import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename="시가총액1-200.csv"
f=open(filename, "w", encoding="utf-8-sig", newline="") # 엑셀파일을 열 때 한글이 깨지면 "utf8" 대신 "utf-8-sig"를 입력
writer=csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") # 글자들이 tab으로 구분되어 있으므로 tab으로 나누어 들어가게 함
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res=requests.get(url+str(page))
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    
    data_rows=soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns=row.find_all("td")
        if len(columns)<=1: # 의미없는 데이터, 5개 종목이후 나오는 공백은 가져오지 않음
            continue
        data=[column.get_text().strip() for column in columns] # .get_text()이후에 .strip()을 붙여 \n, \t 등을 삭제
        #print(data)
        writer.writerow(data)