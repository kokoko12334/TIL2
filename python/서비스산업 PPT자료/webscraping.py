import requests
#step1 사이트 받아오고 정상적으로 받아왔는지 확인
res = requests.get('https://www.naver.com/') #사이트 받아오기
res.status_code   #사이트를 정상적으로 받았는지 확인

#오류날 시의 상황
if res.status_code == requests.codes.ok:
    print('정상')
else:
    print('에러'+res.status_code)


#위과정을 한번에 하는 함수
res.raise_for_status()  #200이나 아무것도 안나오면 정상처리됨.
print(res.text)  #해당 사이트의 코드내역을 다 불러옴.

#사이트 코드 텍스쳐 저장방법
with open('res.html', 'w', encoding='utf-8') as f:
    f.write(res.text)



#header(접근권한 개념)가 필요한 경우

url = 'https://www.naver.com/'
#구글에서 useragent를 치거나 f12 -> console ->navigator.userAgent치면 나옴
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
 }

res = requests.get(url, headers=header)


#####step 2 파일 분석모드에 넣기
#pip install bs4
#pip install lxml   필요할시에 설치함

from bs4 import BeautifulSoup
#step1
url = 'https://www.naver.com'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

res = requests.get(url, headers=header)
res.raise_for_status
#step2
soup = BeautifulSoup(res.text, 'lxml')     #해당 사이트의 text의 'lxml'의 파셜로 분석을 시작함
print(soup)

#f12 누르고 왼쪽 맨위의 마우스 커서를 갖다대고 해당 코드를 확인한다.
#title항목의 내용 가져오기 ' .태그 하면 그 태고 내용을 가져온다 '
soup.title.get_text()  #문자열로 받아옴
soup.title.contents #리스트로 받아옴

#링크 속성 값들 받아오기
soup.a
soup.a.attrs #앵커 속성의 딕셔너리들
soup.a['href']


#find 메소드 find('태그', attrs = {'class': 값})
new = soup.find('a', attrs = {'class':'nav'}) ;print(new)
new.get_text()  #a안의 텍스트인 '메일'을 받아옴
new.i  #new안의 i태그 항목 검색




#####상속 개념(상대개념)으로 찾기
#step1
url = 'https://comic.naver.com/index'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

    }
ko = requests.get(url, headers = header)
ko.raise_for_status()
#step2
soup = BeautifulSoup(ko.text, 'lxml')
print(soup)

rank1 = soup.find('li', attrs = {'class':'rank01'})
rank1
rank1.a.get_text()

#형에서 동생찾기
rank2 = rank1.next_sibling ;rank2       #보면 '/n'만 나옴 이럴때에는 한번 더 써줌
rank2 = rank1.next_sibling.next_sibling ;rank2
rank2.a.get_text()

rank3 = rank2.next_sibling.next_sibling ;rank3
rank3.a.get_text()

#동생에서 형 찾기
rank22 = rank3.previous_sibling.previous_sibling ;rank22

#부모 찾기(그 다음 상위계층 안의 가족들이 다 나옴)
rank2.parent
#find 메소드 위랑은 별로 차이는 없는데
rank222 = rank1.find_next_sibling('li') ;rank222
rank2222 = rank3.find_previous_sibling('li') ; rank2222

#모든 동생 찾기
rank1.find_next_siblings('li')  #자기 제외

rank2.find_previous_siblings('li') #자기 포함


#find_all 메소드
url = 'https://comic.naver.com/webtoon/list?titleId=748105'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

    }
ko = requests.get(url, headers = header)
ko.raise_for_status()
#step2
soup = BeautifulSoup(ko.text, 'lxml')
print(soup)


cartoon = soup.find('td', attrs = {'class':'title'})  # 맨 위의 항목인 하나만 가져옴
cartoon.get_text()


cartoon = soup.find_all('td', attrs = {'class':'title'})
cartoon
cartoon.get_text()  #이때 모두 가져왔으므로 그냥 쓰면 오류남
cartoon[0].get_text() #인덱싱으로 구분함.
cartoon[0].a.get_text()  #차이점은 \n가 있냐없냐
cartoon[0].a['href']  #주소 불러오기

for i in cartoon:
    print(i.a.get_text())

for i in cartoon:
    print(i.a['href'])




