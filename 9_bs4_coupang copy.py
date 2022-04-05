import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

for i in range(1,6):
    print("\n*** 현재 페이지는 ", i, " 번째 페이지 입니다.***")
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
        
    res = requests.get(url, headers = headers, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    
    for item in items:
        
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
        if ad_badge:
            # print("<광고 상품은 제외합니다.>")
            continue
        
        # 사전 예약 제품도 제외
        pre_order_badge = item.find("span", attrs = {"class":"pre-order-badge-text"})
        if pre_order_badge:
            # print("<사전 예약 제품은 제외합니다.")
            continue
        
        
        name = item.find("div", attrs={"class":"name"}).get_text()
        
        # 애플 제품 제외
        if "Apple" in name:
            # print("<애플 상품은 제외합니다.>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        
        
        rate = item.find("em", attrs={"class":"rating"})
        if rate: # 평점이 없는 상품이 있을 수 있으므로
            rate = rate.get_text()
        else:
            # rate="평점없음"
            # print("<평점 없는 상품은 제외합니다.>")
            continue
    
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt: # 평점이 없으면 리뷰 수도 없기 때문에
            rate_cnt = rate_cnt.get_text()[1:-1] # 출력이 (25)와 같이 되고 있음, slicing 두번째 글자(1)부터 마지막 앞(-1)까지

        else:
            # rate_cnt="평점 수 없음"
            # print("<평점 수 없는 상품은 제외합니다.>")
            continue
        
        link = item.find("a", attrs = {"class":"search-product-link"})["href"]

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회 하도록 변경
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate} ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com/" + link))
            print("-" * 100) # 줄 긋기
            
        



    
