import re

# ca?e
#care, cafe, case, cave ???

p = re.compile("ca.e")  
# . (ca.e): 하나의 문자를 의미 > care, cafe, case but caffe 같은 건 찾지 못함
# ^ (^de): 문자열의 시작 > desk, destination (O) but fade (X)
# $ (se$): 문자열의 끝 > case, base (O) bur face (X)

# m = p.match("case")
# m = p.match("caffe")
# print(m.group()) # 매칭되지 않으면 에러가 발생함.

def print_match(m): 
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열을 반환
        print("m.string: ", m.string) # 입력받은 문자열을 반환, 함수가 아니라 변수이기 때문에 ()없이 사용해야 함.
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("careless") # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("careless cafe good care") # findall은 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# 정리
# 1. p = re.compile("원하는 형태") >> 보통 패턴을 의미하는 p라는 변수를 사용
# 2. m = p.match("비교할 문자열") >> 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") >> 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") >> 일치하는 모든 것을 "리스트" 형태로 반환