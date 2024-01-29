import re
#정규표현식에 대한 실습: https://regexr.com/

p = re.compile('ca.e')  #조건식

m = p.match('case')  #필터링 시킬 문자열
m.group() #결과보기

#오류나옴
m = p.match('cccs')
m.group()
#대처
if m:
  print(m.group())
else:
  print('Error')

#함수로 만들어 놓기
def print_match(m):
    if m:
        print(m.group())
    else:
        print('Error')    

print_match(m)


p = re.compile('ca.e')
m  = p.match('11case')    #case123하면 case가 나옴 match메소드는 앞에 case가 먼저 나와야함.
print_match(m)


#search 메소드(match와는 다르게 위치 상관 없음)
m = p.search('123case')
print_match(m)

#그 외
def print_match(m):
  if m:
    print(f'm.group: {m.group()}')    #조건식에 맞는 문자열 출력
    print(f'm.string(): {m.string}')  #필터링한 문자열
    print(f'm.start: {m.start()}')    #해당 조건식에 맞는 문자열의 시작인덱스
    print(f'm.end: {m.end()}')        #해당 조건식에 맞는 문자열의 끝인덱스 이때 슬라이싱처럼 끝은 -1인 형식임
    print(f'm.span: {m.span()}')      #시작, 끝 인덱스
  else:
    print('Error')


p = re.compile('ca.e')
m = p.search('good case')
print_match(m)
print('='*80)
m = p.search('caseless')
print_match(m)


p.findall('goodcare') #리스트로 반환함.


#정규표현식과 웹스레이핑
###쿠팡의 노트북 이름, 가격, 평점, 후기 빼오기 정규표현식+웹스크레이핑
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

}
res = requests.get(url, headers= header)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print(soup.text)



#items는 이터러블객체 형태(?)여서 인덱싱으로 지정하고 해주어야함.(클래스에 정규표현식조건식을 넣음)
items = soup.find_all('li', attrs = {'class':re.compile('^search-product')}) 
#중간에 search-product가 있을 수 있으므로 맨 처음을 나타내는 ^를 씀
print(items[0].find('div', attrs = {'class':'name'}))


for i in items:
    name = i.find('div', attrs = {'class': 'name'}).get_text()
    name = name.split(',')[0]
    
    price = i.find('strong', attrs = {'class':'price-value'}).get_text()
    
    rating = i.find('em', attrs = {'class':'rating'})
    if rating:
        rating = rating.get_text()
    else: 
        rating = '평점없음'

    rate_count = i.find('span', attrs = {'class':'rating-total-count'})
    if rate_count:
        rate_count = rate_count.get_text()
    else:
        rate_count = '정보없음'

    ad = i.find('span', attrs = {'class':'ad-badge-text'})
    if ad:
        # ad = '광고제품'
        continue  #아래의 print까지가 한 과정인데 이걸로인해 넘어가게 되서 위에서 할당은 되더라도 프린트가안됨
    else:
        ad = '광고제품 아님'

    co = i.find('img', attrs = {'class':"badge-ico badge-coupick"})
    if co:
        # co = '***쿠팡 추천제품임***'
        continue              
    else:
        co = '쿠팡추천제품아님'
    print('='*80)
    
    print(f'제품명:{name}')
    print(f'가격:{price}')
    print(f'평점:{rating}')
    print(f'후기수:{rate_count}')
    print(ad)
    print(co)














